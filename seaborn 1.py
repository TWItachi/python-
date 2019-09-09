import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


#sinplot()
#sns.set()
sns.set_style("dark")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data)
plt.show()
#五种默认风格darkgrid whitegrid dark white ticks