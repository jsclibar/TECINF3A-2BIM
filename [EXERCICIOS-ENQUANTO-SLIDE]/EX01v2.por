programa {
  funcao inicio() {

    inteiro numero, soma = 0, quantidade = 0
    real media

    escreva("Digite um número (ou zero/negativo para encerrar): ")
    leia(numero)

    enquanto (numero > 0) {
      soma = soma + numero
      quantidade = quantidade + 1

      escreva("Digite um número (ou zero/negativo para encerrar): ")
      leia(numero)
    }

    se (quantidade > 0) {
      media = soma / quantidade
      escreva("Quantidade de números digitados: ", quantidade, "\n")
      escreva("Média aritmética: ", media, "\n")
    } 
    senao {
      escreva("Nenhum número positivo foi digitado.\n")
    }
  }
}

/*
  Este algoritmo solicita ao usuário que digite números inteiros positivos.
  A primeira entrada é feita fora do laço, e o programa continua solicitando
  novos números enquanto o valor digitado for maior que zero.

  Para cada número válido, ele soma e conta quantos foram digitados.
  Quando o usuário digita um número zero ou negativo, o laço termina.

  Se pelo menos um número válido foi digitado, o programa exibe a quantidade
  de entradas e a média aritmética. Caso contrário, informa que nenhum número
  positivo foi informado.
*/