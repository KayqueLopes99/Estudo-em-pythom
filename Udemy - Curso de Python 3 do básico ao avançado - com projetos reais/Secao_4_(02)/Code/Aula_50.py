# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filter_price(product):
    return product['preco'] > 100

new_product_list_comprention = [
    index_products for index_products in products
    if index_products['preco'] > 100
]

# outra
novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filter_price,
    products
)

print_iter(products)
print_iter(new_product_list_comprention)