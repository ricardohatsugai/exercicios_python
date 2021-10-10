'''
    Faça um programa que mostre o resultadode n!
    5! = 5 * 4 * 3 * 2 * 1
'''

x = int(input('Digite um número: '))
num = x - 1

for i in range(num, 0, -1):
    x = x * i
    print(i)

print('O fatorial de {} é {}'.format(num + 1, x))