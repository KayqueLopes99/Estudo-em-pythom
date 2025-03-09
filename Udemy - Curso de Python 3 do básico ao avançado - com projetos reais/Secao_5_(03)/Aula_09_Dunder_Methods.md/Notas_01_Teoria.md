## Teoria: Special Methods, Magic Methods ou Dunder Methods em Python**  
- São métodos especiais do Python que começam e terminam com **dois underscores** (`__dunder__`). Eles permitem definir comportamentos personalizados para operações padrão da linguagem, como comparação, operadores matemáticos e conversão para string. 
- Util para os objetos!
- **Dunder = Double Underscore**  
---
- self: Objeto. 
- other: Outro Objeto.
+ Os métodos abaixo definem como objetos da classe serão comparados usando operadores padrão:  

| Método | Operação | Exemplo |
|--------|----------|---------|
| `__lt__(self, other)` | Menor que (`<`) | `obj1 < obj2` |
| `__le__(self, other)` | Menor ou igual (`<=`) | `obj1 <= obj2` |
| `__gt__(self, other)` | Maior que (`>`) | `obj1 > obj2` |
| `__ge__(self, other)` | Maior ou igual (`>=`) | `obj1 >= obj2` |
| `__eq__(self, other)` | Igualdade (`==`) | `obj1 == obj2` |
| `__ne__(self, other)` | Diferente (`!=`) | `obj1 != obj2` |

+ Esses métodos permitem definir **operações matemáticas** personalizadas para objetos:

| Método | Operação | Exemplo |
|--------|----------|---------|
| `__add__(self, other)` | Soma (`+`) | `obj1 + obj2` |
| `__sub__(self, other)` | Subtração (`-`) | `obj1 - obj2` |
| `__mul__(self, other)` | Multiplicação (`*`) | `obj1 * obj2` |
| `__truediv__(self, other)` | Divisão (`/`) | `obj1 / obj2` |
| `__neg__(self)` | Negativo (`-obj`) | `-obj` |

+ Esses métodos controlam como um objeto é **representado como string**:

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `__str__(self)` | Representação amigável ao usuário | `str(obj)` ou `print(obj)` |
| `__repr__(self)` | Representação detalhada para depuração | `repr(obj)` |

- `__str__`: Deve fornecer uma saída **legível para humanos**.  
- `__repr__`: Deve fornecer uma saída mais técnica, útil para **depuração**.  
---

- Código explicativo:
````py
# Python Dunder Methods __repr__ e __str__

class Ponto:
    def __init__(self,x, y):
        self.x = x
        self.y = y

     
#    def __str__(self): # Quam olha o código. 
#       return f"({self.x}, {self.y})"

    def __repr__(self): # Para desenvolvedores.
        class_name = type(self).__name__
        return f"{class_name}(x={self.x}, y={self.y})"
    
    # Da soma p1 + p2 
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)
    def __gt__(self, other):
        result_self = self.x + self.y 
        result_other = other.x + other.y
        return  result_self > result_other
    

  




if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2?', p1 > p2)
    print('P2 é maior que P1?', p2 > p1)

# Se definir com algum deve fazer tudo segundo a ele. 
# Se tiver string nos parâmetros de um método? use __str__
````


##  __new__(99%  SEM USO) e __init__(USA MUITO) em classes Python
- __new__ é o método responsável por criar e
- retornar o novo objeto. Por isso, new recebe cls.
- __new__ ❗️DEVE retornar o novo objeto❗️

- __init__ é o método responsável por inicializar
- a instância. Por isso, init recebe self.
- __init__ ❗️NÃO DEVE retornar nada (None)❗️
- object é a super classe de uma classe
`````py
class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)
````