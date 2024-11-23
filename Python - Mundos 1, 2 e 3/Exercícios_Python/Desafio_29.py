# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Informe a velocidade do seu veíuculo: '))

if velocidade > 80:
    print("Velocidade Ultrapassada o máximo é 80Km/h.")
    resultado = velocidade * 7
    print("Valor a pagar {}".format(resultado))
    
else:
    print('Nenhuma multa, Muito Bem !!!')
    