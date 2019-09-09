import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, hue="sex", palette="Set1", size=5, hue_kws={"marker":["^", "v"]})
g.map(plt.scatter, "total_bill", "tip", s=100, linewidth=.5)
g.add_legend()
plt.show()