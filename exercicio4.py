'''
    Faça um programa que receba várias idades e calcule e mostre a média das indades.
    Finalize o programa quando a entrada for iqual a -1.
'''

try:
    x = int(input('Quantas idades deseja calcular?'))
    vet = []
    for i in range(x, -1, -1):
        if i > 0:
            vet.append(int(input('Digite uma idade: ')))
            print(vet)

except:
    print('Algo ocorreu errado.')

finally:
    print('A soma de todas idades é {}, e a média é {}'.format(sum(vet), sum(vet) / x))
    print('Obrigado por utilizar nosso software.')
