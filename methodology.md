# Methodology

Workflow:

**Website -> Playwright Scraping -> Pandas DataFrame -> Data Validation -> Data Cleaning -> Price Analysis -> Visualizations -> Exported Results -> Interactive Dashboard**

## 1. Website
The source is the Data Table page of Scraping Sandbox (<https://scrapingsandbox.com/data-table>), a website designed
for practising scraping. The data is shown in a table split across 20 pages.

## 2. Playwright scraping
Playwright controls a real Chromium browser from Python. The notebook opens the page, reads every table row and its
cells, clicks to the next page, and repeats until all 20 pages are done. Because the table loads in a browser, a
browser-based tool is more reliable than downloading raw HTML.

## 3. Pandas DataFrame
All rows are collected in a Python list and turned into a DataFrame with 10 columns:
`ID, Image, Product_Name, Vendor, Category, Price, Rating, Stock, SKU, Variants`.

## 4. Data validation
Before changing anything the notebook counts missing values and duplicate rows and checks that the total record
count is close to the expected 500.

## 5. Data cleaning
* Exact duplicate rows are removed.
* `Price`, `Rating` and `Variants` are converted to numbers (symbols such as `$` and `,` are stripped first).
* Values that cannot be converted become `NaN` instead of stopping the program; rows without a valid price are left out of price calculations.
* The result is saved as CSV and Excel.

## 6. Price analysis
Average, minimum, maximum and median price; descriptive statistics; cheapest and most expensive product; price by
category and by vendor; ten most expensive and ten cheapest products; Low/Medium/High grouping with `pd.cut()`;
price-rating correlation (Pearson, via `Series.corr()`).

## 7. Visualizations
Five Matplotlib charts are saved as PNG files: price histogram, average price by category, products by price range,
price vs rating scatter plot, average price by vendor.

## 8. Exported results
Summary, category analysis, top-10 expensive and top-10 cheapest tables are saved as CSV in `results/`.

## 9. Interactive dashboard
The dashboard reads the same CSV and uses Plotly charts and ipywidgets controls (category, vendor and price filters).
Filtered data and the summary can be downloaded as CSV.

## Assumptions to be aware of
* Price ranges use equal-width bins (`pd.cut(bins=3)`); change this if your original code used fixed boundaries.
* Correlation shows a linear relationship only and does not prove cause and effect.
