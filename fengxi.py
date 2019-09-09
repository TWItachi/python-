import matplotlib.pyplot as plt
import pandas as pd

unrate = pd.read_csv('UNRATE.csv')
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['DATE'], subset['VALUE'], c=colors[i])#三个参数代表横纵坐标，颜色

#print(help(plt))
plt.show()