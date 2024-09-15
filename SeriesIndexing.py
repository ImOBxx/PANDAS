import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index = ['a', 'b', 'c', 'd'])

print(data)

print()

print(data['a' : 'c'])

data['d'] = 1.25

print(data['a':'d'])

print(data(data.T))