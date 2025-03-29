import pandas as pd  

# Lê o arquivo CSV com a codificação adequada
df = pd.read_csv('C:/teste/dados.csv', delimiter=';', encoding='ISO-8859-1', engine='python')

# Configurando o Pandas para exibir até 9999 linhas
pd.options.display.max_rows = 9999  

# Exibindo os dados completos
print(df.to_string())
