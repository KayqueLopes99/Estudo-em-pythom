- 0.1 Classe pricipal (pessoa)
+ **Superclasse** (Base Class / Parent Class): Classe principal que contém atributos e métodos comuns ou Generica.

- 0.2 Classes filhas (cliente)
+ **Subclasse** (Child Class / Derived Class): Classe que herda da Superclasse e pode adicionar ou modificar comportamentos.
- *Tudo que está no pai está em seus filhos (classe).*


---
## super e a sobreposição de membros em Python Orientado a Objetos
- Todo comando herda de uma classe, tipo da class str, int, float e etc...
- O objetivo de desenvolver classes é estender suas funcionalidades. 
- `super()` Permite invocar métodos de uma classe pai (ou superclasse) dentro de uma classe filha (ou subclasse). 
- Em contextos de herança, quando você deseja acessar um método da classe pai.

- Usado em situações de **sobrescrita de métodos** (ou *method overriding*). Quando você redefine um método na classe filha, mas ainda quer executar o comportamento do método original da classe pai).
- 

### Sintaxe

```python
super().metodo()
```

## Ou

```python
super(CLASSNAME, self).metodo()
```
- Eu sou CLASSNAME procura na minha Classe_pai o metodo()...


```python
class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        super().falar()  # Chama o método 'falar' da classe pai (Animal)
        print("O cachorro late.")

# Criação de um objeto Cachorro
dog = Cachorro()
dog.falar()
```


### Vantagens do `super()`
- **Evitar hardcoding de nomes de classes:** Usar `super()` permite que a classe filha seja mais flexível e reutilizável, sem ter que se preocupar com o nome específico da classe pai.
- **Facilita a manutenção:** Se você mudar a classe pai, o código da subclasse pode continuar funcionando corretamente, sem a necessidade de atualização explícita de todas as chamadas para a classe pai.

### Chamada múltipla de superclasses em hierarquias complexas

- Se a classe filha herda de várias classes (herança múltipla), o `super()` ajuda a resolver qual método será chamado entre todas as superclasses de forma organizada. 


- **ordem de resolução de método (MRO)**, que define a ordem na qual as classes são consultadas.
- comando ``.mro()`` para ver a ordem de busca. 


```python
super(CLASSNAME, self).metodo()
```
- Eu sou CLASSNAME procura na minha Classe_pai o metodo()...
- A partir da classe filha procura na minha classe pai especificada este método e executa ele. 


```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()  ## Procurando na classe A
        print("Hello from B")

class C(A):
    def hello(self):
        super().hello()  ## Procurando na classe A
        print("Hello from C")

class D(B, C):
    def hello(self):
        super().hello()  ## Procurando na classe 1-C e 2-B
        print("Hello from D")

# Testando
obj = D()
obj.hello()
```


```
Hello from A
Hello from C
Hello from B
Hello from D
```


- Sempre que vamos repasar métodos de classe colocamos:
``` py
class A:
    ...

class B:
    def __init__(self, atributo_de_A):
        super().__init__(atributo)
        # Alterações

class C:
    def __init__(self, *args **kwargs):
        super().__init__(*args, **kwargs)
        # Alterações

...
```
- Isso é importante quando vamos fazer coisas/modificações /implementações diferentes na classe B. 