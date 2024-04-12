palavra = input('Digite uma palavra: ').upper()
letra = input('Digite uma letra: ').upper()
c = 0

for l in palavra:
    print(f'No momento estamos testando a letra {l}')
    if letra == l:
        print(f'A letra {letra} foi encontrada')
        c += 1
print(f'Na palavra {palavra} existem {c} letra(s) {letra}')