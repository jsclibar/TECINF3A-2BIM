# Exemplo completo de como trabalhar com listas em Python

# 1. Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]
print("Lista inicial:", frutas)

# 2. Acessando elementos da lista
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# 3. Modificando um item da lista
frutas[1] = "morango"  # Substitui 'banana' por 'morango'
print("Após modificação:", frutas)

# 4. Adicionando elementos à lista
frutas.append("uva")  # Adiciona 'uva' ao final da lista
print("Após append:", frutas)

frutas.insert(1, "abacaxi")  # Insere 'abacaxi' na posição 1
print("Após insert:", frutas)

# 5. Removendo elementos da lista
frutas.remove("maçã")  # Remove 'maçã' da lista
print("Após remove:", frutas)

ultimo = frutas.pop()  # Remove o último item ('uva') e o armazena em uma variável
print("Item removido com pop:", ultimo)
print("Lista após pop:", frutas)

# 6. Iterando sobre a lista com um laço for
print("\nFrutas na lista:")
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

# 7. Descobrindo o tamanho da lista
tamanho = len(frutas)
print("\nTotal de frutas na lista:", tamanho)

# 8. Ordenando e invertendo uma lista de números
numeros = [3, 1, 4, 1, 5, 9]
print("\nLista de números original:", numeros)

numeros.sort()  # Ordena em ordem crescente
print("Ordenada:", numeros)

numeros.reverse()  # Inverte a ordem (agora em ordem decrescente)
print("Invertida:", numeros)

# 9. Verificando se um item está na lista
if "laranja" in frutas:
    print("\nTem laranja na lista!")
else:
    print("\nNão tem laranja na lista.")

# 10. Lista com tipos diferentes de dados (não recomendado em todos os casos)
dados = ["João", 25, 1.75, True]
print("\nLista com tipos mistos:", dados)