## List comprehension com mais de um for
- Podemos fazer um for dentro de outro.

```py
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))


lista_01 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista_01)
```


## Duuvidas:
- Atribuição de uma lista a outra variavel, as duas apontam para o mesmo local na memória. Isso implica que se um muda a outra muda também. 
- `copy()`

```py
numeros = [1, 2, 3, 4, 5]
novos_numeros = [numero for numero in numeros]

```
