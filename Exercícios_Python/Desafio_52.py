# Dizer se é frimo
# Divisel por um e ele mesmo.
numero = int(input('Informe um número inteiro: '))
PRIMO = 1 # Verdade

for i in range(2, numero):
    if numero % i == 0:
        PRIMO = 0 # Falso
        break

if PRIMO and numero != 1:
    print("É primo")
else:
    print("Não é primo")
