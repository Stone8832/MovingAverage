import pandas as pd
import matplotlib.pyplot as plt

#Goal: Create a graph that shows transaction activity over time
#inputs the csv file
data = pd.read_csv(r"C:\Users\willr\Downloads\Klima DAO coin data - New 50,000 data (1).csv")

#Make the date datetime
data['Date'] = pd.to_datetime(data['Date'], errors = 'coerce')
data['Date'] = data['Date'].dt.normalize()

#Group transactions by date
grouped = data.groupby('Date').size()


#plot findings
plt.bar(grouped.index ,grouped.values); plt.show()