## Variáveis livres + nonlocal (locals, globals)
### 01. Variáveis Livres  
- Uma **variável livre** é uma variável que não é definida dentro do escopo local da função, mas que é usada dentro dela. 

```python
def externa():
    x = 10  # Variável "x" está no escopo da função externa

    def interna():
        print(x)  # "x" é uma variável livre dentro da função interna

    return interna  # Retorna a função interna sem executá-la

func = externa()  # Chama a função externa e armazena a função interna
func()  # Saída: 10 (a função interna ainda se lembra de "x")
```
- Motivo de "x":  
- `x` **não está definido dentro da função `interna`**, mas ela consegue acessá-lo do escopo externo (`externa`).  
- A função `interna` ainda "lembra" de `x`, mesmo depois que `externa` já terminou a execução. Isso é um exemplo de closure.


###  02. `locals()` e `globals()`
- Visualizar variáveis nos escopos local e global.

- `locals()`
- Retorna um dicionário com as variáveis do escopo local.

```python
def teste():
    x = 42
    y = "Python"
    print(locals())  # {'x': 42, 'y': 'Python'}

teste()
```

- `globals()`
- Retorna um dicionário com as variáveis globais do programa.

```python
global_var = "Sou global"

def teste():
    print(globals()['global_var'])  # Acessa a variável global

teste()
```

### 03 `nonlocal`
- O `nonlocal` permite **modificar** variáveis de um escopo externo (mas não global) dentro de uma função interna.  
+ Exemplo sem `nonlocal` (erro ao tentar modificar a variável):
```python
def externa():
    x = 10  # Variável do escopo externo

    def interna():
        x += 5  # Erro! O Python não permite modificar 'x' diretamente
        print(x)
    
    interna()

externa()
```
+ Exemplo correto com `nonlocal`:
```python
def externa():
    x = 10  

    def interna():
        nonlocal x  # Indica que queremos modificar a variável do escopo externo
        x += 5  
        print(x)  # Saída: 15

    interna()
    print(x)  # Saída: 15 (a variável foi realmente modificada)

externa()
```

- *Aula_41.py*