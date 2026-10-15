"""Check Markdown links to files and directories inside this repository."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
errors = []
checked = 0

for document in root.rglob("*.md"):
    if ".git" in document.parts or "_plantillas" in document.parts:
        continue
    content = document.read_text(encoding="utf-8-sig")
    content = re.sub(r"^```.*?^```", "", content, flags=re.MULTILINE | re.DOTALL)
    for target in pattern.findall(content):
        target = target.strip("<>")
        if not target or target.startswith(("#", "mailto:", "data:")):
            continue
        if urlsplit(target).scheme or target.startswith("//"):
            continue
        local = unquote(target.split("#", 1)[0].split("?", 1)[0])
        path = (document.parent / local).resolve()
        checked += 1
        if not path.is_relative_to(root) or not path.exists():
            errors.append(f"{document.relative_to(root)}: {target}")

for error in errors:
    print(f"BROKEN: {error}")
print(f"Checked {checked} local links; {len(errors)} broken")
sys.exit(1 if errors else 0)
