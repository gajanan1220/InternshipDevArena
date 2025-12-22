"""
Task 12: Create pivot tables to summarize data by categories
Run: python task12_pivot_tables.py
"""

import pandas as pd


def main():
    df = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5, 6],
            "category": ["Resistor", "Capacitor", "IC", "Resistor", "IC", "Cable"],
            "order_date": pd.to_datetime(["2024-01-05", "2024-01-12", "2024-02-03", "2024-02-18", "2024-03-01", "2024-03-10"]),
            "sales": [120, 80, 450, 200, 300, 150],
            "quantity": [10, 8, 15, 20, 12, 25],
        }
    )

    df["order_period"] = df["order_date"].dt.to_period("M")

    pivot = pd.pivot_table(
        df,
        values="sales",
        index="category",
        columns="order_period",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total",
    )

    pivot_qty = pd.pivot_table(
        df,
        values="quantity",
        index="category",
        columns="order_period",
        aggfunc="sum",
        fill_value=0,
    )

    print("Sales by category and month (pivot table):")
    print(pivot, "\n")

    print("Quantity by category and month:")
    print(pivot_qty, "\n")


if __name__ == "__main__":
    main()

