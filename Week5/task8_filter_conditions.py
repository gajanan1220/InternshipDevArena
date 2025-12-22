"""
Task 8: Filter data using multiple conditions (AND, OR)
Run: python task8_filter_conditions.py
"""

import pandas as pd


def main():
    data = [
        {"order_id": 1, "region": "West", "sales": 1800, "channel": "Online"},
        {"order_id": 2, "region": "East", "sales": 2400, "channel": "Retail"},
        {"order_id": 3, "region": "West", "sales": 2600, "channel": "Retail"},
        {"order_id": 4, "region": "South", "sales": 900, "channel": "Online"},
        {"order_id": 5, "region": "East", "sales": 3100, "channel": "Online"},
    ]
    df = pd.DataFrame(data)

    # AND condition: West region AND sales > 2000
    filtered_and = df[(df["region"] == "West") & (df["sales"] > 2000)]

    # OR condition: West region OR sales > 2000
    filtered_or = df[(df["region"] == "West") | (df["sales"] > 2000)]

    # Mixing AND/OR with parentheses to control precedence
    filtered_mixed = df[((df["region"] == "East") & (df["channel"] == "Online")) | (df["sales"] > 2500)]

    print("Original:")
    print(df, "\n")

    print("AND (West & sales > 2000):")
    print(filtered_and, "\n")

    print("OR (West | sales > 2000):")
    print(filtered_or, "\n")

    print("Mixed ((East & Online) | sales > 2500):")
    print(filtered_mixed, "\n")


if __name__ == "__main__":
    main()

