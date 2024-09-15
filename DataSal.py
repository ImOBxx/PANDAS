import numpy as np
import pandas as pd
import re

df = pd.read_csv('Dataset salary 2024.csv')
print(df)

"""
df_sal = df[(df['job_title'].str.contains('AI'))]

df_fsal = df_sal[['salary_in_usd','salary_currency', 'employment_type']]

print(df_fsal)

df_sal_grouped = df_sal.groupby('experience_level')['work_year'].mean()

print(df_sal_grouped)

print(df.describe())
"""

f_sald = df[['job_title', 'salary_in_usd']].sort_values(by='salary_in_usd', ascending=False).drop_duplicates(subset=['job_title'])

print(f_sald.head())



