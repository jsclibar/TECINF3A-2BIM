# Listas:

# somando valores

vendas = [100, 200, 50, 300, 150, 403] # lista de valores
print(sum(vendas)) # mostra na tela a soma dos valores na lista

# contando os valores:

print(len(vendas))

# maximo e minimo:

print(max(vendas))
print(min(vendas))

# selecionar elementos da lista

print(vendas[1])

# verificar se um item existe dentro da lista

lista_produtos = ['iphone', 'macbook', 'ipad', 'airpod']
procura_produto = input('Digite um produto: ').lower()

print(procura_produto in lista_produtos)

# adicionar um item na lista

lista_produtos.append('apple watch')
print(lista_produtos)

# remover um item da lista

lista_produtos.remove('apple watch')
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

# editar um item da lista

lista_produtos[0] = 'iPhone15'
print(lista_produtos)
vendas[0] = vendas[0] + 10
print(vendas)

# contar quantas vezes um item aparece na lista

print(lista_produtos.count('iPhone15'))

# ordenar uma lista

lista_produtos.sort()
print(lista_produtos)

lista_produtos.sort(reverse=True)
print(lista_produtos)   
