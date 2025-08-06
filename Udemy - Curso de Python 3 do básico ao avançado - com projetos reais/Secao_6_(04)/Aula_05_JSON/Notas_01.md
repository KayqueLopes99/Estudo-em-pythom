## O que é JSON - JavaScript Object Notation
- JSON - JavaScript Object Notation (extensão .json)
- É uma estrutura de dados que permite a serialização de objetos em texto simples para facilitar a transmissão de dados através da rede, APIs web ou outros meios de comunicação.
### O JSON suporta os seguintes tipos de dados:
- Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
- Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
- As strings devem ser envolvidas por aspas duplas
- Booleanos: são os valores verdadeiro (true) ou falso (false)
- Arrays: são listas ordenadas de valores, como [1, 2, 3] ou ["Oi", "Olá", "Bom dia"]
- Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
- null: é um valor especial que representa ausência de valor
-
- Ao converter de Python para JSON:
- Python        JSON
- dict          object
- list, tuple   array
- str           string
- int, float    number
- True          true
- False         false
- None          null


## Comandos:
### 290. json.dumps e json.loads com strings + typing.TypedDict
- **dumps**: Converte um objeto Python em uma string JSON.  
    Exemplo: `json.dumps(objeto_python)`
- **loads**: Converte uma string JSON em um objeto Python.  
    Exemplo: `json.loads(string_json)`
- s: strings

- exemplo:
```python
string_json = '{"nome": "João", "idade": 30, "ativo": true}'
objeto_python = json.loads(string_json)
print(objeto_python)  # {'nome': 'João', 'idade': 30, 'ativo': True}

string_json = json.dumps(objeto_python)
print(string_json)  # '{"nome": "João", "idade": 30, "ativo": true}'
```

## TypedDict
- O `TypedDict` é uma classe do módulo `typing` que permite definir tipos para dicionários em Python.
- Ele é usado para especificar os tipos de chaves e valores em um dicionário, tornando o código mais legível e seguro.
```python
from typing import TypedDict
class Pessoa(TypedDict):
    nome: str
    idade: int
    ativo: bool
import json
pessoa: Pessoa = {"nome": "João", "idade": 30, "
ativo": True}
string_json = json.dumps(pessoa)
print(string_json)  # '{"nome": "João", "idade": 30,    "ativo": true}'
pessoa_carregada: Pessoa = json.loads(string_json)      
print(pessoa_carregada)  # {'nome': 'João', 'idade': 30, 'ativo': True}
```

## 291. json.dump e json.load com arquivos
- **dump**: Converte um objeto Python em uma string JSON e grava em um arquivo.
    Exemplo: `json.dump(objeto_python, arquivo)`
- **load**: Lê um arquivo JSON e o converte em um objeto Python.
    Exemplo: `json.load(arquivo)`


- exemplo:
```python
import json
# Criando um dicionário Python
pessoa = {"nome": "João", "idade": 30, "ativo": True}
# Gravando o dicionário em um arquivo JSON
with open('pessoa.json', 'w') as arquivo:
    json.dump(pessoa, arquivo)      
# Lendo o arquivo JSON e convertendo em um dicionário Python
with open('pessoa.json', 'r') as arquivo:
    pessoa_carregada = json.load(arquivo)
print(pessoa_carregada)  # {'nome': 'João', 'idade': 30, 'ativo': True}
```