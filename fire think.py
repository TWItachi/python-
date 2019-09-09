import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#例题一
#np.random.seed(0)
#sns.set()
#uniform_data = np.random.rand(3, 3)#随机
#print(uniform_data)#打印
#heatmap = sns.heatmap(uniform_data) #绘图

#例题二
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
#print(flights.head())
ax = sns.heatmap(flights, linewidths=.5)


plt.show()