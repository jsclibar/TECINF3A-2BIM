id_produto = ['ABC123', 'abd012', ' ABS111  ', 'AbB333'] # Lista com códigos de produtos
#texto = id_produto[3] # variável texto recebe o indice 3 da lista
#texto = texto.upper() # formata o texto recebido com letras maiusculas
#texto = texto.strip() # remove espaços antes e depois do texto
#print(texto)


# Transformando as ações acima em uma função:

def formata_id(texto): # nome da função e argumento de retorno
    texto = texto.upper() # tratamento dos dados...
    texto = texto.strip() # tratamento dos dados...
    return texto # função retorna a variável texto

# diferentes formas de usar a função em seu código...

print(formata_id('aBc123  '))
novo_texto = formata_id('abc123')
print(novo_texto)
novo_texto = formata_id(id_produto[3])
print(novo_texto)

# diferentes formas de usar a função em seu código...

for i, produto in enumerate(id_produto):
    id_produto[i] = formata_id(produto)
print(id_produto)