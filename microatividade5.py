import pandas as pd  

# Lê o arquivo CSV com a codificação adequada
df = pd.read_csv('C:/teste/dados.csv', delimiter=';', encoding='ISO-8859-1', engine='python')

# Exibir informações gerais sobre o conjunto de dados
print("🔹 Informações gerais sobre o DataFrame:")
print(df.info())  # Exibe colunas, tipos de dados, valores não nulos e memória usada

# Exibir o total de linhas e colunas
print("\n🔹 Total de linhas e colunas:")
print(df.shape)  # Retorna (número de linhas, número de colunas)

# Exibir a quantidade de valores nulos por coluna
print("\n🔹 Quantidade de valores nulos por coluna:")
print(df.isnull().sum())  # Conta quantos valores nulos existem em cada coluna

# Exibir a memória utilizada pelo DataFrame
print("\n🔹 Memória utilizada pelo conjunto de dados:")
print(df.memory_usage(deep=True))  # Exibe a memória usada por cada coluna
