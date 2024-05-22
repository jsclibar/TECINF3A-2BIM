total = 0
num = int(input("Digite um número para analisar se ele é primo: "))
c = num
while c != 0:
    if num % c == 0:
        total += 1
    c -= 1
if total > 2:
    print("O número NÃO É PRIMO")
else:
    print("O número é PRIMO")