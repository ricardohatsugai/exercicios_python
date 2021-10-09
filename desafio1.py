'''Desafio 01
    Faça um programa que leia as variáveis: Nome, idade, Nota1, Nota2.
    E mostre na tela o nome do aluno com as iniciais maiúscula.
    Exiba se ele foi aprovado ou reprovado.
    Somente será aprovado se a média for >= 6.
    E idade >= 18 anos.'''

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
nome = nome.lower().title()
nota1 = float(input('Digite a nota N1: '))
nota2 = float(input('Digite a nota N2: '))
media = (nota1 + nota2) / 2
print('O nome digitado {}, contem {} caracteres, contando com espaço.'.format(nome, len(nome)))
if idade >= 18:
    if media < 6:
        print('O aluno {n}, que tem a idade {i}, foi reprovado com média {m:.2f}'.format(n=nome, i=idade, m=media))
    if media > 6  and media < 7.5:
        print('O aluno {n}, que tem a idade {i}, foi aprovado com conceito C, e média {m:.2f}'.format(n=nome, i=idade, m=media))
    if media >= 7.5 and media < 8.5:
        print('O aluno {n}, que tem a idade {i}, foi aprovado com conceito B, e média {m:.2f}'.format(n=nome, i=idade,m =media))
    if media >= 8.5:
        print('O aluno {n}, que tem a idade {i}, foi aprovado com conceito A, e média {m:.2f}'.format(n=nome, i=idade, m = media))
else:
    print('O aluno {} não foi aprovado por ter a idade menor que 18 anos.'.format(idade))