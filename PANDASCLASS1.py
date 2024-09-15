import pandas as pd
import numpy as np

data = {
    ('California', 2000): 33871648,
    ('California', 2010): 37253956,
    ('Texas', 2000): 20851820,
    ('Texas', 2010): 25145561,
    ('New York', 2000): 18976457,
    ('New York', 2010): 19378102
}

ser = pd.Series(data)

print(data)
print(ser)

df = pd.DataFrame(ser)
print(df)

print(df.index)

df.index.names = ["State", "Year"]
print(df)

idx = pd.MultiIndex.from_product([[2013,2014],[1,2]],names=["Year","Visit"])
print(idx)

column_idx =pd.MultiIndex.from_product([["Bob","Guido","Sue"],["HR","Temp"]],names=["Subject","Type"])

data=np.round(np.random.randn(4,6),1)

print(data)

x = data[:,::2]

x *= 10

print(x)

x += 37

print(x)

health_data = pd.DataFrame(data, index = idx, columns = column_idx)

print(health_data)

print(health_data["Sue"])

index = pd.MultiIndex.from_tuples([('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000), ('Texas', 2010)], names=['state', 'year'])

print(index)

data = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]

print(data)

pop = pd.Series(data, index=index, dtype=int)

print(pop)

print(pop["California"])

print(pop["California", 2000])

print(pop["California":"New York"])


