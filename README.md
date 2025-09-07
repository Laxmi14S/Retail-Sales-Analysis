🛍️ Retail Sales Analysis - Standalone Project
📌 Project Overview

This project performs a comprehensive analysis of retail sales using the Superstore dataset.
It includes data cleaning, exploratory data analysis, visualization, and sales forecasting using ARIMA.

The project is a standalone Python application—no Streamlit required.

The main goals are:

Identify top-performing products and sub-categories

Analyze regional and segment sales trends

Examine the impact of discounts on profitability

Forecast monthly sales for the next 12 months

🛠 Features

Sales & Profit Summary

Total Sales, Total Profit, and Average Discount metrics.

Top Sub-Categories Analysis

Top 10 sub-categories by sales and profit.

Regional & Segment Insights

Sales by Region and Customer Segment.

Discount vs Profit Analysis

Scatter plot to analyze the effect of discounts on profit.

Sales Forecasting

ARIMA model forecasting next 12 months of sales.

Seasonal Decomposition

Decomposes sales into trend, seasonality, and residuals.

Visualizations

Bar plots, line charts, scatter plots, and correlation heatmaps.

📊 Forecasting & Business Insights
🔮 Sales Forecast (ARIMA)

We used an ARIMA model to forecast monthly sales for the next 12 months.
The forecast shows:

A steady upward trend in sales over time.

Seasonal spikes around November–December, indicating holiday season demand.

📉 Seasonal Decomposition

By decomposing sales into trend, seasonality, and residuals, we observed:

Trend: Long-term growth in overall sales.

Seasonality: Recurring spikes in Q4 each year (holiday effect).

Residuals: Short-term fluctuations likely caused by promotions/discounts.

✅ Business Recommendations

Stock Planning → Increase inventory before November–December to capture peak demand.

Discount Strategy → Optimize discounts in Q4, as sales rise naturally during this period.

Regional Focus → Expand marketing in underperforming regions (from EDA insights).

Profitability Check → Limit deep discounts on low-margin products (Discount vs Profit analysis).

📈 Sample Visuals

Top Sub-Categories by Sales


Top Sub-Categories by Profit


Monthly Sales Trend


Discount vs Profit


📝 Dataset

Dataset file: Sample_Superstore.xls

Source: Kaggle Superstore Sales Dataset

Path in project: data/Sample_Superstore.xls

Columns include: Order Date, Ship Date, Segment, Region, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

💻 How to Run Locally

Clone the repository

git clone https://github.com/Laxmi14S/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis


Create a virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux


Install dependencies

pip install -r requirements.txt


Run the analysis

python sales_analysis.py

📦 Requirements

Python >= 3.9

pandas

matplotlib

seaborn

statsmodels

openpyxl

xlrd

🔍 Key Insights

Certain sub-categories consistently outperform others in sales and profit.

Discounts have varying effects on profit across products.

Regional and segment trends help identify target markets for growth.

Forecasting provides actionable insights for inventory and sales planning.

🏆 Outcome

Enhanced data analysis and visualization skills.

Standalone project ready for portfolio and interviews.

Showcases sales forecasting and business insights from real-world retail data.

📂 Folder Structure
Retail_Sales_Project/
│
├─ data/                  # Dataset
│   └─ Sample_Superstore.xls
├─ plots/                 # Generated plots
├─ sales_analysis.py       # Main analysis script
├─ forecasting.py          # ARIMA forecasting script
├─ README.md               # Project documentation
├─ requirements.txt
└─ .gitignore