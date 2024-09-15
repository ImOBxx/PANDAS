import pandas as pd
import numpy as np
import re

df = pd.read_csv('IMDb_Dataset_2.csv')
"""
#print(df.head(5))

x = np.array([df.columns])

#print(x)

#print(df[['Title', 'Year', 'IMDb Rating']].head(4))

#for index, rows in df.iterrows():
    #print(index, rows)

print(df.iloc[0:5, 0:3])

print(df.iloc[5, 4])

#print(df.describe())

x = df.sort_values('Title')

print(x.head(10))

f = df[['Title', 'Duration (minutes)']]

print(f.sort_values)

"""

df_2005 = df[df['Year'] == 2005]

#print(df_2005)

df_Rate = df[df['IMDb Rating'] == 8.8]

print(df_Rate)

df_star = df[(df['Star Cast'].str.contains('Leonardo')) & ((df['Year'] == 2012) | (df['Year'] == 2013) | (df['Year'] == 2014))]
print(df_star)

df_po = df[(df['Certificates'] == "R") & (df['Year'] >= 2000) & (df['Year'] <= 2010)]

print(df_po)

df['Max Duration'] = 500.0

print(df['Max Duration'])

print(df.head(5))

#df = df.drop(columns = ['Max Duration'])

#print(df.head(5))

df_leo = df[(df['Star Cast'].str.contains('Leonardo')) & (df['Genre'] == 'Biography')]

print(df_leo)



df_brad = df[(df['Star Cast'].str.contains('Brad')) & (df['Director'].str.contains('Quentin'))]

print(df_brad)

m = df_brad['Title']

print(m)


df_steven = df[(df['Director'].str.contains('Steven Spielberg')) & df['Poster-src'].str.contains('amazon')]
print(df_steven)


#print(df_steven[['Title', 'Director']].sort_values(df_steven['Title']))


df_chris = df[(df['Director'].str.contains('Christopher Nolan')) & (df['IMDb Rating'] >= 9.0)]

print(df_chris['Title'])

df_title = df[(df['Title'].str.contains('Love', flags= re.I)) & ((df['IMDb Rating'] > 7.0) | (df['MetaScore'] >= 75.0))]

print(df_title['Director'])

df_part = df[(df['Title'].str.endswith('2')) & (df['IMDb Rating'] >= 6.0)]

print(df_part)

df_time = df[(df['Duration (minutes)']) >= 230.0]

print(df_time)


if 'IMDb Rating' in df.columns:
    top_5 = df.sort_values(by = 'IMDb Rating', ascending= False).head(10)
    print(top_5)
else:
    print("NO MOVIES")

print(top_5['Title'])


