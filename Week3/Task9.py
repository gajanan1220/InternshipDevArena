import pandas as pd
import numpy as np

# Create a simple dataset with some missing values
data = {
    "StudentID": [1,2,3,4,5],
    "Name": ["Amit","Neha","Ravi","Pooja","Arjun"],
    "Math": [78,92,np.nan,80,55],
    "Science": [85,88,70,np.nan,60],
    "English": [74,90,68,82,np.nan]
}

df = pd.DataFrame(data)

# Display first few rows
print("First 5 rows:")
print(df.head())
