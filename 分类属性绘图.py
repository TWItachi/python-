import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
titanic = sns.load_dataset("titanic")
#下面是表示泰坦尼克舱位与获救几率的关系
#x轴表示性别，y轴表示获救几率，hue表示舱位
#sns.barplot(x="sex", y="survived", hue="class", data=titanic)
#折线图更好描述差异性
sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()