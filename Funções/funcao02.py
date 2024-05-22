from random import randint

def ola_mundo():
    return 'Olá, Mundo!!!'

def soma_dois_numeros(num1, num2):
    resultado = num1 + num2
    return resultado

def media_tres_numeros(num1, num2, num3):
    resultado = (num1 + num2 + num3) / 3
    return resultado

def calcular_media(*numeros):
    if len(numeros) == 0:
        return 0 
    else:
        soma = sum(numeros)  
        media = soma / len(numeros)  
        return media
    
def par_impar(num):
    if num == 0:
        return 'Impossível calcular'
    else:
        if num % 2 == 0:
            return f'O número digitado é par!'
        else:
            return f'O número digitado é impar!'
        
def gerar_numero(inicio, fim):
    return randint(inicio, fim)

print(ola_mundo())
print(soma_dois_numeros(2,2))
print(media_tres_numeros(3,3,3))
print(calcular_media(2,2,2,2))
print(par_impar(0))
print(gerar_numero(1,10))