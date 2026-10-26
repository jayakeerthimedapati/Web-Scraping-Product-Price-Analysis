# Code Review Notes and Open Items

## Important: how the notebooks were prepared
No original notebooks or dataset files were available when this repository was prepared. The three notebooks were
**written from the project description**, not copied from the original code. They follow the described workflow,
file names and column names.

## What was and was not verified
| Item | Status |
|------|--------|
| Analysis notebook code | Executed end-to-end on a **synthetic test CSV** (kept outside the repository). It ran without errors and created all CSVs and PNGs. It has **not** been run on the real scraped data. |
| Dashboard helper functions (filtering, summary) | Run on the same synthetic CSV. The Plotly / ipywidgets interface was **not** executed, so the dashboard is **untested**. |
| Scraping notebook | **Not executed.** There was no internet access to the website. Selectors, column order and the "Next" button logic are assumptions. |

## Things you should check
1. **Scraper selectors:** confirm `ROW_SELECTOR`, the 10-cell column order, and the pagination control on the live site. If you already have working scraping code, paste its logic into Section 3 of `web_scraping.ipynb`.
2. **Price-range bins:** `pd.cut(bins=3)` is equal-width. Replace with your own bin edges if your original used fixed ranges.
3. **Merge your own logic:** if your original analysis differs from these notebooks, keep your version and only reuse the file paths (`data/`, `results/`, `visualizations/`).
4. **Run everything in Colab** and fix any error before describing the dashboard as working.

## Design decisions
* Invalid numbers become `NaN` (via `pd.to_numeric(errors="coerce")`) instead of crashing; rows with no valid price are excluded from price analysis.
* All notebooks locate the project root automatically, so the same CSV path works for all three.
* `dashboard_exports/` is Git-ignored so downloads do not pollute the repository.
* No discount analysis and no multi-site scraping, as the dataset and scope do not include them.
