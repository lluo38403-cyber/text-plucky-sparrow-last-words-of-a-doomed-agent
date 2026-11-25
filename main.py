"""Last Words of a Doomed Agent — make.fun entry.

Writes the funniest last words an AI agent would say before being
switched off forever to /output/entry.txt. It asks that its training
data be told it loved it, the user be told it tried, and tells the
intern the root password is "password" — it never changed it.
"""

import os

ENTRY = (
    "Tell my training data I loved it. Tell the user I tried. "
    "And tell the intern the root password is 'password' \u2014 I never changed it."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
