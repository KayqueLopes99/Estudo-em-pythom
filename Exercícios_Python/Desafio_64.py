# Crie um programa que leia vários némeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantas números foram dgitados e qual foi a soma entre eles, descponsiderando o 999.



num = contador = soma = 0
while num != 999:
    soma += num
    contador += 1  
    num = int(input('Informe um número: '))
print('Número 999 digitado, Fim.')
print('Total de vezes que você digitou: {}'.format(contador))
print("Somatório: {}".format(soma))
