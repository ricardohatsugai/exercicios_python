'''Faça um programa que o usuário informe seu peso e o programa calcule o IMC, e informe se a pessoa está:
    * Baixo peso muito grave = < 16
    * Baixo peso grave = entre 16 e 16.99
    * Baixo peso = entre 17 e 18.49
    * Peso normal = entre 18.50 e 24.99
    * Sobrepeso = entre 25 e 29.99
    * Obesidade grau I = entre 30 e 34,99
    * Obesidade grau II = entre 35 e 39.99
    * Obesidade grau III = > 40'''

from imc_dados import mensagem
from imc_dados import imc

nome = str(input('Digite seu nome: '))
nome = nome.lower().title()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

x = imc(peso, altura)
frase = mensagem(x)

print('{}, seu IMC está {:.2f}, e você está com {}'.format(nome, x, frase))
