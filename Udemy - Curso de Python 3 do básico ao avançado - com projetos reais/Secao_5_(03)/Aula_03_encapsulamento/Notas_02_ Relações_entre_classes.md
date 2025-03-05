## Relações entre classes: associação, agregação e composição
- Os objetos dentro do sistema precisam interagir uns com os outros. Essas interações podem ser de diferentes tipos, sendo os três principais: **Associação, Agregação e Composição**.

---
## Associação  
- A **Associação** acontece quando **um objeto usa outro** sem que haja uma relação de dependência muito forte entre eles. Ou seja, um objeto pode existir **independentemente** do outro.  

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
- Podemos saber qual o objeto da classe 2 a partir do objeto da classe 1, está usando.
- Tipo ver qual objeto da caneta(classe2) o objeto da escritor(classe1) está usando. 
---







## Agregação  
A **Agregação** é um caso especial de associação onde **um objeto faz parte de outro**, mas ainda pode existir **independentemente**.  

### 🔹 Exemplo de Agregação:
```python
class Curso:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # Lista de cursos

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

curso1 = Curso("Python")
curso2 = Curso("JavaScript")

aluno = Aluno("Maria")
aluno.adicionar_curso(curso1)
aluno.adicionar_curso(curso2)

print(f'A aluna {aluno.nome} está matriculada nos cursos: {[curso.nome for curso in aluno.cursos]}')
```
📌 **Explicação:**  
- O **Aluno** tem uma lista de **Cursos**.  
- O **Curso** existe sozinho e pode ser atribuído a vários alunos.  
- Se o aluno for removido, os cursos continuam existindo, pois **não são dependentes**.

---

## 🔹 **Composição**  
A **Composição** é um caso mais forte de associação, onde **um objeto DEPENDE de outro para existir**. Se o objeto "pai" for destruído, o objeto "filho" também será.  

### 🔹 Exemplo de Composição:
```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_do_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_do_motor)  # O motor é criado junto com o carro

carro = Carro("Fusca", 1.6)
print(f'O carro {carro.modelo} tem um motor de {carro.motor.potencia}L.')
```
📌 **Explicação:**  
- O **Motor** só existe dentro de um **Carro**.  
- Se o **Carro** for destruído, o **Motor** também desaparece.  
- O **Carro** **cria** o motor dentro de si, então o motor **NÃO existe separadamente**.

---

## 🔥 **Resumo Rápido**  
| Tipo | Relação | Independência? | Exemplo |
|------|---------|---------------|---------|
| **Associação** | Um objeto usa outro | ✅ Sim | Escritor e Caneta |
| **Agregação** | Um objeto contém outro, mas eles existem separadamente | ✅ Sim | Aluno e Curso |
| **Composição** | Um objeto contém outro e controla seu ciclo de vida | ❌ Não | Carro e Motor |

Essas relações ajudam a estruturar sistemas de forma eficiente, garantindo organização e reaproveitamento de código. 🚀