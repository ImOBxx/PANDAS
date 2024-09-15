import pandas as pd
import numpy as np
import re

df = pd.read_csv('MostStreamedSpotifySongs2024.csv',  encoding='latin1')
print(df)

df_ts = df[(df['Artist'].str.contains('Taylor Swift'))]

print(df_ts) 


