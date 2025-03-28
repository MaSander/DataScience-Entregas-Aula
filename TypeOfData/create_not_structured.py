import pandas as pd

data_csv = {
    "Name": ["Ana", "Carlos", "Jéssica", "Maria", "Vivian"],
    "Years": [23, 35, 25, 34, 42],
    "Cities": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

df_csv = pd.DataFrame(data_csv)

df_csv.to_csv("dadosNao.csv", index=False)
