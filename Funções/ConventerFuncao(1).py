contador=0

palavra = input('Digite uma palavra qualquer: ').lower()
letra = input('Digite a letra que deseja procurar na palavra: ').lower()

for c in palavra:
    if c== letra:
        contador=contador+1

print(f'Na palavra "{palavra} existe(m) {contador} letras "{letra}"')

