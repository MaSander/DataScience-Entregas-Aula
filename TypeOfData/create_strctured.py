import pandas as pd

data_sheet1 = {
    "Name": ["Ana", "Carlos", "Jéssica", "Maria", "Vivian"],
    "Years": [23, 35, 25, 34, 42],
    "Cities": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

df_sheet1 = pd.DataFrame(data_sheet1)

print(data_sheet1)


print(df_sheet1)


with pd.ExcelWriter("dadosEstruturados.xlsx") as xlsx_writer:
    df_sheet1.to_excel(xlsx_writer, "aba 1")
