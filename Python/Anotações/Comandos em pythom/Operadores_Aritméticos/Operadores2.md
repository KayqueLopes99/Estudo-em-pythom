## Arrumar números com '.número_de_casas'.
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o segundo valor'))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print("A soma: {}".format(s))
print("A subtração: {}".format(sb))
print("A multiplicacao: {}".format(m))
print("A divisao: {}".format(d))
print("O quociente da divisao: {}".format(di))
print("A potencia: {}".format(p))

. Formatação 
numero = 1.22222222222222222222
print("{:.1f}".format(numero))
. irá imprimir 1.2
. É um ajuste na formatação do número.
