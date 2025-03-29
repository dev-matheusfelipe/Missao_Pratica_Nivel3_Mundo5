import pandas as pd

# Caminho para o arquivo CSV
arquivo_csv = r"C:\teste\dados.csv"

# Lendo o arquivo CSV com o delimitador correto e encoding adequado
df = pd.read_csv(arquivo_csv, delimiter=";", encoding="ISO-8859-1")

# Exibir as primeiras linhas do DataFrame
print("Primeiras 5 linhas:")
print(df.head())

# Exibir as últimas linhas
print("\nÚltimas 5 linhas:")
print(df.tail())

# Informações sobre o DataFrame
print("\nInformações do DataFrame:")
print(df.info())
