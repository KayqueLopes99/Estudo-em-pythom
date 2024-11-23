# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

peso = float(input('Informe seu Peso: '))

altura = float(input('Informe sua Altura: '))

imc = peso/(altura * altura)

if imc < 18.5:
    print("\033[32 m Abaixo do Peso. \033[m")
elif imc >= 18.5 and imc < 25:
    print("\033[32 m Peso Ideal. \033[m")
elif imc >= 25 and imc < 30:
    print("\033[32 m Sobrepeso. \033[m")
elif imc >= 30 and imc < 40:
    print("\033[32 m Obesidade. \033[m")
else: 
    print("\033[32 m Obesidade Mórbida \033[m")
