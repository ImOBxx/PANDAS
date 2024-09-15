import pandas as pd

cal = {"day1" : 420, "day2" : 380, "day3:" : 390}

myvar = pd.Series(cal, index = ["day1", "day2"])

print(myvar)

