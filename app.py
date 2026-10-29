import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Product Price Analysis Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>
.main-title {font-size:34px;font-weight:750;text-align:center;color:#2563EB;}
.subtitle {text-align:center;color:#64748B;margin-bottom:1.5rem;}
div[data-testid="stMetric"] {background:#F1F5F9;padding:16px;border-radius:12px;border:1px solid #CBD5E1;}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-title">📊 Product Price Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Web Scraping • Price Comparison • Data Analytics</div>', unsafe_allow_html=True)

@st.cache_data
def read_uploaded_file(file):
    if file.name.lower().endswith(".xlsx"):
        return pd.read_excel(file)
    return pd.read_csv(file)

uploaded_file = st.sidebar.file_uploader("Upload product data (optional)", type=["csv", "xlsx"])
try:
    if uploaded_file is not None:
        df = read_uploaded_file(uploaded_file)
    else:
        data_path = Path(__file__).parent / "scraped_product_data.csv"
        if not data_path.exists():
            st.error("Dataset not found. Upload your CSV using the sidebar.")
            st.stop()
        df = pd.read_csv(data_path)
except Exception as exc:
    st.error(f"Could not load the dataset: {exc}")
    st.stop()

required = ["Product_Name", "Vendor", "Category", "Price", "Rating"]
missing = [col for col in required if col not in df.columns]
if missing:
    st.error("Missing required columns: " + ", ".join(missing))
    st.write("Available columns:", df.columns.tolist())
    st.stop()

df = df.copy()
df["Price"] = pd.to_numeric(df["Price"].astype(str).str.replace(r"[^0-9.]", "", regex=True), errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"].astype(str).str.extract(r"(\d+\.?\d*)")[0], errors="coerce")
for col in ["Product_Name", "Vendor", "Category"]:
    df[col] = df[col].fillna("Unknown").astype(str)
if "Stock" in df.columns:
    df["Stock"] = df["Stock"].fillna("Unknown").astype(str)
df = df.dropna(subset=["Price"])
df = df[df["Price"] >= 0]
if df.empty:
    st.error("No valid product prices were found.")
    st.stop()

st.sidebar.header("🔎 Filters")
category_options = sorted(df["Category"].unique().tolist())
vendor_options = sorted(df["Vendor"].unique().tolist())
selected_categories = st.sidebar.multiselect("Category", category_options, default=category_options)
selected_vendors = st.sidebar.multiselect("Vendor", vendor_options, default=vendor_options)
price_min, price_max = float(df["Price"].min()), float(df["Price"].max())
if price_min < price_max:
    price_range = st.sidebar.slider("Price range", price_min, price_max, (price_min, price_max))
else:
    price_range = (price_min, price_max)
selected_stock = None
if "Stock" in df.columns:
    stock_options = sorted(df["Stock"].unique().tolist())
    selected_stock = st.sidebar.multiselect("Stock status", stock_options, default=stock_options)

filtered = df[
    df["Category"].isin(selected_categories)
    & df["Vendor"].isin(selected_vendors)
    & df["Price"].between(price_range[0], price_range[1])
].copy()
if selected_stock is not None:
    filtered = filtered[filtered["Stock"].isin(selected_stock)]
if filtered.empty:
    st.warning("No products match these filters. Change one or more filters.")
    st.stop()

st.subheader("📌 Overview")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Products", f"{len(filtered):,}")
k2.metric("Average price", f"{filtered['Price'].mean():,.2f}")
k3.metric("Highest price", f"{filtered['Price'].max():,.2f}")
avg_rating = filtered["Rating"].mean()
k4.metric("Average rating", f"{avg_rating:.2f}" if pd.notna(avg_rating) else "N/A")
st.caption("Price units and ratings reflect the source dataset.")

st.divider()
st.subheader("📈 Price Analysis")
c1, c2 = st.columns(2)
with c1:
    fig = px.histogram(filtered, x="Price", nbins=25, title="Product Price Distribution")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    category_avg = filtered.groupby("Category", as_index=False)["Price"].mean().sort_values("Price", ascending=False)
    fig = px.bar(category_avg, x="Category", y="Price", title="Average Price by Category", color="Price")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("🏪 Vendor Analysis")
vendor_avg = filtered.groupby("Vendor", as_index=False).agg(Average_Price=("Price", "mean"), Product_Count=("Product_Name", "count")).sort_values("Average_Price", ascending=False)
fig = px.bar(vendor_avg, x="Vendor", y="Average_Price", color="Average_Price", hover_data=["Product_Count"], title="Average Price by Vendor")
st.plotly_chart(fig, use_container_width=True)

st.subheader("⭐ Price vs Rating")
rating_data = filtered.dropna(subset=["Rating"])
if not rating_data.empty:
    fig = px.scatter(rating_data, x="Price", y="Rating", color="Category", hover_name="Product_Name", hover_data=["Vendor"], title="Relationship Between Price and Rating")
    st.plotly_chart(fig, use_container_width=True)
    if len(rating_data) > 1 and rating_data["Price"].nunique() > 1 and rating_data["Rating"].nunique() > 1:
        corr = rating_data["Price"].corr(rating_data["Rating"])
        st.info(f"Price-rating correlation: {corr:.3f}. Correlation describes a linear association, not causation.")
else:
    st.info("No valid ratings are available.")

if "Stock" in filtered.columns:
    st.subheader("📦 Stock Availability")
    stock_counts = filtered["Stock"].value_counts().rename_axis("Stock Status").reset_index(name="Product Count")
    fig = px.pie(stock_counts, names="Stock Status", values="Product Count", title="Products by Stock Status", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("🏆 Product Comparison")
tab1, tab2, tab3 = st.tabs(["💰 Cheapest", "💎 Most Expensive", "⭐ Highest Rated"])
with tab1:
    st.dataframe(filtered.nsmallest(10, "Price"), use_container_width=True, hide_index=True)
with tab2:
    st.dataframe(filtered.nlargest(10, "Price"), use_container_width=True, hide_index=True)
with tab3:
    st.dataframe(filtered.dropna(subset=["Rating"]).nlargest(10, "Rating"), use_container_width=True, hide_index=True)

st.divider()
st.subheader("📋 Product Explorer")
query = st.text_input("Search product name, vendor, or category")
explorer = filtered.copy()
if query:
    mask = (explorer["Product_Name"].str.contains(query, case=False, na=False)
            | explorer["Vendor"].str.contains(query, case=False, na=False)
            | explorer["Category"].str.contains(query, case=False, na=False))
    explorer = explorer[mask]
st.write(f"Products shown: {len(explorer)}")
st.dataframe(explorer, use_container_width=True, hide_index=True)
st.download_button("📥 Download filtered products as CSV", data=explorer.to_csv(index=False).encode("utf-8"), file_name="filtered_product_data.csv", mime="text/csv")
st.markdown("---")
st.caption("Web Scraping and Product Price Analysis System | Python • Pandas • Streamlit • Plotly")
