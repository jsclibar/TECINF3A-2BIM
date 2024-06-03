import pandas as pd

# 1. Ler o arquivo CSV
df = pd.read_csv('dados.csv')

# 2. Agrupar registros por cidade
grupos_por_cidade = df.groupby('Cidade')

# Exibir registros agrupados por cidade
for cidade, grupo in grupos_por_cidade:
    print(f"Cidade: {cidade}")
    print(grupo)
    print("\n")