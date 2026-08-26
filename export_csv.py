import csv
from build_data import DATA

manifest = []
with open('/tmp/manifest.tsv') as f:
    next(f)  # header
    for line in f:
        parts = line.rstrip('\n').split('\t')
        if len(parts) >= 2:
            aid, title = parts[0], parts[1]
            manifest.append((aid, title))

rows = []
missing = []
for i, (aid, title) in enumerate(manifest, start=1):
    if aid not in DATA:
        missing.append(aid)
        continue
    category, summary = DATA[aid]
    pdf_link = f"https://arxiv.org/pdf/{aid}"
    rows.append({
        "Index": i,
        "Title": title,
        "Technosignature Type": category,
        "PDF Link": pdf_link,
        "Summary": summary,
    })

print(f"Total rows: {len(rows)}, missing: {len(missing)}")
if missing:
    print(missing)

with open('papers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Index", "Title", "Technosignature Type", "PDF Link", "Summary"])
    writer.writeheader()
    writer.writerows(rows)

print("Wrote papers.csv")

# category distribution
from collections import Counter
c = Counter(r["Technosignature Type"] for r in rows)
print(c)
