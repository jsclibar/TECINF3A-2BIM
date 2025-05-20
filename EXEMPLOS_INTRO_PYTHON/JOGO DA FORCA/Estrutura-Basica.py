palavra = 'senac' # Palavra de exemplo
letras_chute = ['s', 'c'] # Chutes do usuário de exemplo
changes = 5 # Chances iniciais
ganhou = False # variavel que controla se o usuário ganhou ou não jogo


for letra in palavra: # Para cada letra na palavra....
    if letra in letras_chute: # Checar se a letra foi "chutada" pelo usuário. Se sim...
        print(letra, end = ' ') # Mostra a letra na devida posição! O end = espaço em branco faz com que o print não pule linha, usando como "encerramento" um espaço em branco no lugar de um uma quebra de linha (padrão)
    else:
        print('_', end = ' ') # Se não, no lugar da letra mostra um underline!
print(' ')
    

'''
A partir desse exemplo de código, crie um jogo da forca que funcione da seguinte maneira:

    A. Deve existir um "banco de dados" de palavras aleatórias e um sistema de sorteio Dica: GPT!
    B. O jogo se encerra quando o usuário errar 5 letras.
    C. Acertos não diminuem as chances do jogador.

Melhorias para realizar após os itens A, B e C estarem devidademente implantados:

    A. As chances devem aumentar ou diminuir de acordo com a quantidade de letras das palavras.
    B. O jogo deve sempre informar ao usuário a quantidade de chances disponíveis.
    C. Criar um sistema de pontuação de acordo com o desempenho do jogador.
    D. Após a finalização da partida, perguntar se o usuário deseja jogar de novo.
    E. FAÇA A IMPLANTAÇÃO DE UM NOVO RECURSO DE SUA ESCOLHA.


'''