'''
    Faça um programa que verifique e mostre os números entre 1000 e 2000(inclusive) que, quando dividido por
    11 produza o resto igual a 5.
'''

try:
    vet = []

    for i in range(1000, 2001):
        if i % 11 == 5:
            print(i)
            vet.append(i)

finally:
    print('Os números que divididos por 11 resultal no resto = 5 são:')
    print(vet)
    print('Obrigado por utilizar nosso software.')