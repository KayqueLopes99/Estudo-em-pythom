## TEORIA: Herança, Generalização e Especialização na Programação Orientada a Objetos (POO)  
### 0.1 Herança  
- Herança simples: 

+ *Associação*: O Objeto USA O outro objeto; 
+ *Agragação*: O Objeto TEM O outro objeto; 
+ *Composição*: O Objeto É DONO O outro objeto; 

+ *Herança*: O Objeto É UM outro objeto; 
- A **herança**: permite que uma classe (chamada de **subclasse** ou **classe filha**) **herde atributos e métodos** de outra classe (chamada de **superclasse** ou **classe pai**).  
- Generealização: atributos em comum em uma única classe(PAI). Tudo o que tiver os atributos desta classe(PAI) pode herdar esses atibutos da classe(PAI).
- Uma classe estende uma classe. 

- 0.1 Classe pricipal (pessoa)
+ **Superclasse** (Base Class / Parent Class): Classe principal que contém atributos e métodos comuns ou Generica.

- 0.2 Classes filhas (cliente)
+ **Subclasse** (Child Class / Derived Class): Classe que herda da Superclasse e pode adicionar ou modificar comportamentos.

- Vantagens:  
- **Reutilização de código**
- **Hierarquia entre classes**
- **Facilidade na modificação**  

- Sintaxe: ``class classe_filha(classe_pai):``
- toda classe Herda automaticamente 
- Nome da classe: ``print(self.__class__.__name__)``
- Ordem de busca nas classe: 1 Filha; 2 Pai;  3 Builting.Object -> the System.

- Use no máximo *3 níveis de Herança*. Complexidade da profundidade das heranças. 

```python
# Classe Pai (Superclasse)
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Classe Filha (Subclasse) herdando de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)  # Reutilizando atributos da classe pai
        self.num_portas = num_portas

    def exibir_info(self):
        return f"{super().exibir_info()}, Portas: {self.num_portas}"

# Criando um objeto da classe Carro
carro1 = Carro("Toyota", "Corolla", 4)
print(carro1.exibir_info())  # Saída: Marca: Toyota, Modelo: Corolla, Portas: 4
```
---
## Generalização  
A **generalização** ocorre quando extraímos **características comuns** de duas ou mais classes e colocamos em uma **superclasse** para evitar repetição de código.  
- Quando diferentes classes possuem **comportamentos e atributos em comum**.  
- Para tornar o código mais modular e reutilizável.  
---
## Especialização  
A **especialização** ocorre quando uma subclasse adiciona **novos comportamentos ou atributos** que não existem na classe pai.  
- Quando uma subclasse precisa de funcionalidades **específicas** além das herdadas.  


