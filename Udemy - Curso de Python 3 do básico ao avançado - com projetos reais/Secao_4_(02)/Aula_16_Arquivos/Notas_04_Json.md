## Introdução: 
- Ele representa estruturas de dados comuns (como dicionários e listas) de forma padronizada para que possam ser armazenadas e compartilhadas entre diferentes sistemas e linguagens de programação.

- Armazenar e transmitir informações entre sistemas. Ele é baseado em texto e estruturado de forma simples, semelhante a um dicionário Python.

- ``arquivo.json``
- Tipos de dados: Boll, Number, Null, str, Array[], objeto{}. 

## Salvando dados Python em JSON com módulo json
- Salvar uma estrutura como o dicionário ou algum dado para ser recarregado depois. 
- O módulo `json` do Python permite salvar e carregar dados no formato JSON, que é amplamente utilizado para armazenar e transmitir informações estruturadas. 
- Conversão de Tipos Python <-> Json

## 0.1 `json.dump()` 
- A função `json.dump()` grava os dados diretamente em um arquivo.  
+ Sintaxe:  
```python
json.dump(obj, fp, indent=None)
```
- `obj`: O objeto Python (dicionário, lista, etc.) que será convertido para JSON.  
- `fp`: O arquivo onde os dados serão salvos.  
- `indent`: (Opcional) Define a formatação para facilitar a leitura.  

- Exemplo: Salvando um dicionário em um arquivo JSON.  
```python
import json

dados = {"nome": "Ana", "idade": 25, "cidade": "Natal"}

# Abrindo um arquivo para escrita e salvando os dados
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False) # ensure_ascii=False <- Acentos>

print("Dados salvos com sucesso!")
```
- Isso cria um arquivo `dados.json` com este conteúdo:  
```json
{
    "nome": "Ana",
    "idade": 25,
    "cidade": "Natal"
}
```

---

## 0.2 `json.dumps()`:  
- A função `json.dumps()` converte o objeto Python em uma string JSON, sem salvar em um arquivo.  

+ Sintaxe:  
```python
json.dumps(obj, indent=None)
```
- `obj`: O objeto Python que será convertido.  
- `indent`: (Opcional) Define a formatação do JSON.  

## Observação:
- Classes e módulos não entram aqui. 
- Objetos de classes personalizadas
- Funções (def e lambda)
- Objetos set (conjuntos)

## Como faço para retornar os dados:
## `json.load()`  
- A função `json.load()` lê um arquivo JSON e converte seu conteúdo em um objeto Python (como um dicionário ou lista).  

+ Sintaxe:  
```python
json.load(fp)
```
- `fp`: O arquivo JSON que será lido.  

- Vamos supor que temos um arquivo chamado `dados.json` com este conteúdo:  

```json
{
    "nome": "Ana",
    "idade": 25,
    "cidade": "Natal"
}
```

- Podemos carregar esses dados para um dicionário Python assim:  

```python
import json

# Abrindo e lendo o arquivo JSON
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

# Exibindo os dados carregados
print(dados)  # {'nome': 'Ana', 'idade': 25, 'cidade': 'Natal'}

# Acessando valores específicos
print(dados["nome"])  # Ana
print(dados["idade"])  # 25
```
