# Word-count helper for ch 41-64 — run: python _wc_41_64.py
from pathlib import Path
import re

dir = Path(__file__).parent / "chapters"
total = 0
rows = []
for n in range(41, 65):
    matches = list(dir.glob(f"ch-{n:02d}-*.md"))
    if not matches:
        print(f"MISSING ch-{n:02d}")
        continue
    f = matches[0]
    text = f.read_text(encoding="utf-8")
    body = "\n".join(
        ln for ln in text.splitlines()
        if not ln.startswith("#")
    )
    words = re.findall(r"[A-Za-z0-9']+", body)
    nwords = len(words)
    total += nwords
    title = next((ln[3:].strip() for ln in text.splitlines() if ln.startswith("## ")), "")
    flag = "OK" if 650 <= nwords <= 850 else ("SHORT" if nwords < 650 else "LONG")
    rows.append((n, nwords, title, flag, f.name))
    print(f"ch-{n:02d}: {nwords:4d}  [{flag:5}]  {title}  ({f.name})")
print(f"TOTAL body words: {total}")
for n, nwords, title, flag, name in rows:
    if flag != "OK":
        print(f"  !! {flag}: ch-{n:02d} {nwords}w")
