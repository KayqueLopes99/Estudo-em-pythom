## Relações entre classes: associação, agregação e composição
- Os objetos dentro do sistema precisam interagir uns com os outros. Essas interações podem ser de diferentes tipos, sendo os três principais: **Associação, Agregação e Composição**.

---
## Associação  
- A **Associação** acontece quando **um objeto usa outro** sem que haja uma relação de dependência muito forte entre eles. Ou seja, um objeto pode existir **independentemente** do outro.  


- **A associação ocorre quando um objeto usa outro, mas sem uma relação de posse forte entre eles. Ou seja, os objetos podem existir independentemente e são apenas conectados por ``referências``.**
```python
# Classe que representa um Escritor
class Escritor:
    def __init__(self, nome):
        self.nome = nome  
        self._ferramenta = None  

    # Getter para acessar a ferramenta do escritor
    @property
    def ferramenta(self):
        return self._ferramenta

    # Setter para definir a ferramenta de escrita do escritor
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


# Classe que representa uma ferramenta de escrita
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome  

    # Método que simula a ação de escrever
    def escrever(self):
        return f'{self.nome} está escrevendo'


# Criamos um escritor
escritor = Escritor('Luiz')

# Criamos duas ferramentas de escrita: uma caneta e uma máquina de escrever
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

# Associamos o escritor a uma ferramenta (ele escolheu a máquina de escrever)
escritor.ferramenta = maquina_de_escrever

# Exibimos a ação de cada ferramenta escrevendo
print(caneta.escrever())  # "Caneta Bic está escrevendo"
print(maquina_de_escrever.escrever())  # "Máquina está escrevendo"

# O escritor usa a ferramenta que foi associada a ele (no caso, a máquina de escrever)
print(escritor.ferramenta.escrever())  # "Máquina está escrevendo"

```
- Ex: Escritor usa a caneta.
- Podemos saber qual o objeto da classe 2 a partir do objeto da classe 1, está usando.
- Tipo ver qual objeto da caneta(classe2) o objeto da escritor(classe1) está usando. 
---


## Agregação  
- A **Agregação** é um caso especial de associação onde **um objeto faz parte de outro**, mas ainda pode existir **independentemente**.  
- Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
- Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
- Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.
- A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
- Ex: Carro e roda: as duas vivem separadamente, mas necessitam se unir para fazer algo melhor. 
+ **Aula_12.py**
---

## Composição
- A **Composição** é um caso mais forte de associação, onde **um objeto DEPENDE de outro para existir**. Se o objeto "pai" for destruído, o objeto "filho" também será.  
- Composição é uma especialização da agregação.
- Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.
- Método `__del__` -> deletar tudo depois da execução.

- Exemplo: 
- O **Motor** só existe dentro de um **Carro**.  
- Se o **Carro** for destruído, o **Motor** também desaparece.  
- O **Carro** **cria** o motor dentro de si, então o motor **NÃO existe separadamente**.

---
````
           +----------------------+
           |    Associação        |  ← Conjunto maior
           |  (O objeto USA outro) |
           +----------------------+
                  ⬇
           +----------------------+
           |    Agregação         |  ←  Subconjunto de Associação
           |  (O objeto TEM outro) |
           +----------------------+
                  ⬇
           +----------------------+
           |    Composição        |  ← Subconjunto de Agregação
           | (O objeto É DONO do outro) |
           +----------------------+
````