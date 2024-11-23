# 
lista_ordenada_sem_sort = []
maior_valor = -1
for cont in range(0,5):
    valor = int(input("Informe o Valor para Posição {} : ".format(cont+1)))
    # colocar cont == 0 para comparar. Se o valor for maior que o ultimo valor da lista.
    if cont == 0 or valor > lista_ordenada_sem_sort[maior_valor]:
        lista_ordenada_sem_sort.append(valor)
    else:
        # Percorrer as posições da lista.
        for posicao in range(len(lista_ordenada_sem_sort)):
            # Se o valor for menor ou igual aos valores da lista segundo os indices dos elementos da lista.
            # Vou verificar em cada posição se o numero é menor ou igual a ele.
            if valor <= lista_ordenada_sem_sort[posicao]:
                # Inserindo na Lista os Valores segundo os indices do valor menor ou igual aaos demais da lista.
                lista_ordenada_sem_sort.insert(posicao, valor)
                break # Para não duplicar valores
                
print(f"Lista Ordenada: {lista_ordenada_sem_sort}")

