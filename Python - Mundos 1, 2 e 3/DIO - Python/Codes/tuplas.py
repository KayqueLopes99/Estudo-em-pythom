"""
Exercício 2 - Tupla
Crie um programa onde o usuário informa 5 números e eles são armazenados em uma tupla. Depois, o programa deve:

Exibir a tupla completa.

Mostrar o maior e o menor número da tupla.

Informar quantas vezes o número 7 apareceu na tupla.
"""

tupla_de_numeros = ()


numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(5))

# Exibir a tupla completa
print("\nOs números digitados foram:", numeros)
print(f"Maior Número: {max(numeros)}.\nMenor Número: {min(numeros)}.")
print(f"O número 7 apareceu {numeros.count(7)} Vezes.")