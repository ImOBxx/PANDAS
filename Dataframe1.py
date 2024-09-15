import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.dtype)

print(df.columns)
print(df.iloc[1])
print(df.loc[2])
print(df.index)