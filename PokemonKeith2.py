import pandas as pd
import numpy as np

df = pd.read_csv('pokemon_data.csv')

#print(df.head())

#print(df.columns)

x = np.array(df.columns)

#print(x)

#print(df[['Name', 'Type 1', 'HP']].head(40))

#print(df.head(4))

#print(df.iloc[0:1])

#print(df.iloc[0, 1])

#for index, row in df.iterrows():
    #print(index, row['Type 1'])

#print(df.loc[df['Speed'] == 100])

#print(df.iloc[2, 1])

#print(df.describe()) #High Level Mean, Std. Deviation

#x = df.sort_values('Type 1', 'HP', ascending = [False, False])

#print(x)

#Making Chenges To the Data



#ADD AND DELETE COLUMN

""""
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#print(df['Total'])

#print(df.head(5))

df = df.drop(columns = ['Total'])

print(df.head(5))

df['Total'] = df.iloc[:, 4:10].sum(axis = 1)

print(df.head(5))

"""

"""
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)

print(df.head(5))

cols = list(df.columns)

print(cols)

dfx = df[cols[0:4] + [cols[-1]] + cols[4:13]]

print(df)



df.to_csv('modified.csv', index = False)

print(df)

"""
df.to_excel('modified.csv', index = False)

print(df)

df.to_csv('modified.csv', index = False, sep = '\t')

print(df)
"""

"""
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

print(df.head(5))

new_df = new_df.to_csv('filtered.csv')

new_df_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

# Reset the index of the filtered DataFrame in place
new_df_df.reset_index(drop=True, inplace=True)

print(new_df_df)

df = df.loc[df['Name'].str.contains('Mega')] # ~ for Not Operator

print(df)

import re

df = df.loc[df['Name'].str.contains('pi[a-z]*',  flags = re.I ,regex = True)]

print()
#print(df)
print()


#x = df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

#print(x)

for df in pd.read_csv('pokemon_data.csv', chunksize = 5):
      print(df)

