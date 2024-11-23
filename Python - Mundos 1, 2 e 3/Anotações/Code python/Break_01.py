# Executando infinito .
numero = 0
while numero != 999:
    numero = int(input('Digite um número: '))
# Cinco tentativas. 
numero1 = cont = 0
while cont < 5:
    numero1 = int(input('Digite um número: '))
    cont += 1


n = s = 0
while n != 999:
    n = int(input('Digite em número: '))
    s += n
s -= 999
print('A Soma vale {}'.format(s))

# Loop infinito:
n = s = 0
while True:
    n = int(input('Digite em número: '))
    if n == 999:
       break
    s += n
s -= 999
# print('A Soma vale {}'.format(s))
print(f'A soma vale {s}')




