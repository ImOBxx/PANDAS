import numpy as np
import pandas as pd
import re

url = '/Users/abhishekbanerjee/PANDAS/chipotle.tsv'
df = pd.read_csv(url, sep = '\t')

"""
print(df)

print(df.head(10))

print(df.head(5))

print(df.shape[0])

print(df.info())

print(df.shape[1])

print(df.columns)

print(df.index)
"""

c = df.groupby('item_name')['quantity'].

print(c.head(5))

