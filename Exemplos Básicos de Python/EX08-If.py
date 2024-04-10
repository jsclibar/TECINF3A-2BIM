media = 3
reprovadoFalta = False

if media >= 6 and reprovadoFalta == False: # Observe o uso da condição and
    print('Aluno aprovado')
elif media >= 4 and reprovadoFalta == False: # Observe o uso da condição and
    print('Aluno de recuperação')
else:
    print('Aluno reprovado')

print('FIM')

# Importante: Também pode ser usado o operador lógico or.
