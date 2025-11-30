import pandas as pd
import numpy as np

student_data = {
    "StudentID": [1,2,3,4,5],
    "Name": ["Amit","Neha","Ravi","Pooja","Arjun"],
    "Math": [78,92,np.nan,80,55],
    "Science": [85,88,70,np.nan,60],
    "English": [74,90,68,82,np.nan]
}

df=pd.DataFrame(student_data)

# Show missing values count
print("\nMissing values per column:")
print(df.isnull().sum())

# Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nAfter filling missing values:")
print(df_filled)
