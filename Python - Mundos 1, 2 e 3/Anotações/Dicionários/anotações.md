

## Maneiras:
#### Com For:
````py
# Pra cada chave e valor no items
for keys, values in filme.itens():
    print(f"O {keys} é {values}")

````

## Lista com Dicionario:
- Uma lista de dicionários é uma coleção de dicionários agrupados em uma única estrutura. Cada dicionário representa um item da lista.
- Você pode criar uma lista de filmes, onde cada filme é representado por um dicionário contendo informações como título, ano e diretor.
- Por exemplo:

```python
# Lista de filmes
filmes = [
    ## Aqui os dionários poderam ser acessados com o indice na lista e você adiona o elemento no dicionario ou remove.
    # Dionario 0
    # Dionario 1
    # Dionario 2

    {'titulo': 'Divertidade', 'ano': 2024, 'diretor': 'Kelsey Mann'},
    {'titulo': 'Aventuras no Espaço', 'ano': 2023, 'diretor': 'Luna Rodriguez'},
    {'titulo': 'O Mistério do Relógio Perdido', 'ano': 2022, 'diretor': 'Alexandre Silva'}
]
```

1. Acessando informações dos filmes:
- Para acessar informações específicas de um filme, você pode usar índices na lista. Por exemplo:
- NO PRINT: print(nome_da_lista[indice_da_lista][Elemtos_do_dicionario_indice])
```python
# Acessando o primeiro filme da lista
primeiro_filme = filmes[0]
print(primeiro_filme['titulo'])  # Saída: 'Divertidade'
print(primeiro_filme['ano'])     # Saída: 2024
## Ou 
print(filmes[0]['ano']) # 2024
print(filmes[2]['titulo']) # O Mistério do Relógio Perdido

```

2. Iterando sobre a lista de filmes:
- Você pode percorrer todos os filmes da lista usando um loop. Isso imprimirá as informações de todos os filmes na lista.

     ```python
     for filme in filmes:
         print(f"Título: {filme['titulo']}, Ano: {filme['ano']}, Diretor: {filme['diretor']}")
     ```



# Comando Copy():
- A função copy.copy(x) retorna uma cópia rasa do objeto x.
- Uma cópia rasa cria um novo objeto composto e insere nele referências aos objetos encontrados no original.
- Exemplo: 
```python
for c in range(0, qtd):
            estado['Uf'] = str(input('Unidade Federativa: ')).capitalize()
            estado['Sigla'] = str(input('Sigla: ')).upper()
        
            Brasil.append(estado.copy())
        print(Brasil)
```

- A função do método `copy()` nesse trecho de código é criar uma cópia rasa (shallow copy) do dicionário `estado`. Isso significa que a nova variável `estado.copy()` terá as mesmas chaves e valores do dicionário original, mas não compartilhará as mesmas referências de objetos. Portanto, ao adicionar essa cópia ao final da lista `Brasil`, você garante que cada entrada na lista seja independente e não afete o dicionário original. 