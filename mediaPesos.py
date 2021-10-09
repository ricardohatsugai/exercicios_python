'''
    Faça um programa que recebe o peso de 7 pessoas. Calcule e mostre
    * A quantidade de pessoas acima de 90 kg.
    * A média dos pesos das pessoas.
'''

pesos = []

condicao = True
contador = 0

while condicao == True and len(pesos) < 7:
    peso = float(input('Digite um peso: '))
    pesos.append(peso)
    if peso > 90:
        contador += 1

print(pesos)
print('A média dos pessos é {:.2f}'.format(sum(pesos) / 7))
print('A quantidade de pesos acima de 90 Kg, é {}'.format(contador))