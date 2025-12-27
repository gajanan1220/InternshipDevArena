# ===============================
# IMPORT LIBRARIES
# ===============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# GLOBAL STYLING (PROFESSIONAL)
# ===============================
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12


# ===============================
# SAMPLE DATA
# ===============================
df = pd.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [30000, 40000, 50000, 65000, 80000],
    "Experience": [1, 3, 5, 8, 12],
    "Department": ["IT", "HR", "IT", "Sales", "Sales"]
})


# ===============================
# 1️⃣ LINE CHART
# ===============================
plt.figure()
plt.plot(df["Age"], df["Salary"], linewidth=2)
plt.title("Salary Growth with Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()


# ===============================
# 2️⃣ BAR CHART
# ===============================
dept_avg_salary = df.groupby("Department")["Salary"].mean()

plt.figure()
plt.bar(dept_avg_salary.index, dept_avg_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()


# ===============================
# 3️⃣ SCATTER PLOT
# ===============================
plt.figure()
plt.scatter(df["Experience"], df["Salary"], s=80)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid(True)
plt.show()


# ===============================
# 4️⃣ BOX PLOT (DISTRIBUTION)
# ===============================
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()


# ===============================
# 5️⃣ HISTOGRAM
# ===============================
plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# ===============================
# 6️⃣ CORRELATION HEATMAP
# ===============================
plt.figure(figsize=(6, 4))
sns.heatmap(df.select_dtypes(include=["int64", "float64"]).corr(),
            annot=True,
            linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
