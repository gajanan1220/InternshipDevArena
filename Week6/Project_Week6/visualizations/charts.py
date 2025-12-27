"""
Chart creation functions using Seaborn for statistical plots and Plotly for interactive charts
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

# Cohesive color scheme
COLOR_SCHEME = {
    'primary': '#6366f1',      # Indigo
    'secondary': '#8b5cf6',    # Purple
    'accent': '#ec4899',       # Pink
    'success': '#10b981',      # Green
    'warning': '#f59e0b',      # Amber
    'danger': '#ef4444',       # Red
    'palette': ['#6366f1', '#8b5cf6', '#ec4899', '#10b981', '#f59e0b', '#06b6d4']
}

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_palette(COLOR_SCHEME['palette'])


def create_sales_trend_line(df):
    """
    Create an interactive line chart showing sales trends over time (Plotly)
    """
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    daily_sales = df_copy.groupby('Date')['Total_Sales'].sum().reset_index()
    daily_sales = daily_sales.sort_values('Date')
    
    fig = px.line(
        daily_sales,
        x='Date',
        y='Total_Sales',
        title='📈 Sales Trend Over Time',
        labels={'Total_Sales': 'Total Sales ($)', 'Date': 'Date'},
        markers=True,
        line_shape='spline',
        color_discrete_sequence=[COLOR_SCHEME['primary']]
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Total Sales ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        plot_bgcolor='white'
    )
    return fig


def create_product_sales_bar(df):
    """
    Create an interactive bar chart showing sales by product (Plotly)
    """
    product_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()
    product_sales = product_sales.sort_values('Total_Sales', ascending=True)
    
    fig = px.bar(
        product_sales,
        x='Total_Sales',
        y='Product',
        orientation='h',
        title='📊 Total Sales by Product',
        labels={'Total_Sales': 'Total Sales ($)', 'Product': 'Product'},
        color='Total_Sales',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis_title='Total Sales ($)',
        yaxis_title='Product',
        template='plotly_white',
        height=400,
        showlegend=False,
        plot_bgcolor='white'
    )
    return fig


def create_region_sales_pie(df):
    """
    Create an interactive pie chart showing sales distribution by region (Plotly)
    """
    region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()
    
    fig = px.pie(
        region_sales,
        values='Total_Sales',
        names='Region',
        title='🌍 Sales Distribution by Region',
        color_discrete_sequence=COLOR_SCHEME['palette']
    )
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Sales: $%{value:,.0f}<br>Percentage: %{percent}<extra></extra>'
    )
    fig.update_layout(
        template='plotly_white',
        height=400,
        plot_bgcolor='white'
    )
    return fig


def create_price_distribution_box(df):
    """
    Create a box plot showing price distribution by product (Seaborn to Matplotlib to Plotly conversion)
    """
    # Create figure using matplotlib/seaborn
    plt.figure(figsize=(10, 6))
    ax = sns.boxplot(
        data=df,
        x='Product',
        y='Price',
        palette=COLOR_SCHEME['palette']
    )
    ax.set_title('📦 Price Distribution by Product', fontsize=14, fontweight='bold')
    ax.set_xlabel('Product', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return ax.get_figure()


def create_quantity_sales_scatter(df):
    """
    Create an interactive scatter plot showing relationship between quantity and sales (Plotly)
    """
    fig = px.scatter(
        df,
        x='Quantity',
        y='Total_Sales',
        color='Product',
        size='Price',
        title='🎯 Quantity vs Total Sales by Product',
        labels={
            'Quantity': 'Quantity',
            'Total_Sales': 'Total Sales ($)',
            'Price': 'Price ($)'
        },
        hover_data=['Region', 'Customer_ID'],
        color_discrete_sequence=COLOR_SCHEME['palette']
    )
    fig.update_layout(
        xaxis_title='Quantity',
        yaxis_title='Total Sales ($)',
        template='plotly_white',
        height=400,
        plot_bgcolor='white'
    )
    return fig


def create_correlation_heatmap(df):
    """
    Create a correlation heatmap of numerical features (Seaborn)
    """
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numerical_cols].corr()
    
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        center=0,
        square=True,
        fmt='.2f',
        cbar_kws={'label': 'Correlation Coefficient'}
    )
    ax.set_title('🔥 Correlation Heatmap of Sales Metrics', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return ax.get_figure()


def create_cumulative_sales_area(df):
    """
    Create an interactive area chart showing cumulative sales over time (Plotly)
    """
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    daily_sales = df_copy.groupby('Date')['Total_Sales'].sum().reset_index()
    daily_sales = daily_sales.sort_values('Date')
    daily_sales['Cumulative_Sales'] = daily_sales['Total_Sales'].cumsum()
    
    fig = px.area(
        daily_sales,
        x='Date',
        y='Cumulative_Sales',
        title='📈 Cumulative Sales Over Time',
        labels={'Cumulative_Sales': 'Cumulative Sales ($)', 'Date': 'Date'},
        color_discrete_sequence=[COLOR_SCHEME['primary']]
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Cumulative Sales ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        plot_bgcolor='white'
    )
    return fig


def create_price_distribution_violin(df):
    """
    Create a violin plot showing price distribution by product (Seaborn)
    """
    plt.figure(figsize=(10, 6))
    ax = sns.violinplot(
        data=df,
        x='Product',
        y='Price',
        palette=COLOR_SCHEME['palette'],
        inner='box'
    )
    ax.set_title('🎻 Price Distribution by Product (Violin Plot)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Product', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return ax.get_figure()


def create_monthly_sales_comparison(df):
    """
    Create a bar chart comparing monthly sales (Plotly)
    """
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    df_copy['Month'] = df_copy['Date'].dt.strftime('%Y-%m')
    
    monthly_sales = df_copy.groupby('Month')['Total_Sales'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values('Month')
    
    fig = px.bar(
        monthly_sales,
        x='Month',
        y='Total_Sales',
        title='📅 Monthly Sales Comparison',
        labels={'Total_Sales': 'Total Sales ($)', 'Month': 'Month'},
        color='Total_Sales',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Total Sales ($)',
        template='plotly_white',
        height=400,
        showlegend=False,
        plot_bgcolor='white'
    )
    return fig


def create_product_region_heatmap(df):
    """
    Create a heatmap showing sales by product and region (Plotly)
    """
    pivot_data = df.pivot_table(
        values='Total_Sales',
        index='Product',
        columns='Region',
        aggfunc='sum'
    ).fillna(0)
    
    fig = px.imshow(
        pivot_data,
        labels=dict(x="Region", y="Product", color="Total Sales ($)"),
        title='🔥 Sales Heatmap: Product vs Region',
        color_continuous_scale='Viridis',
        aspect='auto'
    )
    fig.update_layout(
        template='plotly_white',
        height=400,
        plot_bgcolor='white'
    )
    return fig

