import matplotlib.pyplot as plt

# Sample data — replace with your own
categories = ['Rent', 'Food', 'Transport', 'Shopping', 'Bills', 'Other']
expenses = [15000, 6000, 2000, 4000, 2500, 1500]

# Create pie chart
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=90)

plt.title('Expense Distribution')
plt.axis('equal')  # Makes the pie chart a perfect circle
plt.show()
