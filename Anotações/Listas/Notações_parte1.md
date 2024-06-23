# Listas em Python (Parte 1)
## Definição:
- Usamos `[]` e separando-os por vírgulas.
- Estrutura => nome=['','', ...]
- Guardam valores e podem ser modificadas.
- É uma estrutura de dados que pode conter vários elementos. 

- Exemplo de uma lista:
```python
minha_lista = ['maçã', 'banana', 'cereja']
```

## Comandos de Lista
### list()
- Criar uma Lista.
### append():
- Este comando adiciona um elemento ao final da lista.
- Sintaxe: `lista.append(elemento)`
- Exemplo:
   ```python
   minha_lista.append('damasco')

   print(minha_lista)  # Saída: ['maçã', 'banana', 'cereja', 'damasco']
   ```
#### Outra maneira com append:
- Podemos inserir os dados diretamente com append.
- Exemplo:
   ```python
   minha_lista.append(str(input("Informe uma Fruta: ")))
   # exemplo 'damasco'.

   print(minha_lista)  # Saída: ['maçã', 'banana', 'cereja', 'damasco']
   ```
### insert():
- Este comando insere um elemento em uma posição específica na lista.
   Sintaxe: `lista.insert(posição, elemento)`
   Exemplo:
   ```python
   minha_lista.insert(1, 'abacate')
   print(minha_lista)  # Saída: ['maçã', 'abacate', 'banana', 'cereja', 'damasco']
   ```

### del:
- Este comando remove um elemento de uma posição específica na lista.
   Sintaxe: `del lista[posição]`
   Exemplo:
   ```python
   del minha_lista[0]
   print(minha_lista)  # Saída: ['abacate', 'banana', 'cereja', 'damasco']
   ```

### pop():
- Este comando remove e retorna o último elemento da lista, ou o elemento na posição especificada.
   Sintaxe: `lista.pop()` ou `lista.pop(posição)`
   Exemplo:
   ```python
   fruta = minha_lista.pop()
   print(fruta)  # Saída: 'damasco'
   print(minha_lista)  # Saída: ['abacate', 'banana', 'cereja']
   ```

### remove():
- Este comando remove a primeira ocorrência de um elemento específico na lista.
   Sintaxe: `lista.remove(elemento)`
   Exemplo:
   ```python
   minha_lista.remove('banana')
   print(minha_lista)  # Saída: ['abacate', 'cereja']
   ```
- Podemos fazer uma verificação se o elemento está na lista com if e in.

### Criar uma Lista com Range:
```` python
valores = list(range(4,11))
````
```
-        [4][5][6][7][8][9][10]
- Indices 0  1  2  3  4  5  6 

```
## Ordenar
### Numeros:
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

### Saber o Tamanho Com len()
- len(nome_da_lista)

# Obs:
- Se você igualar as listas, se mudar uma a outra muda.
````python
a = [1,2,3,4]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
````

# Podemos copiar os Dados:
- Com fatiamento.
````python
print("Copia no Ftaiamento")
d = [1,2,3,4]
c = d[:]# Recebe todos os itens da lista D.
c[2] = 8
print(f'Lista D: {d}')
print(f'Lista C: {c}')
```