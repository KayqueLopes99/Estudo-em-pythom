## **Funções Decoradoras e Decoradores com Classes**  
- Usados para adicionar funcionalidades sem modificar a estrutura das classes diretamente.

---
+ Obs: O atributo `__class__.__name__` retorna o nome da classe de um objeto. 
- O atributo `__dict__` retorna um dicionário contendo os atributos de instância de um objeto. 
- O método `repr()` retorna uma representação textual de um objeto. 
---

### **Herança vs. Decoradores**
- **Herança** permite reutilizar código entre classes, mas pode introduzir complexidade, especialmente quando há muitas subclasses ou mudanças frequentes nos requisitos.

- **Decoradores** oferecem uma alternativa mais flexível, permitindo modificar ou adicionar funcionalidades às classes sem criar subclasses.
---

### **Composição e Decoradores**
- Ao invés de criar subclasses para cada variação de comportamento, podemos usar **composição**: criamos uma classe base e usamos **decoradores** para modificar ou adicionar funcionalidades.
- Decoradores podem ser aplicados a métodos específicos ou a classes inteiras.

---

- Explicação:
- Tem como fazer com a classe sendo o decorador.
- **Recebe a classe.**
- **Retorna a classe decorada Ou uma nova classe.**.
- Passamos o **@Decorador_função**.


``` py
def meu_decorador_metodo(func):
    def wrapper(self, *args, **kwargs):
        print(f"Método {func.__name__} sendo chamado na classe {self.__class__.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

## Pode ser aqui, mas vai ser para toda classe: 
@meu_decorador_metodo
class MinhaClasse:
    @meu_decorador_metodo # Só para está função -> colocando no método especifico
    def metodo(self):
        print("Executando método.")

obj = MinhaClasse()
obj.metodo()


```

## Funções decoradoras e decoradores com métodos
- Segue a mesma lógica anterior. Mas agora colocamos o decorador no método da classe.
- Subtituição do método pelo que é retornado na função decoradora. Isso pode gerar a recursão.
- func  é a função passada. 
````py
def meu_decorador(func):
    def wrapper(self, *args, **kwargs):
        print(f"Chamando {func.__name__} da classe {self.__class__.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class MinhaClasse:
    @meu_decorador
    def meu_metodo(self):
        print("Executando método!")

obj = MinhaClasse()
obj.meu_metodo()
````