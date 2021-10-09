'''Programa Tabuada de multiplicação'''

for valor1 in range(0, 11, 1):
    for valor2 in range(0, 11, 1):
        produto = valor1 * valor2
        print('{} X {} = {}'.format(valor1, valor2, produto))
    print('*******************')