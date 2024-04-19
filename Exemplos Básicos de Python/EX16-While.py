r = 'S'
soma = 0
contador = 0
while r == 'S':
    n = int(input('Digite um Valor: '))
    r = input('Deseja continuar? [S/N] ').upper()
    soma = soma + n
    contador = contador + 1
print(f'A soma dos {contador} numeros digitados é {soma}')
print('FIM!')