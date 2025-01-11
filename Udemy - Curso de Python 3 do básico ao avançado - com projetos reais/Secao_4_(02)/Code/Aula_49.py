from functools import partial
from types import GeneratorType

# map 
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

product_list = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def level_up_porcentage(value, porcentage):
    return round(value * porcentage, 2) # operação, casas decimais


# Partial, colocamos a porcentagem fixa
increase_porcentage_ten = partial(level_up_porcentage, porcentage=1.1)


def altern_price_of_product(product):
    return {
        **product,  # desempacotar os produtos
        'preco': increase_porcentage_ten(
            product['preco']
        )
    }

# Reutilizar - Converta em lista.
new_product = list(map(altern_price_of_product, product_list))
print_iter(product_list)
print_iter(new_product)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)