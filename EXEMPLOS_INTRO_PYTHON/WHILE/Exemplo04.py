# Repete enquanto a variável continuar sendo True

continuar = True

while continuar == True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == "n":
        continuar = False

print("Programa encerrado.")