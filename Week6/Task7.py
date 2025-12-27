import matplotlib.pyplot as plt

group_A = [45, 48, 50, 52, 49, 47, 46]
group_B = [55, 58, 60, 62, 59, 57, 56]
group_C = [40, 42, 41, 43, 44, 45, 46]


plt.boxplot([group_A, group_B, group_C])
plt.xticks([1, 2, 3], ["Group A", "Group B", "Group C"])
plt.title("Box Plot of Data")
plt.ylabel("Values")
plt.show()

