import pandas as pd
import matplotlib.pyplot as plt

Data=pd.read_csv('D:/InternshipDevArena/Week4/monthlytemperature.csv', encoding='latin1')




Data["Date"]=pd.to_datetime(Data['Date'])

Data['Month'] = Data['Date'].dt.month_name()


monthly_avg = Data.groupby('Month')['Mean'].mean()

monthly_avg = monthly_avg.reindex([
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
])
plt.plot(monthly_avg.index, monthly_avg.values, marker='o')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Monthly Temperature Changes')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
