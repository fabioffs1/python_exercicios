# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_1 = int(input('Informe a primeira nota: '))
nota_2 = int(input('Informe a segunda nota: '))
nota_3 = int(input('Informe a terceira nota: '))
nota_4 = int(input('Informe a quarta nota: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'Média das notas: {media:.2f}')