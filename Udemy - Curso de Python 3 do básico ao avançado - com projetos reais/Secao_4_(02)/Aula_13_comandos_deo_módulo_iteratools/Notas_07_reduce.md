## Reduce - faz a redução de um iterável em um valor
- Sintaxe: 
``` py
from functools import reduce
reduce(funcao, iteravel, valor_inicial)
# funcao → Função que recebe dois argumentos e os reduz a um único valor.
# iteravel → Lista, tupla ou outro iterável que será reduzido.
# valor_inicial (opcional) → Valor inicial da acumulação.

```
- reduz um iterável a um único valor, aplicando uma função acumulativa de dois argumentos de forma sequencial.
- **O valor inicial é zero**. Deve ter para não ter problema.
- Exemplo explicativo. 
```py
from functools import reduce # Importação: `functools`.
product = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
] # Iterável

# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']



# Reduzir um iterável em um único valor.
total = reduce(
    # A função recebe um acumulador e valor_do_elemento.
    # Vai iterando de um em um elemento. 
    # Como o acumulador salva o ultimo valor podemos soma-lo com o elemento numerico. 
    lambda acumulador, product: acumulador + product['preco'],
    product,
    0
)

# Exemplo: valor total.
print('Total é', total)
```