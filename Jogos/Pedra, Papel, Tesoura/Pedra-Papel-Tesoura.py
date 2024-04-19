from random import randint # Importa a funcao randint da biblioteca random

# Repetição que comporta toda a estrutura do jogo, a ideia é poder iniciar as partidas várias vezes,
# perguntando no final se o usuário quer jogar de novo ou não
while True: 
    itens = ['pedra', 'papel', 'tesoura'] # Lista que guarda as opções possíveis! posição 0 = pedra, 1 = papel, 2 = tesoura
    computador = randint(0, 2) # Usa a funcão randint para gerar um número aletório entre 0 e 2 (0 = pedra, 1 = papel e 2 = tesoura)

    # --- Mostra na tela as opções possíveis para o jogador ---
    print('''Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
    # --- Fim das opções

    jogador = int(input('Qual a sua jogada? ')) # Guarda a jogada escolhida pelo jogador
    print('-=' * 11) # Mostra na tela 11 vezes "-=". Execute para entender melhor...
    
    # --- Essa estrutura de repetição é uma forma de garantir que o jogador nunca jogue uma opção invalida.
    while jogador > 2: # Enquanto o jogador digitar algo maior que dois...
        jogador = int(input('Qual a sua jogada? ')) # Pergunta novamente qual será sua jogada
    # --- Fim da estrutura de repetição! Note que ela não possui um break, uma vez que a mesma precisa sempre ser executada enquanto o jogador digitar algo maior que dois (inválido)    

    # Note que foi utilizado itens[computador] ou seja, computador escolhe um número entre 0 e 2
    # Uso o número "escolhido" pelo computador para retornar um elemento da lista (posições: 0, 1 e 2)
    print(f'Computador jogou: {itens[computador]}') # Mostra a escolha do computador
    print(f'Você jogou: {itens[jogador]}') # Mostra a escolha do usuário
    print('-=' * 11) # Mostra na tela 11 vezes "-=". Execute para entender melhor...

    
    # --- Estrutura de if para validar a jogas ---
    # A estratégia usada foi: Se o computador jogar 0, é testada todas as jogadas possíveis do usuário.
    # Exibe na tela de quem foi a vitória
    # Trata jogadas invalidas

    if computador == 0: # Se o computador "escolher" 0 (pedra)
        if jogador == 0: # Se o jogador escolher 0 (pedra)
            print('EMPATE') # Mostre que a partida empatou

        elif jogador == 1: # Agora se o jogar escolher 1 (papel)
            print('VOCÊ VENCEU') # Mostre que o jogador venceu
        elif jogador == 2: # Agora se o jogador escolher 2 (tesoura)
            print('VITÓRIA DO COMPUTADOR!') # Mostre que o computador venceu
        else: # Qualquer escolhe diferentes das anteriores (0, 1 e 2)
            print('JOGADA INVÁLIDA') # Mostre que a jogada foi inválida

    # Mesma coisa do bloco anterior, mas agora testando que o computador "escolheu" 1 (papel)
    if computador == 1:
        if jogador == 0:
            print('VITÓRIA DO COMPUTADOR!')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('VOCÊ VENCEU')
        else:
            print('JOGADA INVÁLIDA')

    # Mesma coisa que o bloco anterior, mas agora testando o que computador "escolheu" 2 (tesoura)
    if computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU')
        elif jogador == 1:
            print('VITÓRIA DO COMPUTADOR!')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')

    # --- Estrutura que pergunta se o jogador quer jogar novamente após a finalização da partida
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        break # Encerra a estrutura de repetição criada no início do código