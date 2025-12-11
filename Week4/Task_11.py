import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1) LOAD DATA
# ---------------------------------------------------------
df = pd.read_csv(r'D:/InternshipDevArena/Week4/monthlytemperature.csv', encoding='latin1')

print("✅ Data Loaded Successfully")
print(df.head())
print(df.info())

# ---------------------------------------------------------
# 2) CLEAN DATA
# ---------------------------------------------------------

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows where Date failed to convert
df = df.dropna(subset=['Date'])

# Extract month name
df['Month'] = df['Date'].dt.month_name()

# Remove missing or invalid Mean values
df = df.dropna(subset=['Mean'])

print("\n✅ Data After Cleaning")
print(df.head())

# ---------------------------------------------------------
# 3) ANALYSIS
# ---------------------------------------------------------

# Group by month and calculate average temperature
monthly_avg = df.groupby('Month')['Mean'].mean()

# Sort months in correct order
month_order = [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
]

monthly_avg = monthly_avg.reindex(month_order)

print("\n✅ Monthly Average Temperature")
print(monthly_avg)

# ---------------------------------------------------------
# 4) VISUALIZATION
# ---------------------------------------------------------

plt.figure(figsize=(10,5))
plt.plot(monthly_avg.index, monthly_avg.values, marker='o', color='blue')

plt.title('Monthly Temperature Changes')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
