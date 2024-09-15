import pandas as pd

print()
mydataset = {
    'CARS' : ["BMW", "Volvo", "Ford"], 'PASSING': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print()