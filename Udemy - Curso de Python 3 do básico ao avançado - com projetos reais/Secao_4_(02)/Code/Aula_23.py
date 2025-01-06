# List - comprehension
# #print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# #print(lista)
lista = [numero * 2 for numero in range(10)]

#print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
#                  Desempacoto o produto e altero com aumento de 5% em cada um. 
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05}
                # Se o proço for maior que 20. 
                if produto['preco'] > 20 else {**produto}  
                for produto in  produtos]

#print(novos_produtos)
#print(*novos_produtos, sep='\n')



# Filter.
# Esquerda do for é mapeamento e a direita do for é filtro.
lista = [n for n in range(10) if n < 5]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05}
                # Se o proço for maior que 20. 
                if produto['preco'] > 15 else {**produto}  
                for produto in  produtos
                if produto['preco'] > 10 # Só os maiores que dez da lista oficial.

                
                ]
print(novos_produtos)