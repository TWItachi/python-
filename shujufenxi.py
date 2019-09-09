import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#引用
unrate = pd.read_csv('UNRATE.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
fig = plt.figure(figsize=(3, 3))
#first_twelve = unrate[0:12]
#plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(np.random.randint(1, 5, 5), np.arange(5))#绘制折线图
ax2.plot(np.arange(10)*3), np.arange(10)
plt.show()
#print(unrate.head(12))
