nd=int(input('Digite um número decimal inteiro: '))
nbin=''

while nd > 0:
    resto = nd % 2
    #print(f'A parte inteira da divisão é {aux}')
    nd=nd//2
    nbin=nbin+str(resto)
    #print(f'O resto da divisão é {resto}')
    #print(f'Construção da saída: {nbin}')

print(f'Resultado: {nbin[::-1]}')