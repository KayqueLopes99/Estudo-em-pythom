## Maneira como os elementos são adicionados a uma **lista de tuplas**
- A ideia principal é que, ao construir uma lista onde cada elemento deve ser uma **tupla**, é preciso garantir que os elementos sejam inseridos corretamente dentro dessa estrutura.  
```python
[("Elemento1", "Elemento2"), ("Elemento3", "Elemento4"), ...]
```
### **Exemplo do erro**
```python
lista = []
lista.append("A")
lista.append("B")
lista.append("C")
lista.append("D")

print(lista)  # Resultado: ['A', 'B', 'C', 'D']
```

## **Solução correta**
A solução correta seria adicionar cada **par de elementos dentro de uma tupla** antes de enviá-los para a lista:

```python
lista = []
lista.append(("A", "B"))
lista.append(("C", "D"))

print(lista)  # Resultado: [('A', 'B'), ('C', 'D')]
```

### **"Podemos mandar os elementos dentro das duplas com o append da lista daí vira este formato"**  
Se for necessário construir a lista dinamicamente, devemos garantir que os elementos sejam agrupados corretamente antes de adicioná-los.

```python
lista = []
elemento1 = "A"
elemento2 = "B"
lista.append((elemento1, elemento2))

print(lista)  # [('A', 'B')]
```
- Podemos construir os pares de elementos dinamicamente e enviá-los para a lista de forma programática.
- *Exemplo:*

````py
lista_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_siglas = ['BA', 'SP', 'MG', 'RJ']
list_oficial = []

for index in range(len(lista_states)):
    list_oficial.append((lista_states[index], list_siglas[index]))

print(list_oficial)
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
```

````