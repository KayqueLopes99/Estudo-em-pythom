# Crie um programa que leia vários némeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantas números foram dgitados e qual foi a soma entre eles, descponsiderando o 999.

qtd = 0 
soma = 0  

while True:  # Loop infinito
    numero = int(input('Informe um número: '))
    if numero == 999:
        break  # Sai do loop se o número 999 for digitado
    qtd += 1  
    soma += numero  
print('Número 999 digitado, Fim.')
print('Total de vezes que você digitou: {}'.format(qtd))
print("Somatório: {}".format(soma))
