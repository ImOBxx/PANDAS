import pandas as pd
import numpy as np

A = np.random.randint(10, size = (3, 4))
print(A)

x = A - A[0]
print(x)

vals1 = np.array([1, np.nan, 3, 4])
print(vals1)

print(np.nansum(vals1))

ser = pd.Series([1, np.nan, 2, None, 3])

print(ser)

print()

print(ser.isnull())

print()

print(ser.notnull())

print()

print(ser[ser.notnull()])

print()

print(ser.dropna())

print()

print(ser)

