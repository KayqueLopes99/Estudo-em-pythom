## Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos
- São utilizadas para definir uma estrutura base para outras classes. **Elas funcionam como modelos, garantindo que as subclasses implementem determinados métodos obrigatórios.**

- A abstração significa esconder detalhes e mostrar apenas o necessário. No Python, usamos classes abstratas para forçar outras classes a implementarem certos métodos.  
- Cria uma base obrigatória para outras classes seguirem.

+ Para criar classes abstratas no Python, utilizamos o módulo abc **(Abstract Base Class)**.


+ *ABCs* são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos(que estão implementados). Também podem ter  métodos concretos por elas mesmas.

- Concretos: métodos que fazem algo.
- Abstrato: métodos que forçam as classe a implementar aqueles métodos. 

+ **@abstractmethods** são métodos que não têm corpo.
+ As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.

+ Métodos abstratos DEVEM ser implementados nas subclasses *(@abstractmethod)*. Não na propria classe abstrata.

+ Uma classe abstrata em Python tem sua **metaclasse**(criar classes abstratas) sendo ABCMeta. É possível criar ``@property @setter @classmethod @staticmethod e @method ``como abstratos, para isso use *@abstractmethod* como decorator mais interno.

+ Temos duas maneiras de criar classes abstratas
````py
from abc import ABC

# Melhor!
class name(ABC):
    
    ...

# OR - maneiras são iguais


from abc import ABC

class ABC(metaclass=ABCMeta):

````

- Exemplo-Explicativo: 
```` py
from abc import ABC, abstractmethod
# Classe Pai - Abstrata passada por herança
# Não pode usar diretamente.
class Log(ABC):
    # Método obrigatório. 

    @abstractmethod
    def _log(self, msg): ...
    
    # Essas são passadas!
    # métodos concretos qua fazer coisas.
    def log_error(self, msg):
        return self._log(f"Error: {msg}")
    
    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogPrintMixin(Log):

    # Esse método abstrato é obrigatório! 
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

l = LogPrintMixin()
l.log_error("Erro.")
````


##  abstractmethod para qualquer método já decorado (property e setter)
- Se uma classe abstrata define um método como @property, todas as subclasses devem implementar essa propriedade.
- Se um método @property é abstrato e possui um @setter, ambos devem ser abstratos.
- É possível criar @property @property.setter @classmethod  @staticmethod e métodos normais como abstratos, para isso use @abstractmethod como decorator mais interno.

### Método concreto: implementa o método abstrato.
### @abstractmethod: Deve vim o mais interno possivel.

```py
from abc import ABC, abstractmethod


# Herda da ABC mas não é abstrata,  POIS ELA NÃO TEM MÉTODOS ABSTRATOS. 
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod 
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
      #  print("Sou inútil")
    

    @AbstractFoo.name.setter
    def name(self, name): 
        self._name = name



foo = Foo("Bar")
print(foo.name)

```