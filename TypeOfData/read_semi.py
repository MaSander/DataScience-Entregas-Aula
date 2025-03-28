import pandas as pd

# Read the JSON file
data = pd.read_json("dadosSemi.json")

# Log the data to the console
print(data.head(2))
