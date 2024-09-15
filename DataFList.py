import pandas as pd
import numpy as np
import re

data = {'X' : [1, 2, 3, 4], 'Y' : [5, 6, 7, 8]}

df = pd.DataFrame(data)

print(df)

print(df.head(3))

print(df['X'])

fd = df[df['X'] > 2]

print(df)

df['Z'] = df['X'] + df['Y']

print(df['Z'])

print(df)

df.drop(columns= ['Z'], inplace= True)

print(df)

print()

df.sort_values(by = 'X', inplace= True)

print(df)

print()

gdf = df.groupby('X').mean()

print(gdf)



