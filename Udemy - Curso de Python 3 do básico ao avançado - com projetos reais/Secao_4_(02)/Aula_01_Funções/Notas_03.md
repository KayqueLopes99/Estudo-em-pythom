## Empacotamento e desempacotamento de dicionários + *args e **kwargs
- O empacotamento ocorre quando múltiplos valores são agrupados em uma única variável, geralmente em uma tupla ou dicionário.
- O desempacotamento ocorre quando os elementos de uma estrutura (lista, tupla ou dicionário) são extraídos individualmente.

## `*args` e `**kwargs`
- Para Manipular funções com argumentos variáveis através dos operadores `*` e `**`.
- 1. Empacotamento (`*args` e `**kwargs`)
- **`*args`** empacota múltiplos argumentos *posicionais* em uma **tupla**.
- **`**kwargs`** empacota múltiplos argumentos *nomeados* em um **dicionário**.

- Sintaxe:
```python
def funcao(*args, **kwargs):
    print("Args:", args)      # Tupla
    print("Kwargs:", kwargs)  # Dicionário
```

### Exemplo 1: Usando `*args` 
```python
def somar(*numeros):
    return sum(numeros)

print(somar(1, 2, 3, 4))  # Saída: 10
print(somar(5, 10))       # Saída: 15
```
- `*numeros` empacota os valores `(1, 2, 3, 4)` em uma tupla `(1, 2, 3, 4)`.

### Exemplo 2: Usando `**kwargs`
```python
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="José", idade=25, cidade="São Paulo")
# Saída:
# nome: José
# idade: 25
# cidade: São Paulo
```
- `**kwargs` empacota os argumentos nomeados `{nome="José", idade=25, cidade="São Paulo"}` em um **dicionário**.

---

- 2. Desempacotamento (`*` e `**`)
- O operador `*` desempacota elementos de uma **lista ou tupla**.
- O operador `**` desempacota elementos de um **dicionário**.

### Exemplo 3:
```python
numeros = [1, 2, 3, 4]
print(*numeros)  # Saída: 1 2 3 4
```
- `*numeros` desempacota os elementos da lista `[1, 2, 3, 4]` e os passa separadamente.


### Exemplo 4: Desempacotamento de Dicionários (`**`)
```python
def apresentar(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

dados = {"nome": "Ana", "idade": 22, "cidade": "Rio de Janeiro"}
apresentar(**dados)  # Saída: Nome: Ana, Idade: 22, Cidade: Rio de Janeiro
```
- `**dados` desempacota `{"nome": "Ana", "idade": 22, "cidade": "Rio de Janeiro"}` para os parâmetros da função.


## Resumo:
```py
pessoa = {
    'nome': 'Kayque',
    'sobrenome': 'Lopes',
}


dados_pessoa = {
    'idade': 20,
    'altura': 1.70,
}


# Desempacotamento do dicionario.
# Juntar-los, criamos um terceiro e extraímos os valores de cada colocando neste. 
# Podemos adicionar informações
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)


# Empacotando
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print("Nomeados:", chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# Desempacotando - Para não colocar todas as variaveis escritas.
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)
```