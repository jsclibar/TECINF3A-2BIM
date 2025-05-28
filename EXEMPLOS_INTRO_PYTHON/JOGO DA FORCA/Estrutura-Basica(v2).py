palavra = 'senac'
letras_chute = ['a', 'c']
chances = 5
ganhou = False


while True:

    for letra in palavra:
        if letra.lower() in letras_chute:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f'Você tem {chances} tentativas')
    tentativa = input('Digite uma letra: ')
    letras_chute.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    print(f'Você tem ainda {chances} chances.')
 