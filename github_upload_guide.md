# GitHub Upload Guide (Beginner Friendly)

## Before you upload
1. Open `LICENSE` and replace `[YOUR FULL NAME]` with your name. (MIT is a simple, permissive licence that is common for student and portfolio projects. Choose another one if your college requires it.)
2. In `README.md`, replace `YOUR_GITHUB_USERNAME` and the team-member placeholders.
3. Run the notebooks and copy the generated files into `results/` and `visualizations/` (see `installation_and_usage.md`). Then follow the "after running" notes in the README.
4. Do **not** upload `data/scraped_product_data.csv/.xlsx` (they are ignored automatically when you use Git; with the website, simply do not add them).

## Method A - GitHub website (no commands)
1. Sign in at <https://github.com>.
2. Click **+** (top right) -> **New repository**.
3. Repository name: `Web-Scraping-Product-Price-Analysis`. Add a short description. Choose **Public** (for a portfolio). Do **not** tick "Add a README" (you already have one). Click **Create repository**.
4. Click **uploading an existing file**.
5. Unzip the project on your computer. Open the unzipped folder and select **everything inside it** (folders and files), then drag them into the browser window. Folders are kept.
6. Wait for the upload to finish. (Browser upload allows up to 100 files at once and 25 MB per file.)
7. In "Commit changes" type the message below and click **Commit changes**.
8. Empty folders are not stored by GitHub; `results/` and `visualizations/` contain a `.gitkeep` file so they still appear.

> Note: the website does not read `.gitignore` for uploads, so just do not drag in dataset files or `dashboard_exports/`.

## Method B - Git command line (optional)
Install Git from <https://git-scm.com>, then open a terminal inside the project folder:
```bash
git init
git add .
git commit -m "Initial commit: web scraping and product price analysis project"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Web-Scraping-Product-Price-Analysis.git
git push -u origin main
```
GitHub asks you to sign in; use a Personal Access Token as the password if prompted.

## Suggested initial commit message
```
Initial commit: Web scraping and product price analysis project
```
Longer version:
```
Add Playwright scraping, price analysis and Colab dashboard notebooks with documentation
```

## After uploading
* Open each notebook on GitHub to confirm it renders.
* Test the "Open in Colab" links in the README.
* Add repository **Topics**: `python`, `web-scraping`, `playwright`, `pandas`, `data-analysis`, `plotly`.
* Pin the repository on your profile for your portfolio.
