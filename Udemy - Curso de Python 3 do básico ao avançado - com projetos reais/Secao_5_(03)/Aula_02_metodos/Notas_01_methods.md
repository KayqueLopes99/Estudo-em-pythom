## Métodos de classe (@classmethod) + factories methods (métodos fábrica)
- Os métodos são funções definidas dentro de uma classe que permitem manipular e acessar atributos de um objeto ou da própria classe.
- *Métodos de Instância* – Operam nos atributos de um objeto (instância da classe) recebe `self`.
- *Métodos de Classe (@classmethod)* – Operam na classe como um todo, em vez de instâncias individuais.


## **O que são Métodos de Classe (@classmethod)**  
- Um método de classe é um método que pertence à classe, não à instância do objeto. Ele é definido com o decorador `@classmethod` e recebe a própria classe (`cls`) como primeiro argumento.  
- Não tem que passar o self.

#### Uso: 
- Quando precisamos acessar ou modificar atributos da classe.  
- Quando queremos criar instâncias da classe de maneiras alternativas (factory methods).  

```python
class Pessoa:
    ano_atual = 2025  # Atributo da classe

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @classmethod
    def criar_por_idade(cls, nome, idade):
        """Cria uma Pessoa calculando o ano de nascimento com base na idade."""
        nascimento = cls.ano_atual - idade
        return cls(nome, nascimento)

# Criando uma instância pelo método de classe
pessoa = Pessoa.criar_por_idade("João", 30)
print(pessoa.nome, pessoa.nascimento)  # João 1995
```

---

### **Factory Methods (Métodos Fábrica)**  
- São métodos que retornam instâncias da classe. Eles são comumente implementados como métodos de classe (`@classmethod`).  

- Quando queremos criar objetos de formas personalizadas.  
- Quando temos múltiplas maneiras de inicializar uma classe.  

- Um *exemplo* séria criar um método só para um caso especifico de pessoas com 50 anos e com nome anonimo no código anterior.
- Passagem de argumentos distintos.

```py
# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class People:
    year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @classmethod
    def method_the_class(cls):
        print("Hey")


    @classmethod
    def create_with_50_years_old(cls, name):
        return cls(name, 50)

    @classmethod
    def create_anonymous(cls, idade):
        return cls("Anônimo(a)", idade)
    
p1 = People('João', 34)
p2 = People.create_with_50_years_old('Helena')
p3 = People('Anônima', 23)
p4 = People.create_anonymous(25)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)
print(p4.name, p4.age)

```
---

## @staticmethod (métodos estáticos) são inúteis em Python =)
- Métodos Estáticos (@staticmethod) – Funções dentro da classe que não acessam atributos da instância ou da classe.

- Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls. Em resumo, são funções que existem dentro da sua classe.

- É como se fosse uma função. 


```py
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)
```

## method vs @classmethod vs @staticmethod
- method - self, método de instância
- @classmethod - cls, método de classe
- @staticmethod - método estático (❌self, ❌cls) <**Nomenclatura COM IMPRESSÕES**>

```py
# # method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # Recebe a self.
        self.user = user
    
    def set_user(self, password):
        self.password = password

    
    @classmethod # Recebe a classe
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)


    def connection_log(msg):
      print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('Kayque', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)


    
```