import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
#titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
#iris = sns.load_dataset("iris")
sns.stripplot(x="day", y="total_bill", data=tips)#x轴，y轴，数据（参数）  前面的是表示函数绘制散点图
#上面的可以注释掉
sns.regplot(x="total_bill", y="tip", data=tips)
#sns.pairplot(iris)
#print(tips.head())
plt.show()


#注意！该课程主要讲的是某种函数或者是方法，使用不同的函数和方法的时候可以画出不同的图
