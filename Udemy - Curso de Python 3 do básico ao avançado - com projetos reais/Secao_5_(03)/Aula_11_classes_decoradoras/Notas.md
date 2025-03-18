## Classes decoradoras (Decorator classes)
- Classes que decoram o objeto.
- Implementam o método especial `__call__`, tornando suas instâncias **callables** (ou seja, podem ser chamadas como funções). Elas funcionam de maneira semelhante a **funções decoradoras**, permitindo modificar o comportamento de outras funções ou métodos sem alterar seu código diretamente.  

---
- ### Para criar uma classe decoradora, seguimos os seguintes passos:  

- 1. **Criamos uma classe** que recebe a função a ser decorada no método `__init__`.  
- 2. **Implementamos o método `__call__`**, que será executado quando a instância da classe for chamada como uma função.  
- 3. **Podemos modificar o comportamento da função original** dentro de `__call__`.  

---
- | Forma de Implementação | Usa `def` e `@` | Usa `class` e `__call__` |
- `@Name_class`
- **Mantêm estado interno**
## Modo 0.1:
```py
class Multiplication:
    def __init__(self, func):
        self.func = func
        self._multiple = 10

    def __call__(self, *args, **kwds):
        print(args, kwds)
         # Retornando / Guardando a função executada.
        result = self.func(*args, **kwds)

        # Retornando a função executada * 10.
        return result * self._multiple
    

@Multiplication # Chamando a classe.

def operation_the_multiplication(x, y):
    return x * y

operation = operation_the_multiplication(2, 4)
print(operation)
```


## Modo 0.2
```py
# Se caso @Multiplication() pode-se: 
class Multiplication:
    def __init__(self, multiplicador):
        self._multiple = 10

    def __call__(self, func):
        # Função interna do decorator
        def intern(*args, **kwds):
            # Retornando / Guardando a função executada.
            result = func(*args, **kwds)
            return result * self._multiple
        # Retornando a função interna.
        return intern # Adiando a execução 
    

@Multiplication(10) # Chamando a classe e passando o multiplicador.

def operation_the_multiplication(x, y):
    return x * y

operation = operation_the_multiplication(2, 4)
print(operation)

```