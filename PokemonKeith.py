import numpy as np
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.head())

#Prints Columns
#print(df.columns)

#print(df[['Name', 'Type 1', 'HP']])

#print(df.head(4))

#print(df.iloc[0:1])
#print(df.iloc[2, 1])


#for index, row in df.iterrows():
    #print(index, row['Name'])
#print(df.loc[df['Type 1'] == "Grass"])

#print(df.iloc[2, 1])

#print(df.describe())

#print(df.sort_values(['Type', 'HP'], ascending = [1.0]))

#df.head(5)


#print(df.head(5))

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#print(df.drop(column = ['Total']))

#df['Total'] = df.iloc[:, 4:9].sum(axis = 1)

##print(df['Total'])

#print(df.head(5))

#cols = list(df.columns.values)
#x = np.array((cols))
#print(x)
#print(cols)
#print(df[['Total', 'HP', 'Defense']])

#dfx = df[cols[0:4] + [cols[-1]] + cols[4:12]]

#print(dfx)

"""
x = df.to_csv('modified.xlsx', index = False)
print(x)

f = df.to_csv('modified.txt', index = False)

matching_rows = df[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & df['HP'] > 70]
print(matching_rows)

new_df = matching_rows.reset_index(drop = True)

print(new_df)
"""

#x = df.loc[~df['Name'].str.contains('Mega')]

#print(x)

#import re

#x = df.loc[df['Name'].str.contains(r'^pi[a-z]*', flags=re.IGNORECASE, regex= True)]

#print(x)
"""
s = df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True

df = pd.read_csv('modified.csv')

d = df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

print(d)

df = pd.read_csv('modified.csv')
"""

"""
df = pd.read_csv('pokemon_data.csv')

print(df)

a = df.groupby(['Type 1']).mean()

print(a)

"""

df ['count'] = 1

q = df.groupby(['Type 1', 'Type 2'].count()['count'])

print(q)

x = pd.read_csv('filtered_csv', chunksize = 5)

print(x)

