"""Convert MyST/Jupyter Book syntax to Quarto syntax.

Handles both .qmd (markdown) files and .ipynb (notebook) files.
Idempotent: running twice on an already-converted file is a no-op.

Usage:
    python scripts/jb_to_quarto.py --dry-run *.qmd
    python scripts/jb_to_quarto.py --apply *.qmd *.ipynb
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

# --- Title → callout-type mapping for {admonition} ---
TITLE_MAP = {
    "exercise": "tip",
    "exercises": "tip",
    "tip": "tip",
    "tips": "tip",
    "important": "important",
    "warning": "warning",
    "caution": "caution",
    "note": "note",
    "hint": "tip",
}


def convert_text(text: str) -> str:
    """Apply all MyST→Quarto transformations to a block of text."""
    lines = text.split("\n")
    out_lines = []
    i = 0

    # Track open callout fences for proper closing
    fence_stack = []  # list of (backtick_count, is_callout)

    while i < len(lines):
        line = lines[i]

        # --- Pass A: Label definitions ---
        # Pattern: (label-name)= on its own line, followed by a heading
        label_match = re.match(r"^\(([a-zA-Z0-9_-]+)\)=\s*$", line)
        if label_match and i + 1 < len(lines):
            label = label_match.group(1)
            next_line = lines[i + 1]
            heading_match = re.match(r"^(#{1,6})\s+(.+)$", next_line)
            if heading_match:
                hashes = heading_match.group(1)
                title = heading_match.group(2)
                # Remove any existing {#...} from title
                title = re.sub(r"\s*\{#[^}]+\}\s*$", "", title)
                out_lines.append(f"{hashes} {title} {{#sec-{label}}}")
                i += 2
                continue
            # Label not followed by heading — emit as-is (shouldn't happen often)

        # --- Pass B: Fence-aware callout conversion ---
        # Match opening fences: ```{note}, ````{admonition} Title, etc.
        fence_open = re.match(
            r"^(`{3,})\{(note|tip|warning|caution|important|exercise|solution)\}\s*(.*)$",
            line,
        )
        admonition_open = re.match(r"^(`{3,})\{admonition\}\s*(.+)$", line)

        if fence_open:
            backticks = fence_open.group(1)
            directive = fence_open.group(2)
            extra = fence_open.group(3).strip()

            if directive == "solution":
                callout_type = "note"
                title_attr = ' title="Solution" collapse="true"'
            elif directive == "exercise":
                callout_type = "tip"
                title_attr = ' title="Exercise"'
            else:
                callout_type = directive
                title_attr = ""

            if extra:
                title_attr = f' title="{extra}"'

            out_lines.append(f"::: {{.callout-{callout_type}{title_attr}}}")
            fence_stack.append((len(backticks), True))
            i += 1
            continue

        elif admonition_open:
            backticks = admonition_open.group(1)
            title = admonition_open.group(2).strip()
            callout_type = TITLE_MAP.get(title.lower(), "note")
            out_lines.append(f'::: {{.callout-{callout_type} title="{title}"}}')
            fence_stack.append((len(backticks), True))
            i += 1
            continue

        # Match code-cell fences (MyST executable cells in .md files)
        code_cell_match = re.match(r"^(`{3,})\{code-cell\}(?: ipython3)?\s*$", line)
        if code_cell_match:
            backticks = code_cell_match.group(1)
            out_lines.append(f"{backticks}{{python}}")
            fence_stack.append((len(backticks), False))
            i += 1
            continue

        # Match closing fences
        close_fence = re.match(r"^(`{3,})\s*$", line)
        if close_fence and fence_stack:
            backtick_count = len(close_fence.group(1))
            # Check if this closes the most recent fence
            top_count, is_callout = fence_stack[-1]
            if backtick_count >= top_count:
                fence_stack.pop()
                if is_callout:
                    out_lines.append(":::")
                    i += 1
                    continue
                # For code-cell→python fences, keep the closing backticks
                out_lines.append(line)
                i += 1
                continue

        # --- Pass A continued: Inline substitutions ---
        converted = line

        # Citations: {cite:t}`key` → @key
        converted = re.sub(r"\{cite:t\}`([^`]+)`", r"@\1", converted)
        # Citations: {cite:p}`key` → [@key]
        converted = re.sub(r"\{cite:p\}`([^`]+)`", r"[@\1]", converted)
        # Citations: {cite:ps}`key` → [@key]
        converted = re.sub(r"\{cite:ps\}`([^`]+)`", r"[@\1]", converted)

        # Cross-references: {ref}`text <label>` → [text](#sec-label)
        converted = re.sub(
            r"\{ref\}`([^<`]+?)\s*<([a-zA-Z0-9_-]+)>`",
            r"[\1](#sec-\2)",
            converted,
        )
        # Cross-references: {ref}`label` → @sec-label
        converted = re.sub(r"\{ref\}`([a-zA-Z0-9_-]+)`", r"@sec-\1", converted)

        out_lines.append(converted)
        i += 1

    return "\n".join(out_lines)


def process_qmd_file(path: Path, apply: bool) -> bool:
    """Process a .qmd file. Returns True if changes were made."""
    original = path.read_text(encoding="utf-8")
    converted = convert_text(original)

    if original == converted:
        return False

    if apply:
        path.write_text(converted, encoding="utf-8")
    else:
        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            converted.splitlines(keepends=True),
            fromfile=str(path),
            tofile=str(path) + " (converted)",
        )
        sys.stdout.writelines(diff)

    return True


def process_ipynb_file(path: Path, apply: bool) -> bool:
    """Process a .ipynb file by converting markdown cells. Returns True if changes were made."""
    original_bytes = path.read_bytes()
    nb = json.loads(original_bytes)

    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue

        source = cell.get("source", [])
        if not source:
            continue

        # Join source lines, convert, then split back
        text = "".join(source)
        converted = convert_text(text)

        if text != converted:
            changed = True
            # Preserve the list-of-strings format
            # Split on newlines but keep the newlines (except possibly the last)
            new_source = []
            conv_lines = converted.split("\n")
            for j, cline in enumerate(conv_lines):
                if j < len(conv_lines) - 1:
                    new_source.append(cline + "\n")
                else:
                    new_source.append(cline)
            cell["source"] = new_source

    if not changed:
        return False

    if apply:
        # Write with consistent formatting
        output = json.dumps(nb, ensure_ascii=False, indent=1)
        # Ensure file ends with newline
        if not output.endswith("\n"):
            output += "\n"
        path.write_text(output, encoding="utf-8")
    else:
        original_text = original_bytes.decode("utf-8")
        new_text = json.dumps(nb, ensure_ascii=False, indent=1) + "\n"
        diff = difflib.unified_diff(
            original_text.splitlines(keepends=True),
            new_text.splitlines(keepends=True),
            fromfile=str(path),
            tofile=str(path) + " (converted)",
        )
        sys.stdout.writelines(diff)

    return True


def main():
    parser = argparse.ArgumentParser(description="Convert MyST/JB syntax to Quarto")
    parser.add_argument("files", nargs="+", help="Files to process")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Show diffs only")
    group.add_argument("--apply", action="store_true", help="Apply changes in-place")
    args = parser.parse_args()

    total_changed = 0
    for filepath in args.files:
        path = Path(filepath)
        if not path.exists():
            print(f"WARNING: {path} does not exist, skipping", file=sys.stderr)
            continue

        if path.suffix == ".qmd":
            if process_qmd_file(path, args.apply):
                total_changed += 1
                print(f"{'Applied' if args.apply else 'Would change'}: {path}")
        elif path.suffix == ".ipynb":
            if process_ipynb_file(path, args.apply):
                total_changed += 1
                print(f"{'Applied' if args.apply else 'Would change'}: {path}")
        else:
            print(f"Skipping unsupported file type: {path}", file=sys.stderr)

    print(
        f"\nTotal files {'changed' if args.apply else 'that would change'}: {total_changed}"
    )


if __name__ == "__main__":
    main()
