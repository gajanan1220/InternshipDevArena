import pandas as pd

data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [30000, 40000, 50000, 65000, 80000],
    "Experience": [1, 3, 5, 8, 12]
}

df = pd.DataFrame(data)
corr_matrix = df.corr()
print(corr_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()
