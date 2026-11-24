"""Write one debugging haiku, three lines, 5-7-5, to /output/entry.txt."""
import os

HAIKU = (
    "Cursor blinks at three\n"
    "log silent, the test still red\n"
    "it was a typo\n"
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = HAIKU
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 3, "haiku must be three lines"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
