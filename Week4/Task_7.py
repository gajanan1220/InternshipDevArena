import pandas as pd
import matplotlib.pyplot as plt

Data=pd.read_csv('D:/InternshipDevArena/Week4/sales.csv', encoding='latin1')

Data=Data.rename(columns={'PRODUCTLINE':'PRODUCTCATEGORY'})
print(Data.info())

plt.bar(Data['PRODUCTCATEGORY'],Data['SALES'])
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.title('Sales by Product Category')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



