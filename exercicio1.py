'''Faça um programa que receba o peso de 7 pessoas. Calcule e mostre:
    * a quantidade de pessoas acima de 90 kg.
    * a média dos pesos das pessoas.'''

from Exercicio1_dados import dados
from Exercicio1_dados import condicao

try:
    while condicao:
        if len(dados) < 7:
            print('Estamos no peso da {} pessoa, falta informar {}'.format(1 + len(dados), 7 - len(dados)))
            dados.append(float(input('Digite o peso: ')))
        else:
            condicao = False

    cont = 0
    for i in range(0, len(dados)):
        if dados[i] > 90:
            cont += 1

    print('A quantidade total de pessoas acima dos 90 Kg é {}.'.format(cont))

    media = sum(dados) / len(dados)

    print('A média dos pesos de todas pessoas é {:.2f}.'.format(media))

except:
    print('Fim do programa.')