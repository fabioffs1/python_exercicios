# Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Informe o valor por hora trabalhada: '))
horas_trabalhadas = int(input('Informe as horas trabalhadas: '))
salario = valor_hora * horas_trabalhadas
print(f'Salário total: R$ {salario:.2f}')