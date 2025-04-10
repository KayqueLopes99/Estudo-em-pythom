## Tipo tuple (tuplas)
- Conceito:
- Em uma Declaração de uma varíavel com atribuição de valor, só podemos atribuir uma coisa para ela.
- Exemplo:
> Lanche = bolo
> lanche = suco X 
- Não podemos atribuir suco, pois ele irá substituir o bolo atribuido. 
- Logo tem-se essa necessidade.
- Isso é possivel com as Tuplas.

- Sintaxe
A sintaxe para criar uma tupla é simples. 

```python
# SINTAXE: 
nome_da_tupla = (elemento1, elemento2, elemento3, ...)
subtupla = nome_da_tupla[inicio:fim]

# Criando uma tupla vazia
tupla_vazia = ()

# Criando uma tupla com um único elemento (note a vírgula)
tupla_solo = (42,)

# Criando uma tupla com múltiplos elementos
minha_tupla = (1, 2, 3, 'abc', True)
```

## Construção
- Uma Tupla é uma varíavel que guarda diferentes valores(elementos).
- Acessamos cada elemento pelo seu índice correspondente.
- A tupla não pode ser alterada - você não pode adicionar, remover ou modificar os elementos.
- Comando `tuple(VARIAVEL)` ou `colocar as varíaveis sem os [ ]` ou colocar dentreo dos `( )`.
- Imutabilidade
```python
minha_tupla[0] = 10  # Isso causará um TypeError
```
- Conversões de tupla <-> Lista.

- Acessando Elementos
- Usando índices, começando do zero:

```python
# Acessando o primeiro elemento (índice 0)
print(minha_tupla[0])  # Saída: 1

# Acessando o último elemento (índice -1)
print(minha_tupla[-1]) # Saída: True
```
- Fatiamento: O fatiamento permite acessar subconjuntos de uma tupla usando índices.

```Python
subtupla = nome_da_tupla[inicio:fim]
```

- Por exemplo, se você tem uma tupla t = (0, 1, 2, 3, 4, 5)
- subtupla = t[1:4]  -> Isso retornará (1, 2, 3)
- subtupla = t[2]  -> Isso retornará (2)
- subtupla = t[1:]  -> Isso retornará (1, 2, 3, 4, 5)
- subtupla = t[-1]  -> Isso retornará ao ultimo elemento(5)

### Usando len(string) - Usamos para saber quantos elemetos tem a tupla.

### Usando Estrutura de Repetição:
- Para percorrer.
- Irá acessar cada elemeto.
- Exemplo:
```python
for c in tupla: # ATÉ O FIM DA TUPLA.
    print(c)
```

### Desempacotamento de Tuplas
O desempacotamento permite atribuir os valores de uma tupla a várias variáveis:

```python
# Desempacotando uma tupla
x, y, z, a, b = minha_tupla
print(x)  # Saída: 1
print(y)  # Saída: 2
```


