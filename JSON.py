import json

# Sample data
data = {
    "people": [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"}
    ]
}

# Write JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
