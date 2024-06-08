# Tupla.
# num  = (2,3,4,5,6,7)
# print(num)
Lista_num  = [1,2,3,4,5,6,7]
print(Lista_num)
while True:

    print("0 - Sair.")
    print('1 - Substituir Um Elemento.')
    print('2 - Adicionar elemento no final da Lista.')
    print('3 - Ordenar elementos.')
    print("4 - Quantidade de Elementos.")
    print("5 - Adicionar Elemento em algum Local.")
    print("6 - Remover elemento.")

    opcao = int(input("Informe uma opção: "))
    if opcao == 1:
        indice = int(input("Qual a posição do elemento da lista você deseja substituir?"))
        elemento1 = int(input("Informe o número que você deseja colocar"))
        Lista_num[indice] = elemento1
        print(Lista_num)  

    elif opcao == 2:
       elemento2 = int(input("Informe o número que será adiconado no Final da Lista: "))
       Lista_num.append(elemento2)
       print(Lista_num)
    
    elif opcao == 3:
      opcao2 = int(input("1 - Crescente\n2 - Reverso"))
      if opcao2 == 1:
        Lista_num.sort() 
        print(f"Lista com Elementos Ordenados: {Lista_num}")
      elif opcao2 == 2:
       Lista_num.sort(reverse=True) 
       print(f"Lista com Elementos Ordenados: {Lista_num}")
    elif opcao == 4:
       print(f'Quantidade de elementos da lista é {len(Lista_num)} elementos.')
    elif opcao == 5:
       posição = int(input('Informe a posição Para Inserção: '))
       elemento3 = int(input('Informe o Algarismo Elementar: '))
       Lista_num.insert(posição, elemento3)
       print(Lista_num)
    elif opcao == 6:
       posição2 = int(input('Informe a posição Para Inserção: '))
       if posição2 in Lista_num:
          del Lista_num[posição2]
          print(Lista_num)
       else:
          print("Posição não encontrada.")
    elif opcao == 0:
        print("Saindo...")
        break
    else:
      print("Opção inválida.")
