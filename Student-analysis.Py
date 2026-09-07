import pandas as pd
import matplotlib.pyplot as plt

data={'Name':['Sanjana','Ram','Anu'],'Marks':[85,78,92]}
df=pd.DataFrame(data)
print(df)
print("Average Marks:",df['Marks'].mean())
df.plot(x='Name',y='Marks',kind='bar',color='orange')
plt.title("Student Marks - Sanjana Project")
plt.show()
