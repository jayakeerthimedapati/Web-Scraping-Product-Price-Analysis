# Web Scraping and Product Price Analysis System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Chromium-green)
![Google Colab](https://img.shields.io/badge/Google-Colab-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A Data Analytics Engineering (DAE) project that scrapes product data from the Scraping Sandbox Data Table with
Playwright, analyses product prices with Pandas, visualises them with Matplotlib and Plotly, and presents them in an
interactive Google Colab dashboard.

> **Project status:** repository prepared for submission. The analysis notebook was checked on synthetic test data only.
> The scraping notebook and the dashboard have **not been executed yet**, and all numerical findings below are
> **pending** until you run the notebooks on the real data. See [`docs/code_review_notes.md`](docs/code_review_notes.md).

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Problem Definition](#2-problem-definition)
3. [Proposed Solution](#3-proposed-solution)
4. [Project Objectives](#4-project-objectives)
5. [Data Source](#5-data-source)
6. [Dataset Description](#6-dataset-description)
7. [Technologies Used](#7-technologies-used)
8. [System Workflow](#8-system-workflow)
9. [Repository Structure](#9-repository-structure)
10. [Web Scraping Methodology](#10-web-scraping-methodology)
11. [Data Cleaning Methodology](#11-data-cleaning-methodology)
12. [Product Price Analysis Features](#12-product-price-analysis-features)
13. [Visualizations](#13-visualizations)
14. [Dashboard Features](#14-dashboard-features)
15. [Installation Instructions](#15-installation-instructions)
16. [Google Colab Execution Instructions](#16-google-colab-execution-instructions)
17. [Expected Output Files](#17-expected-output-files)
18. [Results and Findings](#18-results-and-findings)
19. [Limitations](#19-limitations)
20. [Future Enhancements](#20-future-enhancements)
21. [Team Members](#21-team-members)
22. [Conclusion](#22-conclusion)

## 1. Project Overview
This project builds a small end-to-end data pipeline: it collects about 500 product records from a practice website,
cleans them, analyses price patterns, and shows the results in charts and an interactive dashboard.

## 2. Problem Definition
Product data on websites is spread over many pages. Collecting it by hand is slow and error-prone, and comparing
prices across categories and vendors from a plain table is difficult.

## 3. Proposed Solution
Automate collection with a browser-controlled scraper (Playwright), store the data in a Pandas DataFrame, clean and
validate it, run price analysis, export results, and provide a dashboard with filters.

## 4. Project Objectives
* Scrape product data across 20 pages automatically.
* Validate and clean the data (missing values, duplicates, numeric conversion).
* Calculate price statistics and compare prices by category and vendor.
* Classify products into Low / Medium / High price ranges.
* Study the price-rating relationship.
* Export results (CSV) and charts (PNG).
* Provide an interactive Plotly + ipywidgets dashboard in Google Colab.

## 5. Data Source
| Item | Detail |
|------|--------|
| Website | Scraping Sandbox - Data Table |
| URL | <https://scrapingsandbox.com/data-table> |
| Type | Practice website designed for web-scraping exercises |
| Scope | One website only (no other e-commerce sites are scraped) |

## 6. Dataset Description
About 500 product records (expected; confirm after running the scraper).

| Column | Description | Cleaned type |
|--------|-------------|--------------|
| ID | Product identifier | text / number |
| Image | Product image URL | text |
| Product_Name | Name of the product | text |
| Vendor | Seller / brand | text |
| Category | Product category | text |
| Price | Product price | numeric |
| Rating | Customer rating | numeric |
| Stock | Stock information | as scraped |
| SKU | Stock keeping unit | text |
| Variants | Number of variants | numeric |

The dataset itself is not stored in Git. See [`data/README.md`](data/README.md).

## 7. Technologies Used
| Technology | Purpose |
|-----------|---------|
| Python | Main language |
| Playwright (Chromium) | Browser automation for scraping |
| Pandas | Data handling, cleaning and analysis |
| Matplotlib | Static charts saved as PNG |
| Plotly | Interactive dashboard charts |
| ipywidgets | Dashboard filters and buttons |
| openpyxl | Excel export |
| Google Colab | Development and execution environment |
| CSV / Excel | Data and result formats |

## 8. System Workflow
```
Website -> Playwright Scraping -> Pandas DataFrame -> Data Validation -> Data Cleaning
        -> Price Analysis -> Visualizations -> Exported Results -> Interactive Dashboard
```
Details: [`docs/methodology.md`](docs/methodology.md).

## 9. Repository Structure
```
Web-Scraping-Product-Price-Analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── scraping/
│   └── web_scraping.ipynb                      # Notebook 1
├── analysis/
│   └── product_price_analysis.ipynb            # Notebook 2
├── dashboard/
│   └── Product_Price_Analysis_Dashboard.ipynb  # Notebook 3
├── data/
│   └── README.md                               # generated dataset is NOT committed
├── results/                                    # 4 CSV files (after running Notebook 2)
├── visualizations/                             # 5 PNG charts (after running Notebook 2)
└── docs/
    ├── project_overview.md
    ├── methodology.md
    ├── installation_and_usage.md
    ├── github_upload_guide.md
    └── code_review_notes.md
```

## 10. Web Scraping Methodology
1. Playwright launches headless Chromium and opens the Data Table page.
2. For each of the 20 pages, every table row and cell is read.
3. The Image cell is stored as an image URL.
4. The notebook clicks to the next page and waits until the table content changes.
5. All records are combined into a DataFrame with the 10 columns above.

## 11. Data Cleaning Methodology
* Count missing values and duplicate rows.
* Remove exact duplicates.
* Convert `Price`, `Rating` and `Variants` to numbers; invalid values become `NaN` safely.
* Save `scraped_product_data.csv` and `scraped_product_data.xlsx`.

## 12. Product Price Analysis Features
Average / minimum / maximum / median price - descriptive statistics - cheapest and most expensive product -
average price by category (with min/max/average table) - ten most expensive and ten cheapest products -
Low / Medium / High price ranges with `pd.cut()` - price-rating correlation - average price by vendor -
final summary table - CSV export.

## 13. Visualizations
Generated by `analysis/product_price_analysis.ipynb` into `visualizations/`.

| Chart | File | Type |
|-------|------|------|
| Product Price Distribution | `price_distribution.png` | Histogram |
| Average Price by Category | `average_price_by_category.png` | Bar chart |
| Products by Price Range | `products_by_price_range.png` | Bar chart |
| Price vs Rating | `price_vs_rating.png` | Scatter plot |
| Average Price by Vendor | `average_price_by_vendor.png` | Bar chart |

> The chart images do not exist yet. After you run Notebook 2 and place the PNG files in `visualizations/`,
> delete the first line (`<!-- Remove ...`) and the last line (`End of block -->`) of the commented block below to show them here.

<!-- Remove this line after adding the real PNG files.
![Price Distribution](visualizations/price_distribution.png)
![Average Price by Category](visualizations/average_price_by_category.png)
![Products by Price Range](visualizations/products_by_price_range.png)
![Price vs Rating](visualizations/price_vs_rating.png)
![Average Price by Vendor](visualizations/average_price_by_vendor.png)
End of block -->

## 14. Dashboard Features
* KPI cards: total products, average, minimum, maximum and median price.
* Price distribution, average price by category, products by price range, price vs rating, average price by vendor.
* Ten most expensive and ten cheapest products.
* Complete (filtered) product table.
* Filters: category, vendor, price range.
* Downloads: filtered product data and summary (CSV).

Built with Plotly and ipywidgets for Google Colab. *Status: not yet executed or tested.*

## 15. Installation Instructions
**Google Colab (recommended):** nothing to install; the notebooks install what they need.

**Local computer (optional):**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis.git
cd Web-Scraping-Product-Price-Analysis
pip install -r requirements.txt
playwright install chromium          # browser download - NOT included in pip install
# On Linux / Colab also: playwright install-deps chromium
```

## 16. Google Colab Execution Instructions
Run the notebooks in this order. Replace `YOUR_GITHUB_USERNAME` in the links.

| Order | Notebook | Open in Colab |
|-------|----------|---------------|
| 1 | Web scraping | [Open](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis/blob/main/scraping/web_scraping.ipynb) |
| 2 | Price analysis | [Open](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis/blob/main/analysis/product_price_analysis.ipynb) |
| 3 | Dashboard | [Open](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis/blob/main/dashboard/Product_Price_Analysis_Dashboard.ipynb) |

Full step-by-step guide: [`docs/installation_and_usage.md`](docs/installation_and_usage.md).

## 17. Expected Output Files
| Location | File |
|----------|------|
| `data/` (not in Git) | `scraped_product_data.csv`, `scraped_product_data.xlsx` |
| `results/` | `product_price_analysis_summary.csv`, `category_price_analysis.csv`, `top_10_expensive_products.csv`, `top_10_cheapest_products.csv` |
| `visualizations/` | `price_distribution.png`, `average_price_by_category.png`, `products_by_price_range.png`, `price_vs_rating.png`, `average_price_by_vendor.png` |

## 18. Results and Findings
**Pending.** No numerical result is reported here because the notebooks have not been run on the real dataset.
After running Notebook 2, copy the real values from `results/product_price_analysis_summary.csv`.

| Metric | Value |
|--------|-------|
| Total products analysed | *pending* |
| Average price | *pending* |
| Minimum price | *pending* |
| Maximum price | *pending* |
| Median price | *pending* |
| Cheapest product | *pending* |
| Most expensive product | *pending* |
| Price-rating correlation | *pending* |
| Category with highest average price | *pending* |
| Vendor with highest average price | *pending* |

## 19. Limitations
* Uses a single practice website, so findings do not describe real markets.
* A static snapshot: no price history or live updates.
* The scraper depends on the page layout; a website redesign can break it.
* Price ranges use equal-width bins, which are sensitive to extreme prices.
* Correlation shows association, not cause.
* No discount analysis, because the dataset has no discount field.

## 20. Future Enhancements
* Scheduled scraping to track price changes over time.
* Additional statistics (outlier detection, vendor ranking).
* Optional Streamlit version of the dashboard (kept separate from the Colab notebook).
* Automated tests for the cleaning functions.

## 21. Team Members
| Name | Roll Number | Role |
|------|-------------|------|
| [Name 1] | [Roll No.] | [Role] |
| [Name 2] | [Roll No.] | [Role] |
| [Name 3] | [Roll No.] | [Role] |

**Guide / Faculty:** [Faculty Name]  
**Institution:** [College Name]

## 22. Conclusion
The project demonstrates a complete data workflow - scraping, cleaning, analysis, visualisation and an interactive
dashboard - using Python tools. Final conclusions should be written after the real results are generated.

## License
Released under the MIT License - see [`LICENSE`](LICENSE).
