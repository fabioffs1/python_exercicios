# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe a altura em metros: '))
peso_ideal = 72.7 * altura - 58
print(f'\nPeso ideal: {peso_ideal:.2f} kg')