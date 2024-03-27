nome = 'José'
idade = 22

print('{} tem {} anos.'.format(nome, idade)) # forma mais antiga para manipular variáveis em saídas.
print(f'{nome} tem {idade} anos.') # forma mais nova para fazer a mesma coisa.

email = 'jose.cljr@senacsp.edu.br'

# transformar string em letras maiusculas:
print(email.upper())

email = 'JOSE.CLJR@SENACSP.EDU.BR'

# transformar string em letras minusculas:
print(email.lower())

# pesquisar na string a posição de elemento:

print(email.find('@'))

# retornar o tamanho da string:

print(len(email))

# selecionar um elemento dentro da string:

print(email[9]) # Se não for encontrado, será retornado -1
print(email[-2])

# selecionar um pedaço do texto:

print(email[:9]) # : significa do início até...
print(email[10:]) # aqui, : significa até o final...

# trocando um pedaço da string:

novo = email.replace("SENACSP.EDU.BR", "gmail.com")
print(novo)

# trocando um pedaço da string e gerando a saída toda em minusculo

novo = email.replace("SENACSP.EDU.BR", "gmail.com").lower()
print(novo)

# pegar apenas o servidor do e-mail:

posicao_arroba = novo.find('@') # armazena a posição do caractere @
servidor = novo[posicao_arroba:] # armazena da posição do @ até o fim da string
print(servidor)

# formatação de nomes: 

nome = 'cris mari'
print(nome.capitalize()) # somente primeira letra maiscula
print(nome.title()) # cada palavra com letra maiuscula

# separar primeiro e segundo nome:

posicao_espaco = nome.find(' ') # procura pela posição do espaço na string
primeiro_nome = nome[:posicao_espaco] # armazena do inico da string até a posição do espaço
segundo_nome = nome[posicao_espaco+1:] # armazena a posição do espaço + 1 até o fim
print(primeiro_nome.capitalize()) # exibe o primeiro nome deixando em maiusculo apenas a primeira letra
print(segundo_nome.capitalize()) # exibe o sobrenome deixando em maiusculo apenas a primeira letra

# Arredondando e trabalhando com valores numericos:

n = 42.3245678
p = 0.7134789
v = 30

print(round(n, 2)) # arredonta o valor de n com duas casas decimais
print(f'Porcentagem: {p:.1%}') # exibe o valor de p em porcentagem, com 1 casa decimal
print(f'Valor total é de R$ {v:.2f}') # formata o valor de v em formato float com duas casas decimais