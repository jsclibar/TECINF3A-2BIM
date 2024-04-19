from random import randint # Importa a função randint da biblioteca random para geração de números aleatórios

n_aleatorio = randint(0, 2) # Gera tês possibilidades de valores aleatórios: 0, 1 e 2

print(f'O Computador escolheu o número {n_aleatorio}') #Mostra o valor "escolhido" pelo computador.

if n_aleatorio == 0:
    print('Computador escolheu papel!!')
elif n_aleatorio == 1:
    print('Computador escolheu pedra!!!')
else:
    print('Computador escolheu tesoura!!!')

'''
A partir desses exemplos de código, pense como desenvolver um jogo de "pedra, papel e tesoura" onde o usuário consiga disputar uma partida contra o computador. Seu jogo deverá atingir os seguintes objetivos:

1. Quando a partida se encerrar, perguntar se o jogador quer jogar novamente;
2. Tratar qualquer tipo de entrada inválida que "quebre" a execução do código;
3. Quando o jogador encerrar o jogo, mostrar um placar com as seguintes informações:
    A. Vitórias do Computador: X
    B. Vitórias do Usuário: Y
    C. Vencedor da Rodada

    Exemplos:

    O usuário venceu 4 das 10 partidas disputadas! Vitória do usuário!
    O computador venceu 6 das 7 partidas disputadas! Vitória do computador!
    Computador e usuário empataram!!!

'''

