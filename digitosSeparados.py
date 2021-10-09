'''
    Faça um programa que sorteie um número entre 0 a 9999, e mostre na tela cada um dos digitos separados.
    Exemplo: Unidade: 5, Dezena: 4, Centena: 2, Unidade de milhar: 3.
'''

from random import randint

def separacao(num):
    print('O número sorteado é {}'.format(num))
    cont = len(num)
    print(cont)

    if cont == 4:
        for i in range(0, cont):
            if i == 0:
                print('Milhar {}'.format(num[i]))
            if i == 1:
                print('Centena {}'.format(num[i]))
            if i == 2:
                print('Dezena {}'.format(num[i]))
            if i == 3:
                print('Unidade {}'.format(num[i]))

    if cont == 3:
        for i in range(0, cont):
            if i == 0:
                print('Centena {}'.format(num[i]))
            if i == 1:
                print('Dezena {}'.format(num[i]))
            if i == 2:
                print('Unidade {}'.format(num[i]))

    if cont == 2:
        for i in range(0, cont):
            if i == 0:
                print('Dezena {}'.format(num[i]))
            if i == 1:
                print('Unidade {}'.format(num[i]))

vet = []
vet = randint(0, 10000)
vet = str(vet)

print(vet)

print(list(vet))
print(len(vet))

separacao(vet)


