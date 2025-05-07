# Usuário só pode sair se estiver autenticado (simplesmente com 'senha' correta)

autenticado = False

while not autenticado == True:
    senha = input("Digite a senha: ")
    if senha == "1234":
        autenticado = True

print("Acesso liberado.")