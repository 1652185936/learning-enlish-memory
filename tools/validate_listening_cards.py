"""Validate public listening-card coverage against a Classroom Audio ZIP."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import zipfile


MP3_PATTERN = re.compile(r"`(IC5_L0_[^`\r\n]+\.mp3)`")
REF_PATTERN = re.compile(r"^##\s+`?(IC5-L0-(?:U\d{2}|PC\d{2}-\d{2})-A\d{2})`?\s*$", re.M)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_zip", type=Path)
    parser.add_argument("cards_dir", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    card_files = sorted(args.cards_dir.glob("unit-*.md"))
    card_files.append(args.cards_dir / "progress-checks.md")

    with zipfile.ZipFile(args.audio_zip) as archive:
        expected = {
            entry.filename
            for entry in archive.infolist()
            if entry.filename.startswith("IC5_L0_")
            and entry.filename.lower().endswith(".mp3")
        }

    texts = [path.read_text(encoding="utf-8") for path in card_files]
    listed_items = [item for text in texts for item in MP3_PATTERN.findall(text)]
    listed = set(listed_items)
    refs = [item for text in texts for item in REF_PATTERN.findall(text)]

    errors: list[str] = []
    if missing := sorted(expected - listed):
        errors.append(f"Missing MP3 cards: {missing}")
    if extra := sorted(listed - expected):
        errors.append(f"Unknown MP3 cards: {extra}")
    duplicate_files = sorted(item for item, count in Counter(listed_items).items() if count != 1)
    if duplicate_files:
        errors.append(f"MP3 filenames not listed exactly once: {duplicate_files}")
    duplicate_refs = sorted(item for item, count in Counter(refs).items() if count != 1)
    if duplicate_refs:
        errors.append(f"Reference IDs not unique: {duplicate_refs}")
    if len(refs) != len(expected):
        errors.append(f"Reference count {len(refs)} does not match MP3 count {len(expected)}")

    joined = "\n".join(texts)
    for forbidden in ("asr_unverified", "not_processed", "audio_mode: substitute"):
        if forbidden in joined:
            errors.append(f"Forbidden unresolved marker in usable cards: {forbidden}")

    if errors:
        raise SystemExit("\n".join(errors))

    core = sum(" PC " not in name for name in expected)
    progress_checks = len(expected) - core
    print(
        f"OK: {len(expected)} MP3 cards ({core} core, {progress_checks} progress checks), "
        f"{len(refs)} unique references"
    )


if __name__ == "__main__":
    main()
