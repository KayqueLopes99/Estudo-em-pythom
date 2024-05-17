# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
num = 0

while True:
    print("-"*50)
    num = int(input('Informe um número positivo para ver sua Tabuada ou um número negativo para sair: '))
    
    if num < 0:
        print("Fim.")
        break

    i = 0
    while i <= 10:
        multiplica = num * i
        print(f"{num} x {i} = {multiplica}")
        i += 1
