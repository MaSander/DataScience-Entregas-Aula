from test.libregrtest.runtests import JsonFile
import pandas as pd

data_json = {
    "Name": ["Ana", "Carlos", "Jéssica", "Maria", "Vivian"],
    "Years": [23, 35, 25, 34, 42],
    "Cities": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

df_json = pd.DataFrame(data_json)

df_json.to_json("dadosSemi.json", orient="records", lines=False, force_ascii=False)
