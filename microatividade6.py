import pandas as pd

# Lê o arquivo CSV com a codificação adequada
df = pd.read_csv('C:/teste/dados.csv', delimiter=';', encoding='ISO-8859-1', engine='python')

# Passo 2: Verificar as colunas do DataFrame
print("🔹 Colunas do DataFrame:", df.columns)

# Passo 3: Criar uma cópia do DataFrame
df_limpo = df.copy()

# Passo 4: Verificar e tratar valores nulos na coluna 'Quantity'
if 'Quantity' in df_limpo.columns:
    df_limpo['Quantity'] = df_limpo['Quantity'].fillna(0)  # Substitui nulos na coluna 'Quantity' por 0
    print("🔹 Dados após substituição na coluna 'Quantity':")
    print(df_limpo.head())  # Exibe as primeiras 5 linhas para verificar
else:
    print("🔹 A coluna 'Quantity' não foi encontrada no DataFrame.")

# Passo 5: Verificar e tratar valores nulos na coluna 'InvoiceDate'
if 'InvoiceDate' in df_limpo.columns:
    df_limpo['InvoiceDate'] = df_limpo['InvoiceDate'].fillna('1900/01/01')  # Substitui nulos na coluna 'InvoiceDate'
    print("🔹 Dados após substituição na coluna 'InvoiceDate':")
    print(df_limpo.head())  # Exibe as primeiras 5 linhas para verificar
else:
    print("🔹 A coluna 'InvoiceDate' não foi encontrada no DataFrame.")

# Passo 6: Transformar a coluna 'InvoiceDate' em datetime
if 'InvoiceDate' in df_limpo.columns:
    # Substitui valores inválidos por NaT (Not a Time) para evitar erro na conversão para datetime
    df_limpo['InvoiceDate'] = pd.to_datetime(df_limpo['InvoiceDate'], errors='coerce')
    print("🔹 Dados após transformação da coluna 'InvoiceDate' para datetime:")
    print(df_limpo.head())  # Exibe as primeiras 5 linhas para verificar
else:
    print("🔹 A coluna 'InvoiceDate' não foi encontrada no DataFrame.")

# Passo 7: Remover registros com valores nulos na coluna 'InvoiceDate'
df_limpo = df_limpo.dropna(subset=['InvoiceDate'])
print("🔹 Dados após remoção de valores nulos na coluna 'InvoiceDate':")
print(df_limpo.head())  # Exibe as primeiras 5 linhas para verificar
