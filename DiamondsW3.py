import pandas as pd
import numpy as np
import re

df = pd.read_csv('diamonds.csv')
print(df.head(5))

user = ['carat', 'cut', 'x', 'y', 'z']

print(df[user].head(6))

print(df['carat'])

