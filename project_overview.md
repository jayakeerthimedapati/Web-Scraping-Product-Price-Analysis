# Project Overview

## Purpose
This Data Analytics Engineering (DAE) project collects product data from a practice website, analyses product prices
with Python, and presents the results in charts and an interactive dashboard. It shows a complete beginner-level
data pipeline: **collect -> clean -> analyse -> visualise -> present**.

## Problem definition
Product details on websites are shown page by page. Copying hundreds of rows by hand is slow and error-prone, and it
is hard to compare prices across categories and vendors by just looking at a table.

## Objectives
1. Automatically collect product data from the Scraping Sandbox Data Table across 20 pages.
2. Validate and clean the data (missing values, duplicates, numeric conversion).
3. Calculate price statistics and compare prices by category and vendor.
4. Group products into Low / Medium / High price ranges.
5. Study the relationship between price and rating.
6. Export results as CSV files and charts as images.
7. Provide an interactive Google Colab dashboard with filters.

## Scope
| In scope | Out of scope |
|----------|--------------|
| One source: <https://scrapingsandbox.com/data-table> | Scraping multiple e-commerce websites |
| About 500 products, 20 pages | Live / real-time price tracking |
| Price, rating, category and vendor analysis | Discount analysis (the dataset has no discount field) |
| Google Colab notebooks (Plotly + ipywidgets) | Production deployment / web hosting |

## Expected outcomes
* `data/scraped_product_data.csv` and `.xlsx` (generated, not committed).
* Four result CSV files in `results/`.
* Five chart images in `visualizations/`.
* A working interactive dashboard notebook (after you run and test it).

## Notebook run order
`scraping/web_scraping.ipynb` -> `analysis/product_price_analysis.ipynb` -> `dashboard/Product_Price_Analysis_Dashboard.ipynb`
