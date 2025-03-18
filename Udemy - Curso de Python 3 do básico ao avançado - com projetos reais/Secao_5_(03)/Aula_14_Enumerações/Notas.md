## Teoria: enum.Enum (Enumerações)
### Conceito:
- As **Enumerações** (`Enum`) são usadas para representar um **conjunto fixo de valores nomeados** dentro de um programa. 
- Enum: Usado em um grupo(conjunto) de coisas definidas. 
+ **Membros (constantes)** (`chaves`) são **ligados a valores únicos eles devem ser escritos em  Maiusculo**.  

+ São um conjunto de nomes simbólicos (membros) ligados a valores únicos.

+ Seus valores são **imutáveis** (constantes).  

+ Podem ser **iterados** para retornar seus membros canônicos na ordem de definição.  

+ São subclasses da classe `Enum`, mas **não são classes comuns** no Python.  

+ Podem ser usadas com **anotações de tipo (`type hints`)**, `isinstance()`, e outras verificações de tipo.  

- Na classe ```class Name(enum.Enum):```
```
Chaves Valores
1    azul
2    verde
3    vermelho
4    rosa
...  ...
```


---

### Criando uma Enumeração (`Enum`):  
- Para definir uma Enum, usamos o módulo `enum` e herdamos da classe `Enum`.  
- Tem uma funçã chamada `enum.auto() que faz enumeração numerica`
```python
from enum import Enum

class StatusPedido(Enum):
    PENDENTE = 1
    APROVADO = 2
    ENVIADO = 3
    ENTREGUE = 4
```

---

### Acessando Membros da Enum: .NAME e .VALUE 

```python
print(StatusPedido.PENDENTE)       # Saída: StatusPedido.PENDENTE
print(StatusPedido.PENDENTE.name)  # Saída: PENDENTE
print(StatusPedido.PENDENTE.value) # Saída: 1
```
- `.name` retorna o nome do membro (`PENDENTE`).  
- `.value` retorna o valor associado ao membro (`1`).  

---

- Podemos obter um membro da Enum através de seu **nome** (`chave`) ou **valor**:  

```python
print(StatusPedido['ENVIADO'])  # Saída: StatusPedido.ENVIADO
print(StatusPedido(3))          # Saída: StatusPedido.ENVIADO
```

```py
# Para obter os dados:
membro = Classe(valor), Classe['chave']
chave = Classe.chave.name
valor = Classe.chave.value
```
---

### **Iterando sobre uma Enum**  
```python
for status in StatusPedido:
    print(f"{status.name} = {status.value}")
``` 
```
PENDENTE = 1  
APROVADO = 2  
ENVIADO = 3  
ENTREGUE = 4  
```
### **Enumerações com Valores Personalizados**  

```python
class Cor(Enum):
    VERMELHO = "red"
    VERDE = "green"
    AZUL = "blue"
```
---