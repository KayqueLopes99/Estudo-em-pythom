## Type Annotations - Tipagem de Dados no Python

> 1. Definição e Ferramentas
As **Type Annotations** (anotações de tipo) são uma forma de adicionar dicas de tipagem ao código Python. Essas anotações ajudam desenvolvedores e ferramentas a entenderem o código melhor.

* **Ferramenta principal:** `mypy`
    * O `mypy` é uma biblioteca externa de verificação estática. Ele lê o seu código e as anotações de tipo para encontrar erros de lógica antes mesmo de você rodar o programa.
    * Instalação: `pip install mypy`
    * Uso no terminal: `mypy seu_arquivo.py`

---

## 2. Tipagem de Variáveis Simples
Você pode declarar explicitamente o tipo de uma variável no momento da atribuição.

**Sintaxe:**
`nome_variavel: tipo = valor`

**Exemplos:**
```python
idade: int = 25
nome: str = "Kayque"
ativo: bool = True
altura: float = 1.75

```

---

## 3. Parâmetros e Métodos (Funções)

Nas funções, você pode tipar tanto os argumentos que a função recebe quanto o que ela retorna. Isso é crucial para documentação e validação.

**Sintaxe:**
`def nome_funcao(parametro: tipo, ...) -> tipo_retorno:`

**Exemplo:**

```python
def somar(a: int, b: int) -> int:
    return a + b

# Se a função não retorna nada, usa-se None
def cumprimentar(nome: str) -> None:
    print(f"Olá, {nome}")

```

---

## 4. Estruturas de Dados (Coleções)

A partir do Python 3.9, você pode usar as próprias classes built-in (`list`, `dict`, `set`) para tipagem, sem precisar importar `List` ou `Dict` da biblioteca `typing` (embora em versões antigas isso fosse necessário).

### Nas Listas

Define uma lista onde todos os elementos devem ser de um determinado tipo.

**Sintaxe:**
`list[tipo_elementos]`

**Exemplo:**

```python
notas: list[float] = [8.5, 9.0, 7.5]
nomes: list[str] = ["Ana", "Bruno", "Carlos"]

```

### Nos Dicionários

Define o tipo da chave e o tipo do valor separadamente.

**Sintaxe:**
`dict[tipo_chave, tipo_valor]`

**Exemplo:**

```python
# Chave é string (nome), Valor é float (preço)
precos: dict[str, float] = {"Arroz": 20.50, "Feijão": 8.90}

```

### Nos Sets (Conjuntos)

Define um conjunto de elementos únicos de um tipo específico.

**Sintaxe:**
`set[tipo_elementos]`

**Exemplo:**

```python
ids_unicos: set[int] = {101, 102, 103}

```

---

## 5. Tipos Compostos e Opcionais

### Union Types (Dois ou mais tipos)

Utilizado quando uma variável pode aceitar mais de um tipo de dado. O operador `|` (pipe) funciona como um "OU". (Disponível a partir do Python 3.10).

**Sintaxe:**
`nome: tipo_um | tipo_dois = valor`

**Exemplo:**

```python
# A variável pode ser um número inteiro ou ponto flutuante
numero: int | float = 10.5
identificador: str | int = "ID_123"

```

### Tipos Opcionais

Muito comum em parâmetros de função que têm um valor padrão (default). Indica que o argumento pode ser do tipo especificado ou `None`.

**Sintaxe:**
`def funcao(nome: tipo | None = None) -> retorno:`

**Exemplo:**

```python
# O parâmetro 'saudacao' é opcional. Se não for passado, será None.
def mensagem(texto: str, saudacao: str | None = None) -> str:
    if saudacao:
        return f"{saudacao}, {texto}"
    return texto

```

### Checagem com isinstance

A verificação de tipos em tempo de execução (`isinstance`) também suporta a sintaxe de união com `|`.

**Sintaxe:**
`if isinstance(objeto, tipo_um | tipo_dois):`

**Exemplo:**

```python
x = 10
if isinstance(x, int | float):
    print("É um número")

```

---

## 6. Callable (Funções como Parâmetros)

Usado quando você espera receber uma função (callback) como argumento. É necessário importar da biblioteca `collections.abc` ou `typing`.

**Sintaxe:**
`Callable[[tipo_param1, tipo_param2, ...], tipo_retorno]`

* O primeiro colchete contém a lista de tipos dos argumentos de entrada.
* O segundo elemento é o tipo de retorno.

**Exemplo:**

```python
from collections.abc import Callable

def executar_operacao(a: int, b: int, funcao: Callable[[int, int], int]) -> int:
    return funcao(a, b)

def multiplicacao(x: int, y: int) -> int:
    return x * y

# Passando a função 'multiplicacao' como argumento
resultado = executar_operacao(5, 3, multiplicacao)

```

---

## 7. TypeVar (Tipos Genéricos)

Usado quando você quer criar uma função ou classe que funcione com qualquer tipo, mas que mantenha a consistência desse tipo. Por exemplo, uma função que recebe um argumento de tipo `T` e retorna esse mesmo tipo `T`, seja ele qual for.

**Configuração:**

1. Importar `TypeVar` de `typing`.
2. Definir uma variável de tipo (geralmente chamada de `T`).

**Sintaxe:**

```python
from typing import TypeVar

T = TypeVar('T') # T pode ser qualquer tipo

```

**Exemplo de Uso:**

```python
# Se entrar int, sai int. Se entrar str, sai str.
def retornar_elemento(valor: T) -> T:
    return valor

x = retornar_elemento(10)      # x é inferido como int
y = retornar_elemento("Teste") # y é inferido como str

```

---

## 8. Tipagem com Classes (User-Defined Types)

Você pode usar suas próprias classes como tipos para variáveis e parâmetros.

**Sintaxe:**
`variavel: NomeDaClasse`

**Exemplo:**

```python
class Estudante:
    def __init__(self, nome: str):
        self.nome = nome

# A função espera receber um objeto da classe Estudante
def matricular(aluno: Estudante) -> None:
    print(f"Matriculando {aluno.nome}")

novo_aluno: Estudante = Estudante("Kayque")
matricular(novo_aluno)

```

