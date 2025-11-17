#!/usr/bin/env python3
"""Generate the regression testing issue template from the checklist CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


FRONT_MATTER = (
    "---\n"
    "name: Testing checklist template\n"
    "about: Use this template to create an issue for regression testing\n"
    "---"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        default="regression-testing-checklist.csv",
        type=Path,
        help="path to regression testing checklist CSV (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=Path(".github/ISSUE_TEMPLATE/issue_template.md"),
        type=Path,
        help="output path for generated template (default: %(default)s)",
    )
    return parser.parse_args()


def iter_rows(csv_path: Path) -> Iterable[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield {key: (value or "") for key, value in row.items()}


def build_template(rows: Iterable[dict[str, str]]) -> str:
    lines: list[str] = []
    lines.extend((FRONT_MATTER, ""))

    current_area: str | None = None
    meta_fields = (
        ("Severity", "Severity"),
        ("Current coverage in AMAUAT", "Current Coverage in AMAUAT"),
        ("AMAUAT tests", "AMAUAT test"),
        ("External tools", "External tools"),
    )

    for row in rows:
        area = row["Functional Area"].strip()
        if area and area != current_area:
            lines.append(f"## {area}")
            lines.append("")
            current_area = area

        identifier = row["ID"].strip()
        if not identifier:
            raise ValueError(f"Missing ID for row in functional area: {area}")
        lines.append(f"### {identifier}")
        lines.append("")

        for label, key in meta_fields:
            value = row[key].strip()
            if value:
                lines.append(f"**{label}**: {value}")
                lines.append("")

        feature = row["Feature"].strip()
        then = row["Then"].strip()

        if feature:
            lines.append(feature)
        if then:
            lines.append(then)
        else:
            lines.append("")

        lines.append("")

    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    rows = list(iter_rows(args.csv))
    template = build_template(rows)

    output_path: Path = args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template, encoding="utf-8")


if __name__ == "__main__":
    main()
