# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# TRATAMENTO DOS DADOS

df = pd.read_excel('vendas.xlsx')

# 1.Padronizar a coluna 'categoria' para minúsculas.
df['categoria'] = df['categoria'].str.lower()

# 2.Remover registros onde a quantidade está ausente
df = df.dropna(subset=['quantidade'])

# 3. Remover espaços extras e padronizar com primeira letra maiúscula (estilo título)
df['produto'] = df['produto'].str.strip().str.title()

# 4. Garantir que a coluna data seja datetime
df['data'] = pd.to_datetime(df['data'])

# 5. Calcular valor unitário real das vendas válidas
df['valor_unitario'] = df.apply(lambda row: row['valor_venda'] / row['quantidade'] if row['quantidade'] > 0 else None, axis=1)

# 6. Calcular valor médio unitário por produto (sem considerar nulos)
# 7. Agrupar e calcular média
media_por_produto = df.groupby('produto')['valor_unitario'].mean()

# 8. Preencher valor_unitario ausente
df['valor_unitario'] = df.apply(lambda row: media_por_produto[row['produto']] if pd.isna(row['valor_unitario']) else row['valor_unitario'], axis=1)

# 9. Recalcular valor_venda
df['valor_venda'] = df['quantidade'] * df['valor_unitario']

# 10. Salvar o novo DataFrame limpo em um novo arquivo Excel
df.to_excel('vendas_tratadas.xlsx', index=False)

# ANALISE

# 1. Total de vendas por loja - Agrupar por loja e somar o valor total vendido
vendas_por_loja = df.groupby('loja')['valor_venda'].sum().sort_values(ascending=False)

# 2. Evolução mensal de vendas -  Identificar sazonalidades e picos mensais.
# 3. Agrupar por mês e somar vendas
df['mes'] = df['data'].dt.to_period('M')
vendas_mensais = df.groupby('mes')['valor_venda'].sum()

# 4. Produtos mais vendidos (por volume) Objetivo: saber o que mais sai no caixa.
produtos_mais_vendidos = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)

# 5. Comparação entre categorias. Objetivo: analisar quais categorias são mais lucrativas.
lucratividade_categorias = df.groupby('categoria')['valor_venda'].sum().sort_values(ascending=False)

# 6. Comparação entre lojas por categoria. Objetivo: avaliar se há especialização ou foco
# diferente entre as lojas, com base nas categorias que mais vendem.
vendas_loja_categoria = df.groupby(['loja', 'categoria'])['valor_venda'].sum().unstack()
