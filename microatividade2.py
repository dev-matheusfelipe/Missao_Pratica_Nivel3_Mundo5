import pandas as pd

# Lê o arquivo CSV com a codificação adequada
df = pd.read_csv('C:/teste/dados.csv', delimiter=';', encoding='ISO-8859-1', engine='python')

# Verificando as colunas do DataFrame
print("Colunas:", df.columns)

# Criando o subconjunto de dados
subconjunto_df = df[['InvoiceNo', 'StockCode', 'Description']]  # Substitua com as colunas existentes no seu DataFrame

# Exibindo o subconjunto
print(subconjunto_df)
