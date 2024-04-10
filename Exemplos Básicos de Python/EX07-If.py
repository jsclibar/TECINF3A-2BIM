lista = ['airpods', 'macbook', 'iphone', 'ipad']
busca = input('Digite um produto: ').lower()

if busca in lista: # Se o produto digitado estiver dentro (in) da lista
    print('Produto em estoque!')
else:
    print('Produto indisponivel')

print('FIM')
