import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

#方法一
#sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)#jitter用于分散数据集
#还有另一种方法

#法二
#sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)

#统计离群点，远远超出正常水平
#sns.boxplot(x="day", y="total_bill", data=tips)

#小提琴
#sns.violinplot(x="total_bill", y="day", hue="time", data=tips)
#不同性别的影响
sns.violinplot(x="total_bill", y="day", hue="sex", data=tips, split=True)
plt.show()