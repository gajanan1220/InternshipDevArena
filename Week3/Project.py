import pandas as pd

# Sample sales dataset
sales_data = {
    "OrderID": [101,102,103,104,105,106,107,108,109,110],
    "Product": ["Notebook","Pen","Backpack","Calculator","Marker","Desk Lamp","USB Drive","Water Bottle","Headphones","Charger"],
    "Quantity": [5,10,2,1,12,3,4,6,2,5],
    "Price": [50,10,800,1200,15,450,300,200,1500,600]
}

# Calculate total per order
df = pd.DataFrame(sales_data)
df["Total"] = df["Quantity"] * df["Price"]

print(df)

total_sales = df["Total"].sum()
print("Total Sales:", total_sales)

# By revenue
best_product_revenue = df.groupby("Product")["Total"].sum().idxmax()
best_revenue_value = df.groupby("Product")["Total"].sum().max()

# By quantity
best_product_quantity = df.groupby("Product")["Quantity"].sum().idxmax()
best_quantity_value = df.groupby("Product")["Quantity"].sum().max()

print("Best Product by Revenue:", best_product_revenue, "-", best_revenue_value)
print("Best Product by Quantity:", best_product_quantity, "-", best_quantity_value)

report = f"""
Sales Report
------------
Total Sales: {total_sales}

Best-Selling Product (Revenue): {best_product_revenue} with sales of {best_revenue_value}
Best-Selling Product (Quantity): {best_product_quantity} with {best_quantity_value} units sold
"""

print(report)


