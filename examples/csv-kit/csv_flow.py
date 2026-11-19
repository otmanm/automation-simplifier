"""Small synthetic source checkout for a skill evaluation."""

import argparse
import csv
from pathlib import Path


def import_rows(source: Path) -> list[dict[str, str]]:
    with source.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["id", "name", "units"]:
            raise ValueError("Expected id,name,units")
        return list(reader)


def review_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    reviewed = {}
    for row in rows:
        key = row["id"]
        if key in reviewed:
            answer = input(f"Repeated {key}: keep the earlier row? [y/n] ")
            if answer.strip().lower() == "y":
                continue
        reviewed[key] = row
    return list(reviewed.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    rows = review_rows(import_rows(args.source))
    with args.destination.open("x", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["id", "name", "units"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
