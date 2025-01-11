
from functools import reduce
product = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
total = reduce(
    lambda acumulador, product: acumulador + product['preco'],
    product,
    0
)
print('Total é', total)
# total = 0
# for p in produtos:
#     total += p['preco']
# print(total)
# print(sum([p['preco'] for p in produtos]))

