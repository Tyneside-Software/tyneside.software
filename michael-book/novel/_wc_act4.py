"""Word counts for novel chapters 66-99. Writes wordcounts-66-99.txt"""
from pathlib import Path
import re

root = Path(__file__).parent
dir_path = root / "chapters"
rows = []
for p in sorted(dir_path.glob("ch-*.md")):
    m = re.match(r"ch-(\d+)-", p.name)
    if not m:
        continue
    n = int(m.group(1))
    if n < 66 or n > 99:
        continue
    text = p.read_text(encoding="utf-8")
    # Body words: exclude pure header lines
    body_lines = []
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        body_lines.append(line)
    body = "\n".join(body_lines)
    words = len(body.split())
    rows.append((n, p.name, words))

lines = []
for n, name, words in rows:
    flag = "OK" if 650 <= words <= 850 else ("SHORT" if words < 650 else "LONG")
    lines.append(f"{n:3d}  {words:4d}  {flag:5s}  {name}")

ok = sum(1 for *_, w in rows if 650 <= w <= 850)
short = sum(1 for *_, w in rows if w < 650)
long_ = sum(1 for *_, w in rows if w > 850)
lines.append("---")
lines.append(f"total: {len(rows)}  in_range_650_850: {ok}  short: {short}  long: {long_}")
out = root / "wordcounts-66-99.txt"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
