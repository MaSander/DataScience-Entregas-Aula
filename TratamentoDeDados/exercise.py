import pandas as pd
import numpy as np

# 1. Carregar um arquivo e exibir as primeiras 5 linhas
print("Exercício 1: Carregar um arquivo e exibir as primeiras 5 linhas")
# Criando um DataFrame para exemplificar
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5, 6, 7],
    'B': [10, np.nan, 30, 40, 50, np.nan, 70],
    'C': ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', np.nan, 'Bahia', 'Paraná', 'Rio Grande do Sul'],
    'D': ['  Valor1  ', '  Valor2', 'Valor3  ', '  Valor4  ', 'Valor5', '  Valor6', 'Valor7  ']
})
# Salvando o DataFrame em um arquivo CSV para poder carregá-lo
df.to_csv('exemplo.csv', index=False)

# Carregando o arquivo e exibindo as primeiras 5 linhas
df_carregado = pd.read_csv('exemplo.csv')
print(df_carregado.head(5))
print("\n")

# 2. Verificar se há valores NaN nas colunas do DataFrame
print("Exercício 2: Verificar se há valores NaN nas colunas do DataFrame")
print(df.isna().sum())
print("\n")

# 3. Substituir os valores NaN de uma coluna por 0
print("Exercício 3: Substituir os valores NaN de uma coluna por 0")
df_3 = df.copy()
df_3['A'] = df_3['A'].fillna(0)
print(df_3)
print("\n")

# 4. Substituir os valores NaN de uma coluna por um valor específico (média)
print("Exercício 4: Substituir os valores NaN de uma coluna por um valor específico (média)")
df_4 = df.copy()
df_4['B'] = df_4['B'].fillna(df_4['B'].mean())
print(df_4)
print("\n")

# 5. Remover todas as linhas que contêm valores NaN em qualquer coluna
print("Exercício 5: Remover todas as linhas que contêm valores NaN em qualquer coluna")
df_5 = df.copy()
df_5 = df_5.dropna()
print(df_5)
print("\n")

# 6. Remover todas as linhas que contêm valores NaN em uma coluna específica
print("Exercício 6: Remover todas as linhas que contêm valores NaN em uma coluna específica")
df_6 = df.copy()
df_6 = df_6.dropna(subset=['C'])
print(df_6)
print("\n")

# 7. Substituir valores NaN de uma coluna com a mediana dessa coluna
print("Exercício 7: Substituir valores NaN de uma coluna com a mediana dessa coluna")
df_7 = df.copy()
df_7['A'] = df_7['A'].fillna(df_7['A'].median())
print(df_7)
print("\n")

# 8. Substituir valores NaN de uma coluna com o valor de uma outra coluna
print("Exercício 8: Substituir valores NaN de uma coluna com o valor de uma outra coluna")
df_8 = df.copy()
# Vamos criar uma coluna E como backup da coluna A
df_8['E'] = df_8['A']
df_8.loc[df_8['B'].isna(), 'B'] = df_8.loc[df_8['B'].isna(), 'A']
print(df_8)
print("\n")

# 9. Preencher valores NaN com o valor anterior (método de "forward fill")
print("Exercício 9: Preencher valores NaN com o valor anterior (método de forward fill)")
df_9 = df.copy()
df_9 = df_9.fillna(method='ffill')
print(df_9)
print("\n")

# 10. Preencher valores NaN com o valor posterior (método de "backward fill")
print("Exercício 10: Preencher valores NaN com o valor posterior (método de backward fill)")
df_10 = df.copy()
df_10 = df_10.fillna(method='bfill')
print(df_10)
print("\n")

# 11. Alterar todos os valores de uma coluna para maiúsculas
print("Exercício 11: Alterar todos os valores de uma coluna para maiúsculas")
df_11 = df.copy()
df_11['C'] = df_11['C'].str.upper()
print(df_11)
print("\n")

# 12. Alterar todos os valores de uma coluna para minúsculas
print("Exercício 12: Alterar todos os valores de uma coluna para minúsculas")
df_12 = df.copy()
df_12['C'] = df_12['C'].str.lower()
print(df_12)
print("\n")

# 13. Remover espaços em branco à esquerda e à direita em uma coluna
print("Exercício 13: Remover espaços em branco à esquerda e à direita em uma coluna")
df_13 = df.copy()
df_13['D'] = df_13['D'].str.strip()
print(df_13)
print("\n")

# 14. Substituir valores de uma coluna com base em um dicionário de mapeamento
print("Exercício 14: Substituir valores de uma coluna com base em um dicionário de mapeamento")
df_14 = df.copy()
mapeamento = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Minas Gerais': 'MG',
    'Bahia': 'BA',
    'Paraná': 'PR',
    'Rio Grande do Sul': 'RS'
}
df_14['C'] = df_14['C'].map(mapeamento).fillna(df_14['C'])
print(df_14)
print("\n")

# 15. Identificar e remover valores duplicados de um DataFrame
print("Exercício 15: Identificar e remover valores duplicados de um DataFrame")
# Criando um DataFrame com valores duplicados
df_15 = pd.DataFrame({
    'A': [1, 2, 2, 3, 3, 4],
    'B': [10, 20, 20, 30, 30, 40]
})
print("DataFrame com duplicatas:")
print(df_15)
print("\nIdentificando duplicatas:")
print(df_15.duplicated())
print("\nRemovendo duplicatas:")
df_15_sem_duplicatas = df_15.drop_duplicates()
print(df_15_sem_duplicatas)
