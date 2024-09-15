import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.loc[[0, 1]])

df.to_csv('data2.csv', index=False)


