#color_oalette()传入颜色
#set_palette()设置颜色
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats, integrate
#sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distrbutions")))
#x = np.random.normal(size = 100)
#sns.distplot(x, kde = False)
mean, cov = [0, 1], [(1, .5), (.5, 1)]      #mean为均值，cov协方差
#data = np.random.multivariate_normal(mean, cov, 200)    #生成200组数据
#df = pd.DataFrame(data, columns=["x", "y"])    #数据类型为panda的dataframe
#df  #输出

#sns.palplot(sns.color_palette("hls", 8))#显示颜色
x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k")

#iris = sns.load_dataset("iris")    #传入数据
#sns.pairplot(iris)
plt.show()