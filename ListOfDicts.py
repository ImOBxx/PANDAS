import pandas as pd

data = [{'a' : i, 'b' : 2 * i} for i in range(3)]

print(pd.DataFrame(data))