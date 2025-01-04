## Introdução ao tipo set em Python (conjuntos)
- Sets - Conjuntos em Python (tipo set)
- Conjuntos ensinados na matemática. 
https://brasilescola.uol.com.br/matematica/conjunto.htm
- Representados graficamente pelo diagrama de Venn
- Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

- Em Python, um set (conjunto) é uma coleção desordenada de elementos únicos. Ele é útil quando você precisa armazenar itens sem duplicatas e realizar operações matemáticas como união, interseção e diferença.

+ **Principais Características do set**:
- Elementos únicos: Não permite valores duplicados.
- ``Não ordenado``: Os elementos não têm uma posição fixa.
- Mutável: Você pode adicionar ou remover elementos.
- ``Não indexado``: Não é possível acessar elementos por índice.
- Elementos imutáveis: Apenas valores imutáveis (como números, strings e tuplas) podem ser armazenados.


- **`Criando um set` || `Sintaxe`**
- A sintaxe: `set(interavel) ou {1, 2, 3}`
+ 1. Usando chaves {}
````python
numeros = {1, 2, 3, 4, 5}
print(numeros)  # Saída: {1, 2, 3, 4, 5}
````

+ 2. Usando set()
```` python
vogais = set("aeiou")
print(vogais)  # Saída: {'a', 'e', 'i', 'o', 'u'}
````

## Peculiaridades do tipo mutável set em Python
- Sets são eficientes para remover valores duplicados de iteráveis.
```py
numeros = {1, 2, 3, 3, 4, 5, 5}
print(numeros)  # Saída: {1, 2, 3, 4, 5}
```
- Conversão é possível.
```py
lista = [1,2,3,4,5,5,2,3]
s1 = set(lista) # 1,2,3,4,5
l2 = list(s1) 
```
- Seus valores serão sempre únicos.
- **Não tem Indexes** e **não garantem a ordem**. A parte de não garantir a ordem significa que ela sempre vai mudar os valores de local.
- Não aceitam valores mutaveis, como lista e dict. 
- Rápidos.
- **São iteraveis** (for, in, not in)

- Como o `in` é eficiente, pois para grandes coleções.
- Saber se o elemento está na estrutura. 
```python
elemento in estrutura
```


## Métodos úteis do tipo set
## 1️. Método `add()`
- O método `add()` adiciona um elemento ao conjunto. Se o elemento já existir, ele não será adicionado novamente, pois `set` não permite duplicatas.  

- Sintaxe 
```python
set_obj.add(elemento)
```
- Exemplo:
```python
numeros = {1, 2, 3}
numeros.add(4)  # Adiciona o número 4
numeros.add(2)  # Como 2 já existe, nada acontece

print(numeros)  # Saída: {1, 2, 3, 4}
```

## 2. Método `update()` 
- O método `update()` adiciona múltiplos elementos ao conjunto. Ele aceita listas, tuplas, outros conjuntos ou qualquer iterável como entrada.  

- Sintaxe  
```python
set_obj.update(iterável)
```

- Exemplo:  
```python
pares = {2, 4, 6}
impares = {1, 3, 5}

pares.update(impares)  # Une os dois conjuntos

print(pares)  # Saída: {1, 2, 3, 4, 5, 6}
```

## 3. Método `clear()`*
- O método `clear()` remove todos os elementos do conjunto, deixando-o vazio.  

- Sintaxe  
```python
set_obj.clear()
```

- Exemplo 
```python
numeros = {1, 2, 3, 4}
numeros.clear()  # Remove todos os elementos

print(numeros)  # Saída: set()
```

## 4. Método `discard()`  
- Remove um elemento específico do conjunto.  
Se o elemento **não existir**, **nenhum erro** será gerado (diferente de `remove()`, que gera erro).  

- Sintaxe  
```python
set_obj.discard(elemento)
```

- Exemplo: 
```python
animais = {"cachorro", "gato", "papagaio"}
animais.discard("gato")  # Remove "gato"
animais.discard("peixe") # Não gera erro, mesmo sem "peixe" no conjunto

print(animais)  # Saída: {'cachorro', 'papagaio'}
```


## Exemplo de uso do tipo set
```py
# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite uma Letra: ')
    if not letra.isalpha():
        print("Isso não é uma letra")
        continue
    else:
        letras.add(letra.lower())
    
    if 'l' in letras:
        print("Parabéns venceu!")
        break
    print(letras)
```

## Exercício `Aula_19.py`