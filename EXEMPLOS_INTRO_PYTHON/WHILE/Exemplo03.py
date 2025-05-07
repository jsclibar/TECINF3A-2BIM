# O programa repete indefinidamente até o usuário digitar "sair"

while True:
    texto = input("Digite algo (ou 'sair' para encerrar): ")

    if texto == "sair":
        print("Programa encerrado.")
        break  # Interrompe o laço
    else:
        print(f"Você digitou: {texto}")