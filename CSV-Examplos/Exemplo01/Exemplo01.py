import pandas as pd # importa a biblioteca do pandas (lembre de instalar antes)

path = 'dados.csv' # a variável path armazena o caminho do arquivo.

file = pd.read_csv(path) # a variável file armazena o conteúdo do arquivo csv
#print(file.head()) # o comando .head() exibe por padrão as 5 primeiras linhas do arquivo
#print(file) # exibe o arquivo inteiro
#print(file['Cidade'].unique()) # mostra cada um dos valores da coluna cidade de forma exclusiva
#print(file['Cidade'].value_counts())

#maiores_30 = file[file['Idade'] > 30]
#print(maiores_30)

#ordenado = file.sort_values(by='Idade')
#print(ordenado)

# Selecionar uma coluna
#coluna_nomes = file['Nome']
#print(coluna_nomes)

# Selecionar múltiplas colunas
#colunas_selecionadas = file[['Nome', 'Cidade']]
#print(colunas_selecionadas)

# Selecionar uma linha por índice
#linha_0 = file.iloc[0]
#print(linha_0)

# Selecionar múltiplas linhas por índices
#linhas_0_5 = file.iloc[0:5]
#print(linhas_0_5)

# Renomear colunas
#renomeado = file.rename(columns={'Nome': 'Nome_Completo', 'Idade': 'Anos'})
#print(renomeado)

# Remover coluna 'Cidade'
#sem_cidade = file.drop(columns=['Cidade'])
#print(sem_cidade)

# Exibir uma amostra aleatória de 5 linhas
#amostra = file.sample(n=5)
#print(amostra)

# Converter strings para maiúsculas
#file['Nome'] = file['Nome'].str.upper()
#file['Cidade'] = file['Cidade'].str.upper()
#print(file.head())