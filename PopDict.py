import pandas as pd

pop_dict = {'California' : 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135}

pop = pd.Series(pop_dict)
print(pop)

print(pop['California'])

x = pd.Series([2, 4, 6])
print(x)

