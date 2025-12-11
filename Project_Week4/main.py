import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------
# 1. CONFIGURATION
# --------------------------------
FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "sales.csv")  # Change to .xlsx if needed

# --------------------------------
# 2. DATA LOADING WITH ERROR HANDLING
# --------------------------------
try:
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"File not found at path: {FILE_PATH}")

    file_ext = os.path.splitext(FILE_PATH)[1].lower()

    if file_ext == ".csv":
        df = pd.read_csv(FILE_PATH, encoding="latin1")
    elif file_ext in [".xlsx", ".xls"]:
        df = pd.read_excel(FILE_PATH)
    else:
        raise ValueError(f"Unsupported file type: {file_ext}")

    print("✅ Data loaded successfully.\n")
except Exception as e:
    print("❌ Error loading file:", e)
    exit()

print("First 5 rows of raw data:")
print(df.head(), "\n")

# --------------------------------
# 3. DATA CLEANING & VALIDATION
# --------------------------------

# ✅ Use your actual column names
category_col = "PRODUCTLINE"
sales_col = "SALES"
date_col = "ORDERDATE"

# Drop rows where critical data is missing
df = df.dropna(subset=[category_col, sales_col])

# Ensure Sales is numeric
df[sales_col] = pd.to_numeric(df[sales_col], errors="coerce")
df = df.dropna(subset=[sales_col])

# Clean Category names
df[category_col] = df[category_col].astype(str).str.strip().str.title()

# Convert date column
df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
df = df.dropna(subset=[date_col])

print("✅ Data after cleaning:")
print(df.head(), "\n")
print("Data info:")
print(df.info(), "\n")

# --------------------------------
# 4. FEATURE ENGINEERING
# --------------------------------
df["YearMonth"] = df[date_col].dt.to_period("M").astype(str)

# --------------------------------
# 5. ANALYSIS
# --------------------------------

# Total sales by category
category_sales = df.groupby(category_col)[sales_col].sum().sort_values(ascending=False)

# Monthly sales trend
monthly_sales = df.groupby("YearMonth")[sales_col].sum()

# Basic metrics
total_sales = df[sales_col].sum()
avg_sale = df[sales_col].mean()
max_sale = df[sales_col].max()
min_sale = df[sales_col].min()

print("✅ Total sales by category:")
print(category_sales, "\n")

print("✅ Monthly sales:")
print(monthly_sales, "\n")

print("✅ Overall metrics:")
print(f"Total Sales: {total_sales:.2f}")
print(f"Average Sale Amount: {avg_sale:.2f}")
print(f"Max Single Sale: {max_sale:.2f}")
print(f"Min Single Sale: {min_sale:.2f}\n")

# --------------------------------
# 6. VISUALIZATION (2+ charts)
# --------------------------------

# Chart 1: Bar chart – Sales by category
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values, color="skyblue")
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Pie chart – Sales distribution
plt.figure(figsize=(6, 6))
plt.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Sales Distribution by Category")
plt.axis("equal")
plt.tight_layout()
plt.show()

# Chart 3: Line chart – Monthly sales trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------
# 7. TEXTUAL INSIGHTS
# --------------------------------
print("\n📌 INSIGHTS:")

# 1. Best performing category
top_category = category_sales.idxmax()
top_value = category_sales.max()
print(f"1) Best performing category: '{top_category}' with total sales of {top_value:.2f}.")

# 2. Weakest category
bottom_category = category_sales.idxmin()
bottom_value = category_sales.min()
print(f"2) Lowest performing category: '{bottom_category}' with total sales of {bottom_value:.2f}.")

# 3. Category concentration
top_share = (top_value / total_sales) * 100
print(f"3) The top category contributes {top_share:.1f}% of total sales.")

# 4. Monthly trend insight
first_month = monthly_sales.index[0]
last_month = monthly_sales.index[-1]
trend = "increased" if monthly_sales.iloc[-1] > monthly_sales.iloc[0] else "decreased"
print(f"4) Sales have {trend} from {first_month} to {last_month}.")

# 5. Average ticket size
print(f"5) The average sale amount is {avg_sale:.2f}.")

print("\n✅ Sales analysis completed successfully.")
