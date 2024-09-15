import pandas as pd
import numpy as np
import re

df = pd.read_csv('nba.csv')
#print(df.head(5))

"""
d_sum = df.describe(include = 'all')

#print(d_sum)

print(df.columns)

dfx = df.sort_values(by = 'Salary', ascending = False).head(10)

dfxx = dfx[['Name', 'Salary']]

print(dfxx)
"""

df_snt = df[['Team', 'Name', 'Salary']].sort_values(by = ['Team', 'Salary'], ascending = [True, False])
print(df_snt)

"""

df_avgsal = df.groupby('Team')['Salary'].mean().sort_values(ascending = False)
print(df_avgsal)

print()
df_totsal = df.groupby('Team')['Salary'].sum().sort_values(ascending = False)
print(df_totsal)
print()

df_highsal = df.groupby('Team')['Salary'].max().sort_values(ascending = False)
print(df_highsal)

print(df[['Name', 'Age', 'Salary']])

df_pos = df.groupby('Position')['Salary'].mean().sort_index(ascending = False)
print(df_pos)

print(df[['Name', 'Age', 'Salary']])

import matplotlib.pyplot as plt

# Plotting the salary distribution by position
plt.figure(figsize=(12, 8))
df.boxplot(column='Salary', by = 'Position', grid=False, showfliers=False)
plt.title('Salary Distribution by Position')
plt.suptitle('')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

"""

