# Word-count helper for Perfect rewrite batch (ch 2,5,8,14,26,37,41,47)
# Run: python _wc_batch_edit.py
from pathlib import Path
import re

dir = Path(__file__).parent / "chapters"
nums = [2, 5, 8, 14, 26, 37, 41, 47]
total = 0
for n in nums:
    matches = list(dir.glob(f"ch-{n:02d}-*.md"))
    if not matches:
        print(f"MISSING ch-{n:02d}")
        continue
    f = matches[0]
    text = f.read_text(encoding="utf-8")
    body = "\n".join(ln for ln in text.splitlines() if not ln.startswith("#"))
    words = re.findall(r"[A-Za-z0-9']+", body)
    nwords = len(words)
    total += nwords
    title = next((ln[3:].strip() for ln in text.splitlines() if ln.startswith("## ")), "")
    flag = "OK" if 750 <= nwords <= 950 else ("SHORT" if nwords < 750 else "LONG")
    print(f"ch-{n:02d}: {nwords:4d}  [{flag:5}]  {title}")
print(f"TOTAL body words: {total}")
