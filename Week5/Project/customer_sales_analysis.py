import itertools
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_data(customer_path="Week5/Project/customer_data.csv", sales_path="D:\InternshipDevArena\Week5\Project\sales_data.csv") -> tuple[pd.DataFrame, pd.DataFrame]:
    customers = pd.read_csv(customer_path)
    sales = pd.read_csv(sales_path, parse_dates=["order_date"])
    return customers, sales


def prepare_data(customers: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = sales.merge(
        customers,
        on="customer_id",
        how="left",
        validate="many_to_one",
        suffixes=("_sale", "_cust"),
    )

    # Prefer the sales region if both exist; fall back to customer region if missing.
    if "region_sale" in merged.columns:
        merged["region"] = merged["region_sale"].fillna(merged.get("region_cust"))
    elif "region" not in merged.columns and "region_cust" in merged.columns:
        merged["region"] = merged["region_cust"]

    merged["order_month"] = merged["order_date"].dt.to_period("M").dt.to_timestamp()
    return merged


def compute_aggregations(df: pd.DataFrame) -> dict:
    top_customers = (
        df.groupby(["customer_id", "customer_name"], as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

    product_perf = (
        df.groupby("product", as_index=False)
        .agg(total_revenue=("revenue", "sum"), units_sold=("quantity", "sum"), avg_price=("unit_price", "mean"))
        .sort_values("total_revenue", ascending=False)
    )

    region_summary = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)

    monthly_trend = (
        df.groupby("order_month", as_index=False)
        .agg(monthly_revenue=("revenue", "sum"), orders=("order_id", "nunique"))
        .sort_values("order_month")
    )

    # Co-purchase signal: combos of products within the same order (may be sparse in sample data)
    combos = (
        df.groupby("order_id")["product"]
        .apply(lambda x: list(itertools.combinations(sorted(set(x)), 2)))
        .explode()
        .dropna()
    )

    if combos.empty:
        combo_counts = pd.DataFrame(columns=["product_a", "product_b", "count"])
    else:
        combo_counts = combos.value_counts().reset_index(name="count").rename(columns={"index": "pair"})
        combo_counts[["product_a", "product_b"]] = pd.DataFrame(combo_counts["pair"].tolist(), index=combo_counts.index)
        combo_counts = combo_counts.drop(columns="pair")

    pivot_region_product = pd.pivot_table(
        df, values="revenue", index="region", columns="product", aggfunc="sum", fill_value=0
    )

    return {
        "top_customers": top_customers,
        "product_perf": product_perf,
        "region_summary": region_summary,
        "monthly_trend": monthly_trend,
        "combo_counts": combo_counts,
        "pivot_region_product": pivot_region_product,
    }


def compute_kpis(df: pd.DataFrame, customers: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    total_customers = customers["customer_id"].nunique()
    avg_order_value = df["revenue"].mean()
    top_customer_row = (
        df.groupby(["customer_id", "customer_name"])["revenue"].sum().sort_values(ascending=False).reset_index().head(1)
    )
    top_customer_name = top_customer_row.at[0, "customer_name"]
    top_customer_value = top_customer_row.at[0, "revenue"]

    return {
        "total_revenue": total_revenue,
        "total_customers": total_customers,
        "avg_order_value": avg_order_value,
        "top_customer_name": top_customer_name,
        "top_customer_value": top_customer_value,
    }


def ensure_output_dir(path="outputs") -> Path:
    output_dir = Path(path)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def create_visuals(df: pd.DataFrame, aggs: dict, output_dir: Path) -> None:
    sns.set_theme(style="whitegrid")

    # Bar chart: top customers by revenue
    plt.figure(figsize=(8, 5))
    sns.barplot(data=aggs["top_customers"].head(10), x="revenue", y="customer_name", hue="customer_name", palette="Blues_d", legend=False)
    plt.title("Top Customers by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Customer")
    plt.tight_layout()
    plt.savefig(output_dir / "top_customers.png", dpi=150)
    plt.close()

    # Line: monthly revenue trend
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=aggs["monthly_trend"], x="order_month", y="monthly_revenue", marker="o", color="#2a9d8f")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_revenue_trend.png", dpi=150)
    plt.close()

    # Heatmap: revenue by region and product
    plt.figure(figsize=(8, 5))
    sns.heatmap(aggs["pivot_region_product"], annot=True, fmt=".1f", cmap="YlGnBu")
    plt.title("Revenue by Region and Product")
    plt.xlabel("Product")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.savefig(output_dir / "region_product_heatmap.png", dpi=150)
    plt.close()

    # Bar: product performance by revenue
    plt.figure(figsize=(8, 5))
    sns.barplot(data=aggs["product_perf"], x="product", y="total_revenue", hue="product", palette="crest", legend=False)
    plt.title("Product Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "product_revenue.png", dpi=150)
    plt.close()


def print_report(kpis: dict, aggs: dict) -> None:
    print("CUSTOMER SALES ANALYSIS REPORT")
    print(f"Total Revenue: ${kpis['total_revenue']:,.2f}")
    print(f"Total Customers: {kpis['total_customers']:,}")
    print(f"Average Order Value: ${kpis['avg_order_value']:,.2f}")
    print(f"Top Customer: {kpis['top_customer_name']} - ${kpis['top_customer_value']:,.2f}")
    print("\nTop 5 Customers:")
    print(aggs["top_customers"].head(5).to_string(index=False))
    print("\nProduct Performance:")
    print(aggs["product_perf"].to_string(index=False))
    print("\nRevenue by Region:")
    print(aggs["region_summary"].to_string(index=False))
    if not aggs["combo_counts"].empty:
        print("\nFrequently Bought Together (top 5 combos):")
        print(aggs["combo_counts"].head(5).to_string(index=False))
    else:
        print("\nFrequently Bought Together: insufficient multi-product orders to analyze.")


def main() -> None:
    customers, sales = load_data()
    merged = prepare_data(customers, sales)
    aggs = compute_aggregations(merged)
    kpis = compute_kpis(merged, customers)

    output_dir = ensure_output_dir()
    create_visuals(merged, aggs, output_dir)
    print_report(kpis, aggs)
    print(f"\nVisualizations saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()

