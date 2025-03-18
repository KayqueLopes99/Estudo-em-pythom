## Teoria: metaclasses são o tipo das classes
- No Python, **tudo é um objeto** – incluindo classes. E se classes são objetos, elas também precisam ser criadas por algo. Esse "algo" é a metaclasse.  

## 0.1 O que são Metaclasses: 
- Metaclasses são **as classes das classes**. Assim como um objeto é criado a partir de uma classe, **uma classe é criada a partir de uma metaclasse**.  

- Por padrão, a metaclasse no Python é `type`. Isso significa que, sempre que criamos uma classe, o Python usa `type` para construí-la.  
- O tipo da classe é TYPE.
- Seu objeto é uma instância da sua classe. E sua classe é uma instância de type (type é metaclass)

- Sintaxe:
``` py
# type('Name', (Bases,), __dict__)
MinhaClasse = type("MinhaClasse", (object,), {"atributo": 42})
```

---
## Funcionamento:

```python
# object acima
class MinhaClasse:
    atributo = 42

f = MinhaClasse() # Instancia.
# f é tipo da Minhaclasse.
```
O Python faz:
```python
MinhaClasse = type("MinhaClasse", (), {"atributo": 42})
```

- `"MinhaClasse"`: Nome da classe.  
- `()`: Tupla de classes base (herança).  
- `{"atributo": 42}`: Dicionário com atributos e métodos da classe.  
---
## Passos: 
- Quando criamos uma classe, o Python executa os seguintes passos na ordem:  
+ 1️ **`__new__` da metaclasse é chamado**: Ele cria a nova classe. É diferente do new da classe, o qual cria e retorna a instancia, passando para o self no init.

+ 2️ **`__call__` da metaclasse é chamado**: Ele gerencia a criação da instância, chamando:  
- `__new__` da classe com args: Cria a instância do objeto.  
- `__init__` da classe com args: Inicializa a instância.  

+ 3️ **O processo termina e a classe é criada.**  

---
## Métodos Importantes nas Metaclasses  
- **`__new__(mcs, name_class, bases(heranças), dct)`**: Chamado antes da classe ser criada.
- **`__call__(cls, *args, **kwargs)`**: Chamado ao instanciar a classe.  

---
+ **Metaclasses servem para modificar o comportamento das classes antes delas serem criadas.**  
+ **Se você não sabe se precisa de metaclasses, então provavelmente não precisa delas!**  
> "Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar."


## __call__ de uma metaclass cria e retorna a instância da classe
- Quando não conseguir visualizar a instância.
- Podemos colocar condicionais. 