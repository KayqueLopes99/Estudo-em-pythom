def fatorial(numero):
    fator = 1
    for c in range(numero, 0, -1):
        fator *= c
    return fator

# n = int(input("Digite um número: "))
# print(f"O fatorial de {n}: {fatorial(n)}")

f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial(7)

print(f"Resultados Fatoriais: {f1} {f2} {f3}")


def Par(n=0):
    if n % 2 == 0:
        return True
    else:
        False

num = int(input("Digite um número: "))
if Par(num):
    print('É par!')
else:
    print("Impar")