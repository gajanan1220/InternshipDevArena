"""
Task 11: Merge customer data with sales data
Run: python task11_merge_customer_sales.py
"""

import pandas as pd


def main():
    customers = pd.DataFrame(
        {
            "customer_id": [101, 102, 103],
            "customer_name": ["Alice", "Bob", "Charlie"],
            "segment": ["Retail", "Wholesale", "Retail"],
        }
    )

    sales = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "customer_id": [101, 102, 104, 101],  # Note: 104 not in customers
            "order_date": pd.to_datetime(["2024-01-05", "2024-01-06", "2024-01-07", "2024-02-01"]),
            "sales": [120, 330, 210, 150],
        }
    )

    merged = sales.merge(customers, on="customer_id", how="left", indicator=True)

    print("Customers:")
    print(customers, "\n")

    print("Sales:")
    print(sales, "\n")

    print("Merged (left join on customer_id):")
    print(merged, "\n")

    # Identify unmatched records (e.g., customer_id 104)
    unmatched = merged[merged["_merge"] == "left_only"]
    print("Unmatched sales (customers missing):")
    print(unmatched, "\n")


if __name__ == "__main__":
    main()

