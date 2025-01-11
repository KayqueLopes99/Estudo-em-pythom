## Funções decoradoras em geral
### 01. Funções Decoradoras e Decoradores (ou decorators)
- Funções **decoradoras** são funções que recebem outra função como argumento e **modificam seu comportamento** sem alterar diretamente seu código com uma closore. Elas permitem **adicionar, remover, restringir ou modificar** algo.  
- Funções decoradoras são funções que decoram outras funções.

```python
def decorador(funcao):
    def envoltoria():
        print("Executando algo antes da função...")
        funcao()  # Chamando a função original
        print("Executando algo depois da função...")
    return envoltoria  # Retorna a nova função modificada

# Aplicando o decorador manualmente
def minha_funcao():
    print("Sou a função original!")

minha_funcao = decorador(minha_funcao)  # Decorando manualmente
minha_funcao()
```

```
Executando algo antes da função...
Sou a função original!
Executando algo depois da função...
```
- O decorador **modifica a função original**, adicionando código antes e depois dela.

- O trabalho de uma função decoradora é receber uma função como argumento e criar uma função interna (closure). Essa função interna não será executada imediatamente, mas retornada sem execução, permitindo que o usuário a chame posteriormente.

- Quando a função decoradora é aplicada a outra função, ela pode executar ações antes ou depois da execução da função decorada, permitindo adicionar, modificar ou restringir seu comportamento sem alterar seu código original.

## Decoradores em Python **(@syntax_sugar)**
- Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
- `@decorador` (atalho para decorar funções)
- O Python permite usar `@decorador` para simplificar a aplicação da função decoradora.

- Exemplo com `@decorador`:  
```python
def decorador(funcao):
    def envoltoria():
        print("Executando algo antes...")
        funcao()
        print("Executando algo depois...")
    return envoltoria

@decorador  # Aplicando automaticamente o decorador
# Coloca-se acima da função que vai mandar. 
def minha_funcao():
    como __name__ ela vai ter o nome da função interna = envoltoria
    print("Sou a função original!")

minha_funcao()
```
- (mesma do exemplo anterior)  
```
Executando algo antes...
Sou a função original!
Executando algo depois...
```
- O `@decorador` **substitui** a necessidade de atribuir manualmente `minha_funcao = decorador(minha_funcao)`.  

---

