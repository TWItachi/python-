import pandas as pd
from numpy import arange
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
fig, ax = plt.subplots()
ax.scatter(reviews['Fandango_Ratingvalue'], reviews['RT_user_norm'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()