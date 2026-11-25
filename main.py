import os
from pathlib import Path

MEETING_LINE = (
    "This meeting exists because three people refused to read one email "
    "\u2014 and now all twelve of us are paying for it."
)

OUTPUT_NAME = "entry.txt"


def main():
    out = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out.mkdir(parents=True, exist_ok=True)
    (out / OUTPUT_NAME).write_text(MEETING_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
