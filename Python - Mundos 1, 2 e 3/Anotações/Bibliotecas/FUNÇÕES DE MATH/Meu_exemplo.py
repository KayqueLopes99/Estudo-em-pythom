import math

numero1 = float(input("Informe o primeiro algarismo:\n"))
numero2 = float(input("Informe o segundo algarismo:\n"))

print('numero: {}'.format(numero1))
print('numero: {}'.format(numero2))

potencia = math.pow(numero1, numero2)
raiz = math.sqrt(numero1)
divisao = numero1/numero2
ceil = math.ceil(divisao)
floor = math.floor(divisao)

print('Potencia: {}'.format(potencia))
print('Raiz quadrada: {}'.format(raiz))
print('Divisao: {}'.format(divisao))
print('Arredondamento para cima (ceil): {}'.format(ceil))
print('Arredondamento para baixo (floor): {}'.format(floor))
