# Crie um programa que leia 
media = qtd = soma = maior = menor= 0
resp = 'S'
while resp in 'Ss':
    numero = int(input('Informe um número: '))  
    soma += numero
    qtd += 1
    # Neste momento Temos que se apenas um número for gigitado.
    if qtd == 1:
        maior = menor = numero
    # Se tivermos dois números diferentes. 

    else:
        # Maior e menor já tem um valor atribuidos a eles, exemplo 2.
        # O segundo número digitado foi 3, tipo como o maior é 2, ele compara.
        if numero > maior:
            # Ele atribui se achar que o numero é maior do que o numero atribuido a variavel "maior".
            maior = numero
            # O segundo número digitado foi 3, tipo como o menor é 2, ele compara.
        if numero < menor:
            # Ele atribui se achar que o numero é menor do que o numero atribuido a variavel "menor".
            menor = numero
        

    resp = str(input('Deseja continuar(S/N)')).upper().strip()[0]
    

    
media = soma / qtd
print("Maior número: {}\nMenor número: {}".format(maior, menor))
print('Quantidade de Números digitados {} e a Média: {}'.format(qtd, media))
