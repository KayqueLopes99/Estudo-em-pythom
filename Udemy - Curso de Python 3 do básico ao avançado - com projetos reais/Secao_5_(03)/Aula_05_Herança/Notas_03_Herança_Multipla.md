## Teoria - Herança múltipla - Python Orientado a Objetos 
````md
- Herança simples:
- Animal -> Mamifero -> Humano -> Pessoa -> Cliente
- Herança múltipla e mixins(classe que não faz parte da familia)
- Log -> FileLog(arquivo de dados)
- Animal -> Mamifero -> Humano -> Pessoa -> Cliente
- **Cliente(Pessoa, FileLog)**
-
- A, B, C, D
- D(B, C) - C(A) - B(A) - A
-
- método -> falar
-           A
-         /   \
-        B     C
-         \   /
-           D
````

- Quer dizer que no Python, uma classe pode estender várias outras classes.
- Ocorre quando uma classe herda de duas ou mais classes ao mesmo tempo, permitindo que ela combine funcionalidades de múltiplas superclasses. 
- **MRO (Method Resolution Order)**: define a ordem na qual as classes são pesquisadas para a execução de métodos.  
## Para saber a ordem de chamada dos métodos: Use o método de classe Classe.mro(). Ou o atributo __mro__ (Dunder - Double Underscore)
---
- Sintaxe:

```python
class ClasseBase1:
    def metodo(self):
        print("Método de ClasseBase1")

class ClasseBase2:
    def metodo(self):
        print("Método de ClasseBase2")

class ClasseDerivada(ClasseBase1, ClasseBase2):
    pass

obj = ClasseDerivada()
obj.metodo()  # Qual método será chamado?
```

---
### - A ordem importa: quanto mais no começo, mais ele vai procurar neste local, ou seja, procura no mais a esquerda. 

