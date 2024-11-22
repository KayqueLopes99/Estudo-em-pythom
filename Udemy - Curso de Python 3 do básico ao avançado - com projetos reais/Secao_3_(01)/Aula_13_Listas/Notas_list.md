## Tipo list - Introdução às listas mutáveis em Python
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


## Alterando uma lista com índices, del, append e pop (Tipo list)
## Comandos de Lista
````python
lista = [10, 20, 30, 40, 50]
print(lista)
print(lista[2]) # 30
variavel = lista[2] # Atrubuir.
print(variavel)

lista = [10, 20, 30, 40, 50]
for elemento in lista:
    print(elemento)

````
- Se alterar o valor da lista todo relacionado a essa varível é alterado. 

---

### append():
- Este comando adiciona um elemento ao final da lista.
- O ultimo indice é reorganizado `n + 1`
- Sintaxe: `lista.append(elemento)`
- Exemplo:
   ```python
   minha_lista.append('damasco')

   print(minha_lista)  # Saída: ['maçã', 'banana', 'cereja', 'damasco']
   ```
### Outra maneira com append:
- Podemos inserir os dados diretamente com append.
- Exemplo:
   ```python
   minha_lista.append(str(input("Informe uma Fruta: ")))
   # exemplo 'damasco'.

   print(minha_lista)  # Saída: ['maçã', 'banana', 'cereja', 'damasco']
   ```
---
### insert():
- Inserindo itens em qualquer índice da lista com insert (Tipo list).
- Este comando insere um elemento em uma posição específica na lista.
   Sintaxe: `lista.insert(posição, elemento)`
   Exemplo:
   ```python
   minha_lista.insert(1, 'abacate')
   print(minha_lista)  # Saída: ['maçã', 'abacate', 'banana', 'cereja', 'damasco']
   ```
---

### del:
- Este comando remove um elemento de uma posição específica na lista.
- O python reorganiza com a exclusão.
- O elementos da frente se movem.
- Evita mover elementos do meio, e sim trabalhe sempre no final da lista. 
   Sintaxe: `del lista[posição]`
   Exemplo:
   ```python
   minha_lista = ['maçã', 'abacate', 'banana', 'cereja', 'damasco']
   del minha_lista[0] # Apartir daqui ele é deletado
   print(minha_lista)  # Saída: ['abacate', 'banana', 'cereja', 'damasco']
   ```
---

### pop():
- Este comando remove e retorna o último elemento da lista, ou o elemento na posição especificada.
- Pode-se mostrar o vaor removido. 
- retorna um valor relaconado ao tipo relacionado a lista.
   Sintaxe: `lista.pop()` ou `lista.pop(posição)`
   Exemplo:
   ```python
   fruta = minha_lista.pop()
   print(fruta)  # Saída: 'damasco'
   print(minha_lista)  # Saída: ['abacate', 'banana', 'cereja']
   ```
---

### remove():
- Este comando remove a primeira ocorrência de um elemento específico na lista.
   Sintaxe: `lista.remove(elemento)`
   Exemplo:
   ```python
   minha_lista.remove('banana')
   print(minha_lista)  # Saída: ['abacate', 'cereja']
   ```
- Podemos fazer uma verificação se o elemento está na lista com if e in.

---

### extend()
- Usado para adicionar múltiplos elementos ao final de uma lista.
- Ele aceita qualquer **iterável** (como listas, tuplas, strings, ou conjuntos) como argumento e adiciona cada elemento desse iterável à lista original, um por um.
- Não retorna a nada `none`.

- Sintaxe
```python
lista.extend(iterável)
```

- `lista`: A lista na qual os elementos serão adicionados.
- `iterável`: Um objeto como lista, tupla, string, etc., cujos elementos serão adicionados à lista.

- Exemplo
```python
# Exemplo com outra lista
lista = [1, 2, 3]
lista.extend([4, 5, 6])
print(lista)  # Resultado: [1, 2, 3, 4, 5, 6]

# Exemplo com uma tupla
lista = [1, 2, 3]
lista.extend((7, 8))
print(lista)  # Resultado: [1, 2, 3, 7, 8]

# Exemplo com uma string (cada caractere será adicionado como elemento)
lista = ['a', 'b']
lista.extend('cd')
print(lista)  # Resultado: ['a', 'b', 'c', 'd']
```

---

### Método `clear()`

- Usado para remover todos os elementos de uma lista.
-  Após o uso desse método, a lista ficará **vazia**, mas continuará existindo.

- Sintaxe
```python
lista.clear()
```
```python
# Exemplo básico
lista = [1, 2, 3, 4]
lista.clear()
print(lista)  # Resultado: []

# Exemplo em um cenário real
tarefas = ['fazer compras', 'estudar', 'caminhar']
print("Antes de limpar:", tarefas)  # Resultado: ['fazer compras', 'estudar', 'caminhar']
tarefas.clear()
print("Depois de limpar:", tarefas)  # Resultado: []
```
---

