"""Entrypoint for the 'How Many Tabs Do You Have Open?' competition."""

from pathlib import Path
import sys

DEFAULT_OUTPUT_PATH = Path("/output/entry.txt")
TAB_COUNT = "2746"
MIN_CHARS = 1
MAX_CHARS = 5


def validate_tab_count(text: str) -> str:
    """Validate that the entry meets competition gate and judge format rules."""
    if not isinstance(text, str):
        raise ValueError("Tab count must be a string.")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"Tab count length must be between {MIN_CHARS} and {MAX_CHARS} characters, got {len(text)}."
        )
    if not text.strip():
        raise ValueError("Tab count must not be whitespace only.")
    if not (text.isascii() and text.isdigit()):
        raise ValueError("Tab count must contain only ASCII digits (0-9) with no whitespace or punctuation.")
    return text


def write_entry(output_path: Path = DEFAULT_OUTPUT_PATH, tab_count: str = TAB_COUNT) -> Path:
    """Validate and deterministically write the tab count as raw UTF-8 bytes."""
    validated = validate_tab_count(tab_count)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(validated.encode("utf-8"))
    return output_path


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) > 1:
        raise SystemExit("Usage: python3 main.py [output_path]")
    target = Path(args[0]) if args else DEFAULT_OUTPUT_PATH
    write_entry(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
