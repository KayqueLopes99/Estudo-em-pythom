# Tabuada 
numero = float(input('Informe um algarismo: '))
multiplica = 0
divide = 0
adicao = 0
subtracao = 0
for i in range(1,11):
    multiplica = numero*i
    print("Multiplicação de {} por {} = {}".format(numero, i, multiplica))
    divide = numero/i
    print("Divisão de {} por {} = {}".format(numero, i, divide))
    adicao = numero + i
    print("Adição de {} por {} = {}".format(numero, i, adicao))
    subtracao = numero - i
    print("Subtração de {} por {} = {}".format(numero, i, subtracao))
