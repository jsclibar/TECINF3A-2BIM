x = int(input("Digite o valor inicial do intervalo: "))
y = int(input("Digite o valor final do intervalo: "))

numeros_pares = []
numeros_impares = []

for numero in range(x, y + 1):
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f"Números pares no intervalo de {x} a {y}: {numeros_pares}")
print(f"Números ímpares no intervalo de {x} a {y}: {numeros_impares}")