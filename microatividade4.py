import pandas as pd  

# Lê o arquivo CSV com a codificação adequada
df = pd.read_csv('C:/teste/dados.csv', delimiter=';', encoding='ISO-8859-1', engine='python')

# Exibindo as primeiras 10 linhas
print("🔹 Primeiras 10 linhas:")
print(df.head(10))

# Exibindo as últimas 10 linhas
print("\n🔹 Últimas 10 linhas:")
print(df.tail(10))
