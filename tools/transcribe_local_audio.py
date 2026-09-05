"""Transcribe a local folder of MP3 files without uploading the audio.

This utility deliberately writes raw ASR output only to the path supplied by
the operator. Raw publisher transcripts must not be committed to this public
repository; use them only to build concise, source-grounded reference cards.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_jsonl", type=Path)
    parser.add_argument("model_dir", type=Path)
    parser.add_argument("--vendor-dir", type=Path)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--compute-type", default="int8")
    parser.add_argument("--language", default="en")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.vendor_dir:
        sys.path.insert(0, str(args.vendor_dir))

    from faster_whisper import WhisperModel

    files = sorted(args.input_dir.glob("*.mp3"))
    if not files:
        raise SystemExit(f"No MP3 files found in {args.input_dir}")

    model = WhisperModel(
        str(args.model_dir),
        device=args.device,
        compute_type=args.compute_type,
        local_files_only=True,
    )
    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)

    with args.output_jsonl.open("w", encoding="utf-8") as output:
        for index, audio_path in enumerate(files, start=1):
            segments_iter, info = model.transcribe(
                str(audio_path),
                language=args.language,
                beam_size=5,
                temperature=0,
                vad_filter=True,
                condition_on_previous_text=False,
            )
            segments = [
                {
                    "start": round(segment.start, 3),
                    "end": round(segment.end, 3),
                    "text": segment.text.strip(),
                }
                for segment in segments_iter
            ]
            record = {
                "source_file": audio_path.name,
                "duration_seconds": round(info.duration, 3),
                "language": info.language,
                "language_probability": round(info.language_probability, 5),
                "text": " ".join(item["text"] for item in segments).strip(),
                "segments": segments,
            }
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            output.flush()
            print(f"[{index}/{len(files)}] {audio_path.name}", flush=True)


if __name__ == "__main__":
    main()
