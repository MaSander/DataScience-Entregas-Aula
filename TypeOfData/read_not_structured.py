import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv("dadosNao.csv")

# Exibindo as primeiras linhas do DataFrame para verificar se foi carregado corretamente
print(df["Name"])
