## filter é um filtro funcional
## ** `filter()`** :
- **filtrar elementos** de um iterável (como listas e tuplas) **com base em uma condição**.
- Aplica uma função que retorna `True` ou `False` para cada elemento do iterável e mantém apenas aqueles que retornam `True`.

---
- Sintaxe
```python
filter(funcao, iteravel)
```
- **`funcao`**  Uma função que retorna `True` para os itens que devem ser mantidos.  
- **`iteravel`**  A lista, tupla ou outro iterável de onde os elementos serão filtrados.  

O `filter()` retorna um **iterador**, então normalmente convertemos para `list()` ou `tuple()`.

- Filtrando números pares
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filter(lambda x: x % 2 == 0, numeros)

print(list(pares))  # [2, 4, 6, 8, 10]
```

## **Usando `filter()` com List Comprehension**

- **Dentro da List Comprehension**: O `filter()` pode ser utilizado na parte direita do `for` para aplicar uma condição de filtro.
- **Condição de Filtro**: Apenas os elementos que atendem à condição (retornam `True`) serão mantidos.
- **Alternativa**: Você pode optar por usar **list comprehension** diretamente ou o comando `filter()`, ambos com o mesmo propósito.
- **False**: Elementos que não atendem à condição do filtro são considerados `False` e não são incluídos.

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6]
```

```py
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
```