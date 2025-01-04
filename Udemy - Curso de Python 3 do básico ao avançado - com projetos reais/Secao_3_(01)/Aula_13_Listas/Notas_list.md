## Tipo list - Introdução às listas mutáveis em Python
- Exercício de listas:`Aula54.py`
- Acesso na string: `string[indice]`
``` python
# +12345
# -54321
string = 'ABCDE' # Cadeia de caracteres -> len(): 5.
```
- Podemos acessar elemento por elemento na string. Isso limita um pouco, assim tem-se o tipo `list`
## Definição:
- Uma lista de elementos em python: `Mutável`.
- Usamos `[]` e separando-os por vírgulas.
- Suporta vários valores de qualquer tipo.
- Estrutura => `nome = ['','', ...]`
- Guardam valores e podem ser modificadas.
- Pode-se colocar uma lista dentro da outra.
- É uma estrutura de dados que pode conter vários elementos. 
- Lista vazia é `False` e com elementos `True`.

```python
minha_lista = []
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