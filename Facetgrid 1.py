import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord, "axis_grids")))
tips = sns.load_dataset("tips")
print(tips)#查看信息

#g = sns.FacetGrid(tips, col="time")#绘制坐标，后引用绘图
#举个例子，吸烟和性别的关系
#g.map(plt.hist, "tip")#午餐，晚餐，不打清楚

#g = sns.FacetGrid(tips, col="sex", hue="smoker")
#g.map(plt.scatter, "total_bill", "tip", alpha=0.07)#散点图，scatter，alpha透明度参数
#g.add_legend();#类别add


#浮点，fit_reg->回归线
g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
g.map(sns.regplot, "size", "total_bill", color=".1", fit_reg=True, x_jitter=.1)
plt.show()