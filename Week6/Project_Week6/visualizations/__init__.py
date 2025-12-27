"""
Visualization modules for the sales dashboard
"""
from .charts import (
    create_sales_trend_line,
    create_product_sales_bar,
    create_region_sales_pie,
    create_price_distribution_box,
    create_quantity_sales_scatter,
    create_correlation_heatmap,
    create_cumulative_sales_area,
    create_price_distribution_violin,
    create_monthly_sales_comparison,
    create_product_region_heatmap,
    COLOR_SCHEME
)

__all__ = [
    'create_sales_trend_line',
    'create_product_sales_bar',
    'create_region_sales_pie',
    'create_price_distribution_box',
    'create_quantity_sales_scatter',
    'create_correlation_heatmap',
    'create_cumulative_sales_area',
    'create_price_distribution_violin',
    'create_monthly_sales_comparison',
    'create_product_region_heatmap',
    'COLOR_SCHEME'
]
