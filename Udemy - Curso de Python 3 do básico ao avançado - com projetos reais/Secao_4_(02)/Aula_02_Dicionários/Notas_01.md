## Introdução ao tipo de dados dict - Dicionários em Python
- Os dicionários são coleções de itens, onde cada elemento é armazenado de forma não ordenada.
- São estruturas de dados do tipo par de `chave` e `Valor`. 

+ Cada elemento contém uma chave e um valor associado.
- A chave serve para indexar (posicionar) um elemento no dicionário.
- Chave como o Índice que vimos na lista e podem ser de tipos imutáveis como: str, int, bool, float, tuple ...

+ O valor pode ser de qualquer tipo, icluindo outr dicionario.
- Usamos `{}` - ou a classe dict para criar dicionários. 
- ``Mutávei``s: dict e list. 

+ Sintaxe básica: {'chave': 'valor'}.
- Semelhantes as Listas e tuplas, porém agora conseguimos persolizar os indices.

- Informações com atributos.
- Chaves iguais atualiza e só usa o ultimo valor.

``` python
pessoa = {
    'Nome': 'José Kayque',
    'Sobrenome': 'Lopes',
    'Idade': 20,
    'altura': 1.7,

# - Lista de dicionários - 
    'Endereços': [{'Rua': 'Zona Rural', 'Número': 230}, {'Graduação': 'Tecnologia da Informação', 'Matricula': 2023011415}
    ],
}

# print(pessoa, type(pessoa))
# pessoa = dict(nome='KAYQUE')
print(pessoa["Nome"])
print(pessoa["Sobrenome"])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
```

## Comandos: 
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
- print(diconário['Nome_do_indice'])

## Adionar Elementos Indice:
- Podemos Colocar:
- A sequência é Nome. Idade. Sexo.
````py
dados = {'Nome':'Kayque','Idade':19}
print(dados['Nome']) # Kayque
print(dados['Idade']) # 19

dados['Sexo']='M'
```` 
- Ele adionou o 'M' no elemento indice adionado ao dicionário chamado dados.

## Remover um Elemento Indice:
- Usamos Del ou Pop
### del:
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


## Manipulando chaves e valores em dicionários em Python:
- Adicionar: `Nome_dict['Indice'] = 'valor'`.
- Keyerror e Indexerror. 
- Chaves dinâmicas: Atribuir o  nome da chave a uma varíavel. Isso permite alterar. 

### Comando Get():
- O comando get() em dicionários no Python é uma forma segura de acessar os valores associados a uma chave.
- A principal vantagem de usar get() ao invés de acessar diretamente o valor com a chave, por exemplo, dicionario[chave], é que o get() não gera um erro caso a chave não exista no dicionário.

- Se tentarmos acessar uma chave que não existe no dicionário, não gera um erro. Ele apenas retorna None, indicando que a chave não foi encontrada.

````python
dicionario.get(chave, valor_default)
````

``` python
# Manipulando chaves e valores em dicionários

pessoa = {}
## Editar
chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

## Acessar
print(pessoa[chave])

## Criar
pessoa[chave] = 'Maria'

# Remover
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

## Verificar
# Se a chave existe !? 
# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')
```

--- 

## Obs:
1. **Lista como valor**:
- Uma lista como valor associado a uma chave. Por exemplo:
```python
pessoa = {'nome': 'Maria', 'idades': [25, 30, 35]}
```
- A chave `'idades'` tem uma lista de três valores.

2. **Dicionário aninhado**:
- Um dicionário dentro de outro dicionário. Por exemplo:
- ```python
- aluno = {'nome': 'João', 'notas': {'matematica': 8, 'portugues': 9}}
- ```
- A chave `'notas'` contém outro dicionário com as notas nas disciplinas.

## Com For:
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
# Aula16.py
```

1. Acessando informações dos filmes:
- Para acessar informações específicas de um filme, você pode usar índices na lista. Por exemplo:
- NO PRINT: print(nome_da_lista[indice_da_lista][Elemtos_do_dicionario_indice])

2. Iterando sobre a lista de filmes:
- Você pode percorrer todos os filmes da lista usando um loop. Isso imprimirá as informações de todos os filmes na lista.

     ```python
     for filme in filmes:
         print(f"Título: {filme['titulo']}, Ano: {filme['ano']}, Diretor: {filme['diretor']}")
     ```


## comandodo `in`:
- O operador in varifica se algo existe na lista ou dicionário.