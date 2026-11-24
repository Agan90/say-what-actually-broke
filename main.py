import os
import sys

LINE = "The server crashed while deploying the fix for the last crash. Your work is saved; our dignity is still loading."

MAX_CHARS = 200


def validate(line):
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not match LINE"
    print(f"wrote {len(line)} chars to {path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
