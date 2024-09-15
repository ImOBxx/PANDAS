import pandas as pd
import numpy as np
from scipy import stats
import re

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
"""
print(df.head(5))

print(df.describe())

df_sl = np.array(df['Sleep Duration'])
print(df_sl)

md = stats.mode(df_sl)

print("Min. Duration: ", np.max(df_sl))
print("Max. Duration: ", np.min(df_sl))
print("Median Duration: ", np.median(df_sl))
print("Average Duration: ", np.average(df_sl))
print("25th Percentile: ", np.percentile(df_sl, 25))
print("50th Percentile: ", np.percentile(df_sl, 50))
print("75th Percentile: ", np.percentile(df_sl, 75))
print("Mean Value: ", np.mean(df_sl))
print("Standard Deviation: ", np.std(df_sl))
print("Variance: ", np.var(df_sl))
print("Sum: ", np.sum(df_sl))
print("Product: ", np.sum(df_sl))
print("Cumulative Sum: ", np.cumsum(df_sl))
print("Cumulative Product: ", np.cumprod(df_sl))
print("Correlation Coefficient: ", np.corrcoef(df_sl))
print("Covariance Matrix: ", np.cov(df_sl))
"""

"""
df_sl = df[(df['Sleep Duration'] < 6.0) & (df['Quality of Sleep'] < 6)]
print(df_sl[['Occupation', 'Sleep Disorder']])

#for index, rows in df_sl.iterrows():

#    print(index, rows)

df_sa = df[(df['Gender'].str.contains('Female')) & (df['Occupation'] == 'Sales Representative')]

print(df_sa)

dfs = np.array(df.columns)
print(dfs)

x = df['Sleep Duration']
print(x)

dfx = np.array(x, dtype = 'int8')
print(dfx)
q = np.count_nonzero(dfx)
print(q)

c = dfx[dfx < 7]
d = np.count_nonzero(c)
print(d)

df_st = df[df['Daily Steps'] > 4000].sort_values(by = 'Daily Steps', ascending= True)

print(df_st['Daily Steps'])

y = np.array(df_st['Daily Steps'])
print(y)

df_avg = df['Daily Steps'].mean()
print("Mean Steps: ", round(df_avg, 2))

df_fst = df[(df['Daily Steps'] & (df['Gender'].str.contains('Female')))]
print(df_fst)

print(df[['Daily Steps', 'Gender']])

df_f = df[df['Gender'] == 'Female']

avg = df_f['Daily Steps'].mean()

print(avg)


df_occ = df.groupby('Occupation')['Daily Steps'].mean().sort_values(ascending = False)

print(round(df_occ, 4))

"""

df_age = df.groupby('Age')['Daily Steps'].mean().sort_values(ascending = False)

print(df_age)

df_gs = df['Sleep Duration'] >= 7
df_hs = df['Stress Level'] >= 7

df_ss = df[df_gs & df_hs]

df_foi = df_ss[['Occupation', 'Sleep Duration', 'Stress Level']]
print(df_foi)

df_avgs = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending = False)
print(round(df_avgs, 2))

df_sle = df.groupby('Occupation')['Stress Level'].mean().sort_values(ascending = False) 

print(round(df_sle))

df_sq = df.groupby('Occupation')['Quality of Sleep'].mean().sort_values(ascending = False)

print(round(df_sq, 2))

df_gs = df.groupby('Gender')['Stress Level'].mean()

print(df_gs)

df_sd = df.groupby('Occupation')['Stress Level'].mean().sort_values(ascending = False)

print(round(df_sd, 2))

df_pa = df.groupby('Gender')['Physical Activity Level'].mean()
print(round(df_pa, 2))

df_gsd = df.groupby('Gender')['Sleep Duration'].mean()

print(round(df_gsd, 2))

corr_ss = df['Sleep Duration'].corr(df['Stress Level'])

print("Correlation Coefficient Between Stress levels & Sleep: ", corr_ss)

df_sag = df.groupby('Age')['Sleep Duration'].mean().sort_values(ascending = True)

print(df_sag)
 
df_sdpa = df.groupby('Physical Activity Level')['Sleep Duration'].mean().sort_values(ascending = False)

print(df_sdpa)

df_hr = df.groupby('Occupation')['Heart Rate'].mean().sort_values(ascending = False)

print(round(df_hr, 2))

df_gpa = df.groupby('Gender')['Physical Activity Level'].mean().sort_values(ascending = False)

print(round(df_gpa))

df_lsl = df.groupby('Occupation')['Stress Level'].mean().sort_values(ascending = True)

print(round(df_lsl, 2).head(5))

df_paa = df.groupby('Age')['Physical Activity Level'].mean().sort_values(ascending = True)

print(round(df_paa))

df_bmi = df.groupby('BMI Category')['Age'].mean().sort_values(ascending = True)

print(round(df_bmi))

corras = df['Age'].corr(df['Stress Level'])
print(corras)

df_grouped = df.groupby(['Age', 'Gender'])['Daily Steps'].mean().reset_index()

print(df_grouped)

dfq = df.loc[df['Sleep Disorder'] == 'Sleep Apnea', 'Sleep Disorder'] = 'Sleep AP'

print(dfq)



