import pandas as pd

ind = pd.Index([2, 3, 5, 7, 11])
print(ind)

print(ind[1])

print(ind[::2])

print(ind.size, ind.shape, ind.ndim, ind.dtype)

a = pd.Index([1, 3, 5, 7, 9])

b = pd.Index([2, 3, 5, 7 ,11])

print(a & b)

print()

print(a | b)

print()

print(a ^ b)

print()
