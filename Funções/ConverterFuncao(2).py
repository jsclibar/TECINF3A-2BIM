potencia=0
ndec=0
i=0

nb = input("Digite um número binário: ")

for c in nb[::-1]:  #O laço irá se repetir até que a variável c assuma cada um dos digitos do número binário de trás para frente.
   #print(f'No momento o digito {c} está sendo calculado:')  #Apenas para entendimento do que acontece no algoritmo
    i = (2**potencia)*int(c)  #Armazena na variável i o valor de 2 ^ a potencia (começa em 0) multiplicado pelo digito armazenado em "c".
    #print(f'2 ^ {potencia} * {c} é igual a {i}')  #Apenas para entendimento do que acontece no algoritmo
    potencia = potencia + 1  #Acrescenta 1 em potencia para a a próxima repetição.
    ndec = ndec + i  #Armazena na variavel ndec seu valor anterior + 2 ^ potencia * digito binário.
print(f'O número binário {nb} equivale a {ndec} em decimal')