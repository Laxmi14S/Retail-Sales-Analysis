# Retail Sales Analysis - Extended (Superstore Dataset)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ===============================
# Prepare folder for plots
# ===============================
if not os.path.exists("plots"):
    os.makedirs("plots")

# Step 1: Load Dataset
df = pd.read_excel("data/Sample_Superstore.xls")  # For .xls version
print("Dataset Shape:", df.shape)
print(df.head())

# Step 2: Data Cleaning
df = df.dropna()
print("Cleaned Shape:", df.shape)

# Step 3: Sales & Profit Summary
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# ===============================
# PART A: Top Categories & Products
# ===============================
print("\nTop 5 Sub-Categories by Sales:")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head())

print("\nTop 5 Sub-Categories by Profit:")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).head())

# Sales by Sub-Category
top_subcats = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_subcats.values, y=top_subcats.index, palette="viridis")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("plots/top_subcategories_sales.png")
plt.show()

# Profit by Sub-Category
top_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_profit.values, y=top_profit.index, palette="magma")
plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("plots/top_subcategories_profit.png")
plt.show()

# ===============================
# PART B: Monthly Sales Trend
# ===============================
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", marker="o", color="teal")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("plots/monthly_sales_trend.png")
plt.show()

# ===============================
# PART C: Regional & Segment Insights
# ===============================
# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(6,4))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("plots/sales_by_region.png")
plt.show()

# Sales by Segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(6,4))
sns.barplot(x=segment_sales.index, y=segment_sales.values, palette="plasma")
plt.title("Sales by Customer Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("plots/sales_by_segment.png")
plt.show()

# ===============================
# PART D: Discount vs Profit Analysis
# ===============================
plt.figure(figsize=(8,5))
sns.scatterplot(x="Discount", y="Profit", data=df, alpha=0.5, color="purple")
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("plots/discount_vs_profit.png")
plt.show()

# ===============================
# PART E: Correlation Heatmap
# ===============================
plt.figure(figsize=(8,6))
sns.heatmap(df[["Sales", "Profit", "Discount", "Quantity"]].corr(), annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()
