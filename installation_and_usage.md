# Installation and Usage (Google Colab)

You do not need to install anything on your computer. All you need is a Google account and a browser.

## Step 1 - Put the project on GitHub
Follow `docs/github_upload_guide.md`. (If you are only testing, you can also upload the three notebook files to Colab directly.)

## Step 2 - Open a notebook in Google Colab
1. Go to <https://colab.research.google.com>.
2. Choose **File -> Open notebook -> GitHub** tab.
3. Paste your repository URL, then choose `scraping/web_scraping.ipynb`.

## Step 3 - Run the scraping notebook (Notebook 1)
1. Click **Runtime -> Run all**, or run the cells one by one with the play button.
2. The first code cell installs Playwright and the Chromium browser. This takes about a minute.
3. Wait until all 20 pages have been printed.
4. The notebook creates `data/scraped_product_data.csv` and `.xlsx` and downloads them to your computer.

> Colab's disk is temporary. Keep the downloaded files.

## Step 4 - Run the analysis notebook (Notebook 2)
1. Open `analysis/product_price_analysis.ipynb`.
2. If you are in a new Colab session, the notebook will ask you to **upload** `scraped_product_data.csv`.
3. Run all cells. Five charts and four CSV files are created and downloaded as two zip files.
4. Unzip them and place the files into the repository's `results/` and `visualizations/` folders.

## Step 5 - Use the dashboard (Notebook 3)
1. Open `dashboard/Product_Price_Analysis_Dashboard.ipynb`.
2. Upload `scraped_product_data.csv` when asked.
3. Run all cells. Use the Category, Vendor and Price controls, then press **Apply filters**.
4. Use the tabs: Overview, Charts, Top 10, Dataset. Use the download buttons to save filtered data or the summary.

## Running locally (optional)
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis.git
cd Web-Scraping-Product-Price-Analysis
python -m venv venv
venv\Scripts\activate          # Windows   (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
playwright install chromium    # downloads the browser (separate from pip)
jupyter notebook
```
Local runs save files into the repository's `data/`, `results/` and `visualizations/` folders automatically.
In the scraping notebook, remove the `!` lines in the install cell if you already installed everything this way.

## Troubleshooting
| Problem | What to do |
|---------|-----------|
| `Executable doesn't exist` error | Run `playwright install chromium` (and `playwright install-deps chromium` on Colab). |
| Scraper stops on a page / wrong record count | The page selectors or the Next button logic may differ from the live site; inspect the page and adjust Section 3 of the scraping notebook. |
| `scraped_product_data.csv not found` | Run Notebook 1 first or upload the CSV when asked. |
| Widgets do not show in Colab | Re-run the setup cell of the dashboard (it enables the custom widget manager). |
