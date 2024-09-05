import random # importa a função random
import os

# O jogo inteiro está dentro do while (repetição). Isso permite no final perguntar se o jogador quer iniciar outra partida.
while True:
    palavras_computacao = [ # Nessa lista existe um "banco de dados" com 50 palavras diferentes.
        "Algoritmo", "Programação", "Computador", "Linguagem", "Software",
        "Hardware", "Dados", "Internet", "Rede", "Byte",
        "Processador", "Memória", "Teclado", "Mouse",
        "Loop", "Condicional", "Variável", "Função", "Classe",
        "Objeto", "Estrutura", "Array", "Vetor", "Lista", "Fila", "Pilha",
        "Java", "Python", "JavaScript", "HTML", "PostgreSQL", "Swift",
        "Kotlin", "Linux", "Windows", "Android", "MongoDB", "SQLite", "Oracle",
        "Assembly", "Banco", "MySQL", "Perl", "Firewall", "Router", "Ethernet",
        "Framework", "Terminal", "Desktop", "Mobile", "Segurança"
    ] # fim da lista.

    palavra = random.choice(palavras_computacao) # Usa a função "choice" para sortear um item da lista
    tamanho_palavra = len(palavra) # Armazena o tamanho da palavra sorteada acima
    palpites_jogador = [] # Inicia uma lista de palpites vazia
    ganhou = False # Variável que controla se o jogo acabou ou não

    # --- Essa estrutura condicional analisa o tamanho da palavra sorteada e define o numero máximo de chances ---
    if tamanho_palavra >= 7:
        chances_restantes = 9
    elif tamanho_palavra >= 5:
        chances_restantes = 6
    else:
        chances_restantes = 5
    # --- Fim ---

    print(f'\nVamos começar! Você terá {chances_restantes} chances')
    print(f'Palavra sorteada foi: {palavra}') # Serve apenas para nos ajudar a testar o jogo

    # --- Estrutura de repetição que controla a lógica do jogo ---
    while True:
        for letra in palavra: # Para cada letra na palavra...
            if letra.lower() in palpites_jogador: # Se a letra constar na lista de palpites:
                print(letra, end='    ') # Exiba a letra
            else: # Senão...
                print('_', end='    ') # Exiba um "underline"
    # --- Note que essa estrutura se repete para cada letra da palavra sorteada ---

        # --- Quando a estrutura acima executar a primeira vez, será mostrado na tela apenas os underlines,
        # --- Uma vez que ainda não existem palpites --- #

        recebe_palpite = input('\nDigite uma letra: ') # Armazena o palpite (letra) digitado pelo jogador
        palpites_jogador.append(recebe_palpite.lower()) # Usa a funcao nome da lista.append para adicionar o palpite na lista

        if recebe_palpite.lower() not in palavra.lower(): # Se o palpite (letra) digitada NÃO estiver na palavra
            chances_restantes -= 1 # Reduz o número de chances de 1 em 1
            print(f'Letra não encontrada! Você tem ainda {chances_restantes} tentativas! :-(') # Mostra as chances atuais para o jogador
            
            # --- Mostra as letras que já foram digitadas ---
            print(f'Letras já digitadas: {palpites_jogador}') 
        
         ### --- Bloco de código para verificar se o usuário acertou a palavra ou não --- #
        ganhou = True # Muda a variável booleana para True


        for letra in palavra: # Para cada letra na palavra
            if letra.lower() not in palpites_jogador: # Se a letra não constar na lista de palpites...
                ganhou = False # Ganhou = Falso
                print(f'A letra {letra} não consta nos palpites do jogador. Então "ganhou" = {ganhou}') # APENAS PARA ENTENDIMENTO
     

        if chances_restantes == 0 or ganhou == True: # Se chances restantes é 0 ou ganhou é verdadeiro....
            print(f'Se você esta vendo essa mensagem, a variável ganhou é = {ganhou} e as changes restantes são iguais a {chances_restantes}') # APENAS PARA ENTENDIMENTO
            print('O próximo passo e verificar se você ganhou ou perdeu...') # APENAS PARA ENTENDIMENTO
            break

    if ganhou == True: # Se ganhou for verdadeiro...
        print(f"Parabéns! você ganhou. A palavra era: {palavra}") # Mostre que ganhou
    else: # senão...
        print(f'Não foi dessa vez! A palavra era: {palavra}') # Mostre que perdeu

    jogar_novamente = input('Deseja iniciar outra rodada? (s/n): '.lower()) # Pergunta se o jogador quer iniciar outra partida
    if jogar_novamente != 's': # Se a escolha for algo diferente de s (sim)...
        break # Esse break encerra o while que controla a repetição do jogo inteiro.