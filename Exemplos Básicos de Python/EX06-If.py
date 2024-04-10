vendas = 1500
meta1 = 1700
meta2 = 2000

if vendas >= 2000: # Se vendas >= 2000
    bonus = 0.13 * vendas # Bonus de 13%
elif vendas >= 1300: # Senão se vendas >= 1300
    bonus = 0.10 * vendas # Bonus de 10%
else: # Se nenhuma das condições anteriores retornarem "verdadeiro"
    bonus = 0 # Não ganha bonus

print('Bonus total de: ', bonus)

print('FIM')