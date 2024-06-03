import pandas as pd # importa a biblioteca do pandas (lembre de instalar antes)

path = 'dados.csv' # a variável path armazena o caminho do arquivo.

file = pd.read_csv(path) # a variável file armazena o conteúdo do arquivo csv

media_idades_cidade = file.groupby('Cidade')['Idade'].mean()
print(media_idades_cidade)

# Salvar o DataFrame resultante em um novo arquivo CSV
media_idades_cidade.to_csv('media_idades_cidade.csv', header=True)
