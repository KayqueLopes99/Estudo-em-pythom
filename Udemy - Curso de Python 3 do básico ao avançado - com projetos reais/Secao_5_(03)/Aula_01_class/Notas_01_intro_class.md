## Introdução à seção e livros de referência
- Programação Orientada a objetos(POO).
## Classes (class) 
- As **classes** são moldes para criar objetos que possuem atributos (dados) e métodos (comportamentos/Funções/Ações dentro da classe). 
- Elas permitem a organização do código de forma estruturada e reutilizável, sendo um dos principais conceitos da programação orientada a objetos (POO).  

- As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

- Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
- Por convenção, usamos **PascalCase** para nomes de classes. (*Primeira Letra maiuscula de cada palavra!*)
- Ex: `NomeDadosClasse` 
- Uma **instância** é um objeto criado a partir de uma classe. Quando você define uma classe, ela serve como um molde (ou modelo), e cada vez que você cria um novo objeto baseado nessa classe, está criando uma instância dela.
- Ex: isInstance -> Mesmo conceito.


+ *Sintaxe:* 
- A palavra-chave `class` é usada para definir uma classe. O primeiro método dentro de uma classe geralmente é `__init__`, que é chamado automaticamente ao criar um novo objeto (instância).  

```python
class NomeDaClasse:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1  # Atributo do objeto
        self.atributo2 = atributo2  # Atributo do objeto

    def metodo(self):
        print(f"Valores: {self.atributo1} e {self.atributo2}")
```
## Introdução ao método __init__ (inicializador de atributos)
- O método __init__ em Python é um inicializador de atributos que faz parte de uma classe. Ele é chamado automaticamente quando um novo objeto (instância da classe) é criado.

- Ações:
- Define os atributos do objeto.
- Recebe valores para configurar esses atributos.
- Garante que cada objeto criado tenha seus próprios dados.
-  O **self** representa o próprio objeto e é usado para armazenar os valores passados na criação da instância. ``Ele deve ser o primeiro parâmetro.``

- *AttributeError*: Não tem o atributo.
- Estrutura:
```py
class Exemplo:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade


```
---

- Exemplo Explicativo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando instâncias (objetos) da classe Pessoa
pessoa1 = Pessoa("Carlos", 30) # Objeto
pessoa2 = Pessoa("Ana", 25) # Objeto

# Chamando o método apresentar para cada objeto
pessoa1.apresentar()  # Saída: Olá, meu nome é Carlos e tenho 30 anos.
pessoa2.apresentar()  # Saída: Olá, meu nome é Ana e tenho 25 anos.
```
