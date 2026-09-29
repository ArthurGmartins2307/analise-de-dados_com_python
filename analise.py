import pandas as pd

df = pd.read_csv("vendas.csv")

# Quantas linhas existem?

linhas = len(df)
print(linhas)
#Quantas colunas existem?

qnt_colunas = len(df.columns)
print(qnt_colunas)
#Quais são os nomes das colunas?

colunas = df.columns
print(colunas)
#Quais são os tipos de dados de cada coluna?

tipo_colunas = df.dtypes
print(tipo_colunas)

#Mostre:
# os 5 primeiros registros;
print(df.head(5))

# os 10 primeiros registros;
print(df.head(10))

# os 5 últimos registros.
print(df.tail(5))

# Descubra quais produtos existem no dataset.
print(df['produto'].tolist())

# Descubra todas as cidades presentes nos dados.
cidade_unica = df['cidade'].unique()
print(cidade_unica)

# Quantas cidades diferentes existem?
contagem_cidades = df['cidade'].nunique()
print(contagem_cidades)