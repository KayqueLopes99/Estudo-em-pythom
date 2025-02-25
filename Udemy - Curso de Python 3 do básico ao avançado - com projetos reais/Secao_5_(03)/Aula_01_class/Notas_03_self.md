## Entendendo self em classes Python
-  O **self** representa o próprio objeto e é usado para armazenar os valores passados na criação da instância. ``Ele deve ser o primeiro parâmetro.``
```py
class Exemplo:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade


```
- self é um nome padrão. mas podemos muda-lo em sua nomeclatura. (CONVERÇÃO PADRÃO).
- Primeiro parâmetro. 
- Na chamada chamamos o objeto self, o qual você deu a nomenclatura e não a classe.

``` py
class Car:
    # Inicialização.
    def __init__(self, name="-"):
        self.name = name
    
    # Métodos e Ações
    def accelerate(self):
        print(f'{self.name} está acelerando!')

# DANDO NOME PARA O SELF!
model_fusca = Car("Fusca")
print(model_fusca.name)

# chamdo o self(objeto)
model_fusca.accelerate

model_celta = Car("Celta")
print(model_celta.name)
model_celta.accelerate

```