"""
Interactive Sales Dashboard
A comprehensive dashboard showing sales trends, customer segmentation, and product performance
"""
import streamlit as st
import pandas as pd
import numpy as np
from visualizations.charts import (
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
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #6366f1;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #6366f1;
    }
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load and cache the sales data"""
    df = pd.read_csv('sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Load data
df = load_data()

# Header
st.markdown('<h1 class="main-header">📊 Interactive Sales Dashboard</h1>', unsafe_allow_html=True)

# Sidebar for filters
st.sidebar.header("🔍 Filters")

# Date filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['Date'].min(), df['Date'].max()),
    min_value=df['Date'].min(),
    max_value=df['Date'].max()
)

# Product filter
products = st.sidebar.multiselect(
    "Select Products",
    options=sorted(df['Product'].unique()),
    default=sorted(df['Product'].unique())
)

# Region filter
regions = st.sidebar.multiselect(
    "Select Regions",
    options=sorted(df['Region'].unique()),
    default=sorted(df['Region'].unique())
)

# Apply filters
filtered_df = df[
    (df['Date'].dt.date >= pd.to_datetime(date_range[0]).date()) &
    (df['Date'].dt.date <= pd.to_datetime(date_range[1]).date()) &
    (df['Product'].isin(products)) &
    (df['Region'].isin(regions))
]

# Key Metrics
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['Total_Sales'].sum()
    st.metric("Total Sales", f"${total_sales:,.0f}")

with col2:
    avg_order_value = filtered_df['Total_Sales'].mean()
    st.metric("Average Order Value", f"${avg_order_value:,.2f}")

with col3:
    total_orders = len(filtered_df)
    st.metric("Total Orders", f"{total_orders:,}")

with col4:
    unique_customers = filtered_df['Customer_ID'].nunique()
    st.metric("Unique Customers", f"{unique_customers:,}")

st.divider()

# Chart Selection
st.sidebar.header("📊 Chart Selection")
chart_options = st.sidebar.multiselect(
    "Select Charts to Display",
    options=[
        "Sales Trend Over Time",
        "Sales by Product",
        "Sales by Region",
        "Price Distribution (Box Plot)",
        "Quantity vs Sales Scatter",
        "Correlation Heatmap",
        "Cumulative Sales",
        "Price Distribution (Violin)",
        "Monthly Sales Comparison",
        "Product vs Region Heatmap"
    ],
    default=[
        "Sales Trend Over Time",
        "Sales by Product",
        "Sales by Region",
        "Quantity vs Sales Scatter",
        "Correlation Heatmap"
    ]
)

# Main dashboard area
if "Sales Trend Over Time" in chart_options:
    st.header("📈 Sales Trend Over Time")
    fig = create_sales_trend_line(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

if "Cumulative Sales" in chart_options:
    st.header("📈 Cumulative Sales Over Time")
    fig = create_cumulative_sales_area(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

# Two column layout for some charts
col1, col2 = st.columns(2)

with col1:
    if "Sales by Product" in chart_options:
        st.header("📊 Sales by Product")
        fig = create_product_sales_bar(filtered_df)
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if "Sales by Region" in chart_options:
        st.header("🌍 Sales by Region")
        fig = create_region_sales_pie(filtered_df)
        st.plotly_chart(fig, use_container_width=True)

if "Sales by Product" in chart_options or "Sales by Region" in chart_options:
    st.divider()

if "Monthly Sales Comparison" in chart_options:
    st.header("📅 Monthly Sales Comparison")
    fig = create_monthly_sales_comparison(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

if "Quantity vs Sales Scatter" in chart_options:
    st.header("🎯 Quantity vs Total Sales Analysis")
    fig = create_quantity_sales_scatter(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

# Seaborn charts (convert matplotlib to streamlit)
col1, col2 = st.columns(2)

with col1:
    if "Price Distribution (Box Plot)" in chart_options:
        st.header("📦 Price Distribution by Product")
        fig = create_price_distribution_box(filtered_df)
        st.pyplot(fig)
        plt.close()

with col2:
    if "Price Distribution (Violin)" in chart_options:
        st.header("🎻 Price Distribution (Violin Plot)")
        fig = create_price_distribution_violin(filtered_df)
        st.pyplot(fig)
        plt.close()

if "Price Distribution (Box Plot)" in chart_options or "Price Distribution (Violin)" in chart_options:
    st.divider()

if "Product vs Region Heatmap" in chart_options:
    st.header("🔥 Sales Heatmap: Product vs Region")
    fig = create_product_region_heatmap(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

if "Correlation Heatmap" in chart_options:
    st.header("🔥 Correlation Analysis")
    fig = create_correlation_heatmap(filtered_df)
    st.pyplot(fig)
    plt.close()
    st.divider()

# Data Table
with st.expander("📋 View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_sales_data.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b7280;'>Interactive Sales Dashboard | Built with Streamlit, Plotly, and Seaborn</div>",
    unsafe_allow_html=True
)

