# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

# ==============================
# Load Data
# ==============================
df = pd.read_excel("data/Sample_Superstore.xls")
df = df.dropna()
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")

# ==============================
# Sidebar Navigation & Filters
# ==============================
st.sidebar.title("📊 Retail Sales Dashboard")

# Page Navigation
page = st.sidebar.radio("Navigate", ["Overview", "Forecast", "Insights"])

# Filters
region_filter = st.sidebar.multiselect(
    "Select Region(s):",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)
segment_filter = st.sidebar.multiselect(
    "Select Segment(s):",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Segment"].isin(segment_filter))
]

# ==============================
# Overview Page
# ==============================
if page == "Overview":
    st.title("📈 Retail Sales Analysis - Overview")

    # KPIs
    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    avg_discount = filtered_df["Discount"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Avg. Discount", f"{avg_discount:.2%}")

    # Sales by Region
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm", ax=ax)
    ax.set_title("Sales by Region")
    st.pyplot(fig)

    # Sales by Segment
    st.subheader("Sales by Segment")
    segment_sales = filtered_df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=segment_sales.index, y=segment_sales.values, palette="plasma", ax=ax)
    ax.set_title("Sales by Customer Segment")
    st.pyplot(fig)

    # Monthly Sales Trend
    st.subheader("Monthly Sales Trend")
    monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()
    monthly_sales["Month_dt"] = monthly_sales["Month"].dt.to_timestamp()
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(monthly_sales["Month_dt"], monthly_sales["Sales"], marker='o', color='teal')
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ==============================
# Forecast Page
# ==============================
elif page == "Forecast":
    st.title("🔮 Sales Forecasting")

    sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()
    sales["Month_dt"] = sales["Month"].dt.to_timestamp()

    # ARIMA Model
    model = ARIMA(sales["Sales"], order=(5,1,0))
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=12)

    # Plot Forecast
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(sales["Month_dt"], sales["Sales"], label="Historical Sales")
    last_month = sales["Month_dt"].iloc[-1]
    future_dates = pd.date_range(start=last_month + pd.offsets.MonthBegin(1), periods=12, freq="MS")
    ax.plot(future_dates, forecast, label="Forecasted Sales", color="red")
    plt.xticks(rotation=45)
    ax.set_title("Sales Forecast (ARIMA)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    plt.legend()
    st.pyplot(fig)

# ==============================
# Insights Page
# ==============================
elif page == "Insights":
    st.title("💡 Key Insights")

    # Top Sub-Categories by Sales
    st.subheader("Top Sub-Categories by Sales")
    subcat_sales = filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=subcat_sales.values, y=subcat_sales.index, palette="viridis", ax=ax)
    ax.set_title("Top 10 Sub-Categories by Sales")
    st.pyplot(fig)

    # Top Sub-Categories by Profit
    st.subheader("Top Sub-Categories by Profit")
    subcat_profit = filtered_df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=subcat_profit.values, y=subcat_profit.index, palette="magma", ax=ax)
    ax.set_title("Top 10 Sub-Categories by Profit")
    st.pyplot(fig)

    # Discount vs Profit
    st.subheader("Discount vs Profit")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(x="Discount", y="Profit", data=filtered_df, alpha=0.5, color="purple", ax=ax)
    ax.set_title("Discount vs Profit")
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(filtered_df[["Sales","Profit","Discount","Quantity"]].corr(), annot=True, cmap="coolwarm", center=0, ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

    # Top & Bottom Sub-Categories by Sales
    st.subheader("Top & Bottom Sub-Categories by Sales")
    subcat_sales_sorted = filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=subcat_sales_sorted.values, y=subcat_sales_sorted.index, palette="coolwarm", ax=ax)
    ax.set_title("Bottom & Top Sub-Categories by Sales")
    st.pyplot(fig)
