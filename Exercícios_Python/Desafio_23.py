# Faça um programa que leia umn número da 0 a 9999 e mostre na tela cada um dos digitos separados.

notas = int(input("Informe um numero de 0 a 9999: "))

milhares = notas // 1000
notas %= 1000

centenas = notas // 100
notas %= 100

dezenas = notas // 10
unidades = notas % 10

print("Milhares: ", milhares)
print("Centenas: ", centenas)
print("Dezenas: ", dezenas)
print("Unidades: ", unidades)








