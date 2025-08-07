import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🛍️ Retail Sales Dashboard - AI Engineer Portfolio")

# Load data
df = pd.read_csv("retail_sales.csv")
df['total_sales'] = df['price'] * df['quantity'] * (1 - df['discount'] / 100)

# KPI
st.subheader("📈 Key Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"Rp {df['total_sales'].sum():,.0f}")
col2.metric("Avg. Order Value", f"Rp {df['total_sales'].mean():,.0f}")

# Chart 1: Penjualan per kategori
st.subheader("📊 Sales by Category")
category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

# Chart 2: Penjualan per produk
st.subheader("📦 Sales by Product")
product_sales = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
st.bar_chart(product_sales)

st.markdown("Made by Bernadus Boli - AI Engineer Portfolio")
