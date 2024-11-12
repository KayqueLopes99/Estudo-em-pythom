# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
Lista_Elementar = []
maior = menor = 0
posicao_maior = []
posicao_menor = []
for cont in range(0,5):
    valor = int(input(f'Informe o Valor para Posição {cont} : '))
    Lista_Elementar.append(valor)
    if cont == 0:# O primeiro valor é o maior e o menor
            maior = menor = Lista_Elementar[cont]
    else:
            # Se o valor é maior que o primeiro valor.
            if Lista_Elementar[cont] > maior:
                   maior = Lista_Elementar[cont]
            # Se o valor é menor que o primeiro valor.
            if Lista_Elementar[cont] < menor:
                   menor = Lista_Elementar[cont]
                   
for indice, valores in enumerate(Lista_Elementar):
       if valores == maior:
              posicao_maior.append(indice)
       if valores == menor:
              posicao_menor.append(indice)
              
print(f'Maior valor {maior} na posição {posicao_maior}')
print(f'Menor valor {menor} na posição {posicao_menor}')


              
              