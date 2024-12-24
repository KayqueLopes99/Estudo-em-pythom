## (Parte 1) Métodos úteis nos dicionários Python (dict):
---
+ `len` - Conta quantas chaves (itens) o dicionário tem.
+ `keys` - Retorna as chaves do dicionário.
 e é iterável com as chaves.
+ `values` - Retorna os valores do dicionário. e é iterável com os valores.
+ `items` - Retorna as chaves e valores do dicionário como tuplas. e é iterável com chaves e valores.
+ `setdefault` - Adiciona uma chave com um valor se ela não existir.
+ `copy` - retorna uma cópia rasa (shallow copy)
+ `get` - Retorna o valor de uma chave, ou um valor padrão se a chave não existir.
+ `pop` - Apaga um item com a chave especificada (del)
+ `popitem` - Apaga o último item adicionado
+ `update` - Atualiza o dicionário com outro dicionário ou iterável.
---

### 1. **`len()`**
- Sintaxe: `len(dicionario)`
- Explicação: Retorna o número de itens (pares chave-valor) no dicionário. Ou seja, quantas chaves ele possui.
  
**Exemplo**:
```python
dicionario = {"nome": "Maria", "idade": 30, "cidade": "São Paulo"}
quantidade = len(dicionario)  # Retorna 3, pois há 3 chaves no dicionário
print(quantidade)
```


### 2. **`keys()`**

- Sintaxe: `dicionario.keys()`
- Explicação: Retorna um iterável contendo todas as chaves do dicionário. Isso permite que você percorra as chaves do dicionário de maneira eficiente.
- Retorna uma "lista" com todas as chaves do dicionário.
**Exemplo**:
```python
dicionario = {"nome": "João", "idade": 25, "cidade": "Rio de Janeiro"}
chaves = dicionario.keys()  # Retorna um iterável: dict_keys(['nome', 'idade', 'cidade'])
print(chaves)
```
- `Coerção`: Tem como converter a tipagem para outra com tupla ou list. 

### 3. **`values()`**

- Sintaxe: `dicionario.values()`
- Explicação: Retorna um iterável contendo todos os valores do dicionário, ou seja, os dados associados às chaves.
- Este retorna uma lista com todos os valores (valores associados às chaves) presentes no dicionário. 

**Exemplo**:
```python
dicionario = {"nome": "Pedro", "idade": 22, "cidade": "Belo Horizonte"}
valores = dicionario.values()  # Retorna um iterável: dict_values(['Pedro', 22, 'Belo Horizonte'])
print(valores)
```


### 4. **`items()`**

- Sintaxe: `dicionario.items()`
- Explicação: Retorna um iterável contendo pares de chave-valor do dicionário. Cada item do iterável é uma tupla com a chave e o valor.
- Retorna uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionário.

**Exemplo**:
```python
dicionario = {"nome": "Ana", "idade": 28, "cidade": "Fortaleza"}
itens = dicionario.items()  # Retorna um iterável: dict_items([('nome', 'Ana'), ('idade', 28), ('cidade', 'Fortaleza')])
print(itens)
```
### 5. **`setdefault()`**

- Sintaxe: `dicionario.setdefault(chave, valor_default)`
- Explicação: Se a chave não existir no dicionário, ela é adicionada com o valor fornecido (`valor_default`). Se a chave já existir, o valor não é alterado e o valor atual é retornado.
  
**Exemplo**:
```python
dicionario = {"nome": "Lucas", "idade": 30}
dicionario.setdefault("cidade", "Salvador")  # A chave "cidade" não existe, então é adicionada
print(dicionario)  # {'nome': 'Lucas', 'idade': 30, 'cidade': 'Salvador'}
dicionario.setdefault("idade", 35)  # A chave "idade" já existe, então o valor não é alterado
print(dicionario)  # {'nome': 'Lucas', 'idade': 30, 'cidade': 'Salvador'}
```







### 6. **`copy()`** - Retorna uma cópia rasa (shallow copy)

- **Sintaxe**: `dicionario.copy()`
- **Explicação**: Retorna uma **cópia rasa** do dicionário. Isso significa que uma nova instância de dicionário é criada, mas as referências aos objetos internos (se existirem) ainda são as mesmas.
  
**Exemplo**:
```python
dicionario = {"nome": "Carla", "idade": 32}
novo_dicionario = dicionario.copy()  # Cria uma cópia rasa
print(novo_dicionario)  # {'nome': 'Carla', 'idade': 32}
```

---

### 7. **`get()`** - Obtém o valor de uma chave

- **Sintaxe**: `dicionario.get(chave, valor_default)`
- **Explicação**: Retorna o valor da chave fornecida. Se a chave não existir, retorna `None` (ou o `valor_default` caso você forneça esse parâmetro).
  
**Exemplo**:
```python
dicionario = {"nome": "Pedro", "idade": 27}
nome = dicionario.get("nome")  # Retorna 'Pedro'
profissao = dicionario.get("profissao", "Desconhecida")  # A chave "profissao" não existe, então retorna "Desconhecida"
print(nome, profissao)
```

---

### 8. **`pop()`** - Apaga um item com a chave especificada

- **Sintaxe**: `dicionario.pop(chave)`
- **Explicação**: Remove e retorna o valor associado à chave especificada. Se a chave não existir, um erro (`KeyError`) será gerado.
  
**Exemplo**:
```python
dicionario = {"nome": "Julia", "idade": 35}
idade = dicionario.pop("idade")  # Remove a chave "idade" e retorna o valor 35
print(dicionario)  # {'nome': 'Julia'}
print(idade)  # 35
```

---

### 9. **`popitem()`** - Apaga o último item adicionado

- **Sintaxe**: `dicionario.popitem()`
- **Explicação**: Remove e retorna o **último** item inserido no dicionário como uma tupla de chave-valor. Se o dicionário estiver vazio, gerará um erro.
  
**Exemplo**:
```python
dicionario = {"nome": "Lucas", "idade": 29}
ultimo_item = dicionario.popitem()  # Remove o último item ('idade', 29)
print(dicionario)  # {'nome': 'Lucas'}
print(ultimo_item)  # ('idade', 29)
```

---

### 10. **`update()`** - Atualiza um dicionário com outro

- **Sintaxe**: `dicionario.update(outra_dict)`
- **Explicação**: Atualiza o dicionário com os pares chave-valor de outro dicionário ou de um iterável de pares chave-valor. Se a chave já existir, o valor será atualizado.
  
**Exemplo**:
```python
dicionario = {"nome": "Beatriz", "idade": 25}
novos_dados = {"idade": 26, "cidade": "Curitiba"}
dicionario.update(novos_dados)  # A chave "idade" é atualizada e "cidade" é adicionada
print(dicionario)  # {'nome': 'Beatriz', 'idade': 26, 'cidade': 'Curitiba'}
```

---

