import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [30000, 40000, 50000, 65000, 80000],
    "Experience": [1, 3, 5, 8, 12]
})

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Scatter
axes[0, 0].scatter(df["Experience"], df["Salary"])
axes[0, 0].set_title("Experience vs Salary")

# Line
axes[0, 1].plot(df["Age"], df["Salary"])
axes[0, 1].set_title("Salary vs Age")

# Histogram
axes[1, 0].hist(df["Salary"])
axes[1, 0].set_title("Salary Distribution")

# Heatmap
sns.heatmap(df.corr(), annot=True, ax=axes[1, 1])
axes[1, 1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()
