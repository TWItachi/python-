import pandas as pd
import numpy as np

fandango = pd.read_csv("titanic_train.csv")
#print(type(fandango))
#print(fandango.head)
#print(fandango.shape)
#print(help(pandas.read_scv))
age = fandango["Age"]
#print(age.loc[0:10])
age_is_null = pd.isnull(age)
#print(age_is_null)
age_null_ture = age[age_is_null]
#print(age_null_ture)
print(len(age_null_ture))
