# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
print('-'*30)
print("Sequência de Fibonacci.")
print('-'*30)
primeiros_termos = int(input('Informe o número de primeiros Termos: '))
# Resolução 2.
# Já declarei o primeiro e o segundo termo, sendo 0 e 1.
primeiro = 0
segundo = 1
# Comecei com 3 termo, blz?
contador = 3
print('Termo 1 : {} \nTermo 2: {}'.format(primeiro,segundo))
while contador <= primeiros_termos:
    # terceiro = 0 + 1 = 1, blz?
    terceiro = segundo + primeiro
    print('Termo {}: {}'.format(contador, terceiro))
    # Vamos mover os termos a cada interação. 
    # O primeiro vai ser o segundo, logo 
    # O primeiro termo que era 0, agora é 1 ,1 que era o valor do segundo.
    # O segundo termo que era 1, agora é 1, 1 que era o valor do terceiro.
    primeiro = segundo
    segundo = terceiro
    # Incremento
    contador += 1
print("Fim.")




'''
Resolção 1
anterior = 0
i = 0  

while i < primeiros_termos:  
    if i == 0:
        numero = 0
    elif i == 1:
        numero = 1
    else:
        # Varíavel Temporária.
        manter_o_numero = numero
        numero += anterior  
        anterior = manter_o_numero
    print("Termo: {} é {}".format(i + 1, numero)) 
    i += 1  
'''