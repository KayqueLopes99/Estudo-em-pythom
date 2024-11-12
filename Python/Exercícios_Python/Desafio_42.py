# Refaça o desafio 35 colocando mais triângulos.

lado1 = float(input('Informe o Primeiro Lado: '))
lado2 = float(input('Informe o Segundo Lado: '))
lado3 = float(input('Informe o Terceiro Lado: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("Pode formar um Triângulo!")
    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
          print("Pode formar um Triângulo Equilátero.")

    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print("Pode formar um Triângulo Escaleno.") 
    else: 
        print("Pode formar um Triângulo Isósceles.") 
else: 
    print("Não pode formar um Triângulo!")
