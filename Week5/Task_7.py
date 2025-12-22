import pandas as pd

# Example sales data
df = pd.DataFrame({
    "date": ["2024-01-05","2024-01-20","2024-02-02","2024-02-18","2024-03-01"],
    "sales": [100, 200, 150, 125, 300],
})

# Ensure dates are datetime
df["date"] = pd.to_datetime(df["date"])

# Group by month and sum
monthly = (
    df
    .resample("MS", on="date")  # month start
    .agg(monthly_sales=("sales", "sum"), orders=("sales", "size"))
    .reset_index()
)

print(monthly)