## Introdução à List comprehension 
- É uma forma para criar listas a partir de iteráveis.
- O `map()` é usado para **aplicar uma função a cada item de um iterável** (como listas e tuplas) e retornar um iterador com os resultados.

+ Sintaxe 
```python
nova_lista = [expressão for item in iterável if condição]
```
- **expressão** - O valor que será adicionado à nova lista.  
- **for item in iterável** - Iteração sobre a sequência de valores.  
- **if condição** *(opcional)* - Filtra os elementos com base em uma condição.  

### Exemplos   
```python
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Saída: [2, 4, 6, 8, 10]
```

```python
numeros = [1, 2, 3, 4, 5]
resultado = ["Par" if x % 2 == 0 else "Ímpar" for x in numeros]
print(resultado)  # Saída: ['Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar']
```

## Mapeamento de dados em list comprehension (map)
- Mapeamento significa transformar cada elemento de uma lista em outra coisa. Por exemplo, se temos uma lista de números e queremos dobrá-los, estamos mapeando cada número para o seu dobro.
- Pegando de um índice por outro.
- Mesmo Tamanho.

````python
nomes = ["ana", "joão", "maria"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)  # Saída: ['ANA', 'JOÃO', 'MARIA']
````

```` py
# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
#                  Desempacoto o produto e altero com aumento de 5% em cada um. 
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05}
                # Se o proço for maior que 20. 
                if produto['preco'] > 20 else {**produto}  
                for produto in  produtos]

print(novos_produtos)
print(*novos_produtos, sep='\n')

````

 
