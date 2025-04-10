## Tipo list - Introdução às listas mutáveis em Python
## Definição:
- Uma lista de elementos em python: `Mutável`.
- Usamos `[]` e separando-os por vírgulas.
- Suporta vários valores de qualquer tipo.
- Estrutura => `nome = ['','', ...]`
- Guardam valores e podem ser modificadas.
- Pode-se colocar uma lista dentro da outra.
- É uma estrutura de dados que pode conter vários elementos. 
- Lista vazia é `False` e com elementos `True`.

- **Armazenamento sequencial DE TUDO.**
- Pode haver lista dentro de outras
```python
minha_lista = []
minha_lista = [[],[]]
minha_lista = ["valor_01", "valor_02", "..."]

# ou
minha_lista_vazia = list()
print(type(minha_lista))
```

- `Acesso`: Os elementos são acessados pelos seus índices começando do zero 0 -> infinito
- índices negativos para acessar elementos a partir do final da lista, onde o índice -1 se refere ao último elemento.
- O elemento sempre permanece com seus tipos normais. 

- `Alterar`: Utilizando o índice correspondente ao elemento que deseja alterar. Após acessar o índice de um elemento, você pode atribuir um novo valor a ele.

- Exemplo de uma lista:
```python           
#        +01234
#        -54321
string = 'ABCDE' # 5 CARACTERES COM len().
lista = list
print(bool([])) # falsy
print(lista, type(lista))


#         0    1       2       3     4
#        -5   -4      -3      -2    -1
lista = [19, True, 'Kayque', 22.12, []]
lista[1] = False # -> Alteração + Acesso.
print(lista)
print(lista[1], type(lista[2]))
```

### Listas aninhadas
- Listas podem armazenas todos os tipo de objetos Python, podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas e matriz), e acessar informando os índices de linha e coluna. 



``` py
matriz = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]

print(matriz[0]) # [1, 2, 3]
print(matriz[0][0]) # 1
```



- Resumo:
```` python
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
````

## Obs:
- Exercício de listas:`Aula54.py`
- Acesso na string: `string[indice]`
``` python
# +12345
# -54321
string = 'ABCDE' # Cadeia de caracteres -> len(): 5.
```
- Podemos acessar elemento por elemento na string. Isso limita um pouco, assim tem-se o tipo `list`

## Fatiamento:
- Podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o indice inicial e/ou final para acessar o conjunto.
- Segue a mesma lógica do fatiamento ``[inicio:fim:salto]`` das strings.

````python
print("Copia no Fatiamento")
d = [1,2,3,4]
c = d[:]# Recebe todos os itens da lista D.
c[2] = 8
print(f'Lista D: {d}')
print(f'Lista C: {c}')
````
# Copias da lista
```py
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
```

## Percorrer / Iterar: for in com tipo list
- O for e o in são usados em Python para percorrer elementos de uma lista de forma simples e eficiente. Eles permitem acessar cada elemento da lista de maneira sequencial.

``` python
frutas = ["maçã", "banana", "cereja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")

```

- Criar uma Lista com Range:
```` python
valores = list(range(4,11))
````
```
-        [4][5][6][7][8][9][10]
- Indices 0  1  2  3  4  5  6 
