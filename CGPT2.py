import pandas as pd

# Define the data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Age': [30, 25, 35, 40, 28],
    'Occupation': ['Engineer', 'Data Scientist', 'Teacher', 'Manager', 'Developer'],
    'Salary': [70000, 80000, 50000, 90000, 75000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a .csv file
df.to_csv('sample_data.csv', index=False)

# Read the .csv file into a DataFrame
df_read = pd.read_csv('sample_data.csv')

# Display the DataFrame
print(df_read)
