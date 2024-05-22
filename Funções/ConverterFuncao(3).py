total = 1

num = int(input("Digite um número para ver seu fatorial: "))

fatorial = num

while num != 0:
    total = total * num
    num = num - 1

print(f"O fatorial de {fatorial} é {total}!")