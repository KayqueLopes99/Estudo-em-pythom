# Dicionários 
- Variáveis Compostas(Dicionários).
## Teoria:
- Os dicionários são coleções de itens, onde cada elemento é armazenado de forma não ordenada.
- Cada elemento contém uma chave e um valor associado.
- A chave serve para indexar (posicionar) um elemento no dicionário.

- Sintaxe básica: {'chave': 'valor'}.
- Mutavél
- Semelhanates as Listas e tuplas, porém agora conseguimos persolizar os indices.

```python
tuplas = ()
lista = []
dicionario = {}
```

## Comandos
### Dict: 
- Declarar um dicionário.
- Podemos declarar também:
``` python
dados = dict{}
# Ou
dados = {'chave_Ou_identificador': 'valor_Associado'}
```
- A sequência é Nome. Idade.
- Exemplo:
``` python
dados = {'Nome':'Kayque','Idade':19}
print(dados['Nome']) # Kayque
print(dados['Idade']) # 19
```
- Anteriomente os Indices seriam 0,1,2...
- Agora os Indices foram alterados para identificador sendo agora o nome e idade, no dicionário Dados.

#### No Print:
- print(diconário['Nome_do_indice'])

### Adionar Elementos Indice:
- Podemos Colocar:
- A sequência é Nome. Idade. Sexo.
````py
dados = {'Nome':'Kayque','Idade':19}
print(dados['Nome']) # Kayque
print(dados['Idade']) # 19
dados['Sexo']='M'
```` 
- Ele adionou o 'M' no elemento indice adionado ao dicionário chamado dados.

### Remover um Elemento Indice:
- Usamos Del ou Pop
#### del:
- Este comando remove um elemento de uma posição específica.
   Sintaxe: `del listdionario['elementos_indexado']`
- Por exemplo:
```python
dados = {'Nome':'Kayque','Idade':19}
print(dados['Nome']) # Kayque
print(dados['Idade']) # 19
dados['Sexo']='M'
del dados['Idade']
```

- Temos o pop(chave) para remover um elemento específico de um dicionário.
- A diferença é que o `.pop()` retorna o valor associado à chave removida. 
- Por exemplo:

```python
notas = {'João': 9, 'Maria': 10, 'José': 4}
nota_jose = notas.pop('José')  # Remove o aluno José e retorna a nota dele
print(f"A nota do José era {nota_jose}")
```
## Criação:
- Podemos criar elementos assim:
- Estes Elementos são chamados de Chaves ou Keys.
```py
# Elementos : TITULO, ANO, DIRETOR.
# Exemplo de dicionário
filme = {'titulo': 'Divertidade',
         'ano': 2024,
         'diretor': 'Kelsey Mann'}
```

1. `values()`: 
- Este retorna uma lista com todos os valores (valores associados às chaves) presentes no dicionário. 
- No dicionário `filme`, os valores seriam `'Divertidade'`, `2024` e `'Kelsey Mann'`.

   ```python
   valores = filme.values()
   print(valores)  # Saída: dict_values(['Divertidade', 2024, 'Kelsey Mann'])
   ```

2. `keys()`:
 - Retorna uma lista com todas as chaves do dicionário.
 - No exemplo, as chaves seriam `'titulo'`, `'ano'` e `'diretor'`.

   ```python
   chaves = filme.keys()
   print(chaves)  # Saída: dict_keys(['titulo', 'ano', 'diretor'])
   ```

3. `items()`: 
- Retorna uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionário.
- No caso do dicionário `filme`, as tuplas seriam `('titulo', 'Divertidade')`, `('ano', 2024)` e `('diretor', 'Kelsey Mann')`.

   ```python
   pares_chave_valor = filme.items()
   print(pares_chave_valor)
   # Saída: dict_items([('titulo', 'Divertidade'), ('ano', 2024), ('diretor', 'Kelsey Mann')])
   ```

### sintaxes:
```python
valores = dicionario.values()
chaves = dicionario.keys()
pares_chave_valor = dicionario.items()
```
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