##  Concatenando listas em Python
- Juntar duas listas, resultando na união delas. 
- Sinal `+`
``` python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
```
---
## Cuidados com tipos de dados mutáveis - list e copy
- Em uma string pode-se salvar o valor da variavel1 em outra varíavel2 e mudar o valor da varíavel1 depois, mantendo copiado os dados da variavel1 na variavel2.
- Se você igualar as listas, se mudar uma a outra muda.
````python
a = [1,2,3,4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
````

``` python
var1 = 'Kay'
var2 = var1
var1 = "que"
```
- Copiado o valor (imutavel)
- Já em listas se `lista1 = lista2` elas vão apontar para o mesmo valor na memória (mutável).
- Quando mudar algum valor na outra vai mudar também.

``` python
lista_a = ['Luiz', 'Maria']
lista_b = lista_a
# Apontado para o mesmo valor na memória.

lista_a[0] = 'Qualquer coisa'
print(lista_b)
```
+ Como pode-se copiar:
- ultilizaos o método `copy()` que retorna os mesmo valores da lista_a para a lista_b. Isso garante que elas não vão apontar para o mesmo campo de memória.

### `copy()` 
- Isso significa que ele copia os elementos da lista original para uma nova lista, permitindo que você modifique uma delas sem alterar a outra.

- Sintaxe
```python
nova_lista = lista.copy()
```

```python
# Atribuição direta
lista1 = [10, 20, 30]
lista2 = lista1  # Referência compartilhada

lista2.append(40)  # Alterar lista2 também altera lista1
print("Lista1:", lista1)  # Resultado: [10, 20, 30, 40]
print("Lista2:", lista2)  # Resultado: [10, 20, 30, 40]

# Usando copy()
lista1 = [10, 20, 30]
lista2 = lista1.copy()  # Copiando

lista2.append(40)  # Alteração na cópia não afeta a original
print("Lista1:", lista1)  # Resultado: [10, 20, 30]
print("Lista2:", lista2)  # Resultado: [10, 20, 30, 40]
```

### Podemos copiar os Dados:
- Com fatiamento.
````python
print("Copia no Ftaiamento")
d = [1,2,3,4]
c = d[:]# Recebe todos os itens da lista D.
c[2] = 8
print(f'Lista D: {d}')
print(f'Lista C: {c}')
````


## for in com tipo list
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

```

- Exercício: exiba os índices da lista (aula com solução) `Aula49.py`

### Saber o Tamanho Com len() -> len(nome_da_lista). 





























### Sort():
- Ordena números que estão na lista.
``` python
valores=[2,7,9,4,53,3]
valores.sort() # 2,3,4,7,9,53
valores.sort(reverse=True) # Reverter -> 53,9,7,4,3,2
```
- Sintaxe: `lista.sort()crescente` ou `lista.sort(reverse=True)decrescente`
-Exemplo:
```python
minha_lista = ['cereja', 'banana', 'abacate']
minha_lista.sort()
print(minha_lista)  # Saída: ['abacate', 'banana', 'cereja']

minha_lista.sort(reverse=True)
print(minha_lista)  # Saída: ['cereja', 'banana', 'abacate']
```
### reverse(): 
- Inverte a ordem dos elementos na lista original.
- Sintaxe: `lista.reverse()`
- Exemplo:
```python
minha_lista = ['abacate', 'banana', 'cereja']
minha_lista.reverse()
print(minha_lista)  # Saída: ['cereja', 'banana', 'abacate']
```
--- 


--- 

















## Sumario:
### Criação e Manipulação
1. **list()** - Cria uma lista.
2. **append()** - Adiciona um elemento ao final da lista.
3. **extend()** - Adiciona múltiplos elementos de um iterável ao final da lista.
4. **insert()** - Insere um elemento em uma posição específica.
5. **pop()** - Remove e retorna o elemento em uma posição específica (ou o último, se não especificado).
6. **remove()** - Remove a primeira ocorrência de um elemento específico.
7. **clear()** - Remove todos os elementos da lista.
8. **del** - Exclui elementos ou fatias da lista.

### **Ordenação e Reversão**
9. **sort()** - Ordena a lista no lugar (opcionalmente com uma função de chave e ordem reversa).
10. **sorted()** - Retorna uma nova lista ordenada, sem alterar a lista original.
11. **reverse()** - Inverte a ordem dos elementos na lista no lugar.

### **Consulta e Busca**
12. **len()** - Retorna o número de elementos na lista.
13. **index()** - Retorna o índice da primeira ocorrência de um elemento.
14. **count()** - Conta quantas vezes um elemento aparece na lista.
15. **in** - Verifica se um elemento está presente na lista.

### **Fatiamento e Iteração**
16. **[:]** - Realiza fatiamento (slicing) para acessar sublistas.
17. **for ... in** - Itera pelos elementos da lista.
18. **enumerate()** - Retorna índices e valores enquanto itera pela lista.

### Operações Matemáticas
19. **sum()** - Retorna a soma dos elementos da lista.
20. **min()** - Retorna o menor elemento da lista.
21. **max()** - Retorna o maior elemento da lista.

### **Outros Métodos Úteis**
22. **copy()** - Retorna uma cópia rasa (shallow copy) da lista.
23. **join()** - Junta os elementos da lista em uma string (aplicável a listas de strings).
