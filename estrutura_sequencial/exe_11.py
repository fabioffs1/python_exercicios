# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1: o produto do dobro do primeiro com metade do segundo .
#2: a soma do triplo do primeiro com o terceiro.
#3: o terceiro elevado ao cubo.

num_1 = int(input('Informe um número inteiro: '))
num_2 = int(input('Informe outro número inteiro: '))
num_3 = float(input('Informe um número real: '))
result_1 = (num_1 * 2) * (num_2 / 2)
result_2 = (num_1 * 3) + num_3
result_3 = num_3 ** 3
print(f'\nO produto do dobro do primeiro com metade do segundo: {result_1}')
print(f'A soma do triplo do primeiro com o terceiro: {result_2:.2f}')
print(f'O terceiro elevado ao cubo: {result_3:.2f}')

