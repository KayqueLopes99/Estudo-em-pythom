# Faça um programa que leia um ângulo e mostre o valor do seno, cosseno e tangente.
import math

angulo = float(input('Informe os angulo: '))

radianos = math.radians(angulo)

print("Seno: {:.4f}".format(math.sin(radianos)))
print("Cosseno: {:.4f}".format(math.cos(radianos)))
print("Tangente: {:.4f}".format(math.tan(radianos)))
 
print("Cossecante: {:.4f}".format(1/math.sin(radianos)))
print("Secante: {:.4f}".format(1/math.cos(radianos)))
print("Cotangente: {:.4f}".format(1/math.tan(radianos)))