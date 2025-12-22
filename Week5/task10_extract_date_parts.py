"""
Task 10: Extract year, month, day from date columns
Run: python task10_extract_date_parts.py
"""

import pandas as pd


def main():
    df = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "order_date": ["2024-01-05", "2024-02-20", "2024-03-15", "2024-03-28"],
            "sales": [100, 250, 180, 90],
        }
    )

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["day"] = df["order_date"].dt.day
    df["month_name"] = df["order_date"].dt.month_name()
    df["order_period"] = df["order_date"].dt.to_period("M")  # handy for grouping

    print(df)


if __name__ == "__main__":
    main()

