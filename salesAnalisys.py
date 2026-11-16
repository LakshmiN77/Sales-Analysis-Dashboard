
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read your CSV file
 

file_path = r"C:\Users\lucky\OneDrive\Attachments\Desktop\SalesPerform\data\Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print(df.head())
print("Dataset loaded successfully!")
print("Shape:", df.shape)

# Clean data
df = df.drop_duplicates()
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df = df.dropna(subset=["Order Date", "Sales", "Profit"])

# Create month column
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Calculate KPIs
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order ID"].nunique())
print("Profit Margin (%):", round(
    df["Profit"].sum() / df["Sales"].sum() * 100, 2
))

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
))

# Create output folders
Path("output").mkdir(exist_ok=True)

# Save cleaned dataset
df.to_csv("output/superstore_clean.csv", index=False)

# Monthly sales chart
df.groupby("Month")["Sales"].sum().plot(
    figsize=(10, 5), marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/monthly_sales.png")
plt.close()

print("\nDone! Check the output folder.")

import matplotlib.pyplot as plt
from pathlib import Path

# Create output folder
output = Path("output")
output.mkdir(exist_ok=True)

# Check dataset
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates().copy()

# Convert data types
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# Remove rows missing essential values
df = df.dropna(
    subset=["Order Date", "Sales", "Profit"]
).copy()

# Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
profit_margin = (
    total_profit / total_sales * 100 if total_sales else 0
)

print("\n--- SALES ANALYSIS ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# Category analysis
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().round(2))

# Regional profit analysis
print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum().round(2))

# Create month column
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Monthly sales chart
df.groupby("Year-Month")["Sales"].sum().plot(
    figsize=(10, 5), marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output / "monthly_sales.png")
plt.show()
plt.close()

# Save cleaned data for Power BI
df.to_csv(output / "superstore_clean.csv", index=False)

print("\nSUCCESS! Cleaned data saved to output/superstore_clean.csv")
