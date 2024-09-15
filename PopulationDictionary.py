import pandas as pd

pop_dict = pd.Series({
    'California' : 38334521,
    'Florida' : 195552869,
    'Illinois' : 12887904675,
    'New York' : 19651127,
    'Texas' : 23448194
})

df = pd.DataFrame(pop_dict, columns = ['Population'])

print(df)