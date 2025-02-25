## Métodos em instâncias de classes Python
- São funções definidas dentro de uma classe que operam sobre as instâncias dessa classe. Eles podem acessar e modificar atributos do objeto, além de executar ações específicas.  

- Sintaxe:
```python
class NomeDaClasse:
    # Inicializa os atributis da instância.
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    def metodo_exemplo(self):
        print(f"Valores: {self.atributo1}, {self.atributo2}")
```

- Métodos de instância são funções definidas dentro de uma classe e usam `self` para acessar os atributos do objeto.  
- O método `__init__` inicializa os atributos quando a instância é criada.  
- Métodos podem ser chamados usando `instancia.metodo()`.  
### Hard coded - é algo que foi escrito diretamente no código.

```py
class Car:
    # Inicialização.
    def __init__(self, name="-"):
        self.name = name
    
    # Métodos e Ações
    def accelerate(self):
        print(f'{self.name} está acelerando!')

model_fusca = Car("Fusca")
print(model_fusca.name)
model_fusca.accelerate

model_celta = Car("Celta")
print(model_celta.name)
model_celta.accelerate

```