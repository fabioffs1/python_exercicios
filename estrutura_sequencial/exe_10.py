# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.
# F = C x 1,8 + 32
celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
print(f'Temperatura em ºF: {fahrenheit:.2f}')