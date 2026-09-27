"""Reset every Markdown note's YAML ``read`` property to ``false``."""

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = ROOT / "AWS-DOP-C02-Notebook"
FRONT_MATTER = re.compile(r"\A---(?:\r\n|\n)(.*?)(?:\r\n|\n)---(?=\r?\n|\Z)", re.DOTALL)
READ_PROPERTY = re.compile(r"^(read[ \t]*:[ \t]*)(true|false)([ \t]*)$", re.MULTILINE)


def updated_note(path: Path) -> tuple[bytes, bool]:
    """Return validated note bytes with the read flag reset and whether it changed."""
    original = path.read_bytes()
    has_bom = original.startswith(b"\xef\xbb\xbf")

    try:
        text = original.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("is not valid UTF-8") from exc

    front_matter = FRONT_MATTER.match(text)
    if front_matter is None:
        raise ValueError("does not start with YAML front matter")

    properties = list(READ_PROPERTY.finditer(front_matter.group(1)))
    if len(properties) != 1:
        raise ValueError(f"expected exactly one Boolean read property, found {len(properties)}")

    prop = properties[0]
    if prop.group(2) == "false":
        return original, False

    start = front_matter.start(1) + prop.start(2)
    end = front_matter.start(1) + prop.end(2)
    updated = text[:start] + "false" + text[end:]
    encoded = updated.encode("utf-8")
    if has_bom:
        encoded = b"\xef\xbb\xbf" + encoded
    return encoded, True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Set the YAML read property to false in every Markdown note in the vault."
    )
    parser.add_argument(
        "--vault",
        type=Path,
        default=DEFAULT_VAULT,
        help=f"vault directory (default: {DEFAULT_VAULT})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and report what would change without modifying any files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault = args.vault.resolve()
    if not vault.is_dir():
        print(f"error: vault directory does not exist: {vault}", file=sys.stderr)
        return 2

    notes = sorted(vault.rglob("*.md"))
    if not notes:
        print(f"error: no Markdown notes found in: {vault}", file=sys.stderr)
        return 2

    pending: list[tuple[Path, bytes]] = []
    errors: list[str] = []
    for path in notes:
        try:
            content, changed = updated_note(path)
            if changed:
                pending.append((path, content))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(vault)}: {exc}")

    if errors:
        print("No files were changed because validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    if not args.dry_run:
        for path, content in pending:
            path.write_bytes(content)

    action = "Would reset" if args.dry_run else "Reset"
    print(
        f"{action} {len(pending)} of {len(notes)} notes; "
        f"{len(notes) - len(pending)} already had read: false."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
