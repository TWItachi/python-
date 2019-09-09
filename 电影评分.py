import pandas as pd
from numpy import arange
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
#title = ['FILM','RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']
num_col = ['RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']
#norm_reviews = reviews[title]
#print(norm_reviews)
bar_heights = reviews.loc[0, num_col].values
print(bar_heights)
bar_positions = arange(5) + 0.75
print(bar_positions)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.3)
plt.show()