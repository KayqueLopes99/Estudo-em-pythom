# Faça um programa que calcule a soma entre todos os números impares que sãomultiplos de três e se encontram no intervalo 1 a 500
soma = 0
for i in range(1,501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
print(soma)