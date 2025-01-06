## Dictionary Comprehension e Set Comprehension
- Analogo, porém ultiliza as chaves `{}` em vez do `[]`.
- Para percorrer um dicionário usamos:
```py
product = {
    'name': 'Blue Pen',
    'preco': 2.5,
    'category': 'Office',
}

# Maneira correta.
# for key, value in product.items(): ...

dict_set = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value 
    in product.items()
    if key != 'category'
}

print(dict_set)

list = [
    ('a', 'Value _ 1'),
    ('b', 'Value _ 2'),
    ('c', 'Value _ 3'),
]

dict_set_2 = {
    key: value 
    for key, value in list
}

print(dict_set_2)

## ou

print(dict(dict_set_2))


# SET COMPREHENSION
s1 = {i ** 2 for i in range(10)}
# print(set(range(10)))
print(s1)
```


### Sintaxe
```python
{chave: valor if condição_opicional_para a chave for item in iterável if condição}
```
- `chave`: A chave do dicionário.
- `valor`: O valor correspondente à chave.
- `iterável`: Qualquer estrutura iterável (lista, range, dicionário, etc.).
- `if condição` *(opcional)*: Um filtro para incluir apenas certos elementos.

```python
quadrados = {x: x**2 for x in range(5)}
print(quadrados)
# Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

