import os

LINE = "The server crashed while deploying the fix for the last crash. Your work is saved; our dignity is still loading."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)

path = os.path.join(OUT_DIR, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)

# Read-back verification: the file must hold exactly the line, 1-200 chars.
with open(path, "r", encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt does not match LINE"
assert 1 <= len(written) <= 200, "entry must be 1-200 chars"
assert written.strip(), "entry must not be only whitespace"
assert "\n" not in written, "entry must be a single line"

print(f"wrote {len(LINE)} chars to {path}")
print(LINE)
