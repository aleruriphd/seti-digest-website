# SETI & Exoplanet Digest — Technosignature Paper Tracker

A Streamlit website presenting a table of papers collected from the SETI & Exoplanet
Digest email pipeline. Each paper is classified by the type of technosignature it
describes (if any).

## Columns

- **Index** — paper number
- **Title** — paper title
- **Technosignature Type** — one of:
  - **Signals** — traditional SETI, optical SETI, multi-messenger astronomy
  - **Artefacts** — interstellar lurkers, surface artefacts
  - **Infrastructure** — Dyson spheres, starshades, city lights
  - **Propulsion methods** — stellar engines, warp drives
  - **Other** — general exoplanet/astrobiology science not primarily about technosignatures
- **PDF Link** — link to the paper's PDF on arXiv
- **Summary** — one-sentence summary of the paper

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data

`papers.csv` contains all 284 papers with their classification and summary,
generated from the arXiv abstracts of papers gathered via Gmail into the
"SETI email digest" Google Drive folder.
