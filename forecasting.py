import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
from statsmodels.tsa.seasonal import seasonal_decompose


# ===============================
# Prepare folder for plots
# ===============================
if not os.path.exists("plots"):
    os.makedirs("plots")

# Step 1: Load Dataset
df = pd.read_excel("data/Sample_Superstore.xls")
df = df.dropna()

# Step 2: Prepare Data for Forecasting
df["Order Date"] = pd.to_datetime(df["Order Date"])
sales = df.groupby("Order Date")["Sales"].sum().reset_index()

# Resample monthly (aggregate)
sales = sales.resample("M", on="Order Date").sum().reset_index()
sales = sales.rename(columns={"Order Date": "ds", "Sales": "y"})

# Step 3: Fit ARIMA Model
model = ARIMA(sales["y"], order=(5, 1, 0))  # (p,d,q) parameters
model_fit = model.fit()

# Step 4: Forecast Next 12 Months
forecast = model_fit.forecast(steps=12)

# Seasonal Decomposition (monthly)
result = seasonal_decompose(sales.set_index("ds")["y"], model="additive", period=12)

# Plot decomposition
fig = result.plot()
fig.set_size_inches(12, 8)
plt.savefig("plots/sales_decomposition.png")
plt.show()

plt.figure(figsize=(12,6))
plt.plot(sales["ds"], sales["y"], label="Actual Sales", color="blue", marker="o")
plt.plot(pd.date_range(sales["ds"].iloc[-1], periods=12, freq="M"),
         forecast, label="Forecast (Next 12 Months)", color="red", marker="x", linestyle="--")
plt.title("Sales Forecast with ARIMA")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/sales_forecast_arima.png")
plt.show()
