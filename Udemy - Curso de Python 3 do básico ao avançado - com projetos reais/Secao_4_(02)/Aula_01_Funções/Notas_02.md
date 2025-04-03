## (Parte 1) *args para quantidade de argumentos não nomeados variáveis
## Empacotamento em Python
- **Empacotamento**:
   - O empacotamento permite agrupar vários valores em uma única variável (como uma lista ou tupla).
   - Você pode usar o operador `*` para empacotar valores em uma sequência.
   - Ele Cria Um Tupla em Caso de Print:
```python
def contador(* núm):
    print(núm)

contador(1,4,3,2,7)
```


   - Exemplo:
     ```python
     def minha_soma(*args):
         return sum(args)

     print(minha_soma(1, 2, 3, 4, 5))  # Saída: 15
     ```
- Acumulação - A cada iteração vai realizando uma operação atuaizando este acumulador.

## (Parte 2) *args para quantidade de argumentos não nomeados variáveis

```` py

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y

# *ARGS - empacota o que se envia na função dentro de uma tupla.
def soma(*args):
    total = 0
    for numero in args:
        print('Total:', total, numero)
        total = total + numero
        print("Total:", total)
    return(total)

numeros01 = (1, 2, 3, 4, 5, 6, 7, 8)



# Desempacotando a tupla para enviar como parâmetros na função. 
somatoria_01 = soma(*numeros01)
print(somatoria_01)

numeros02 = (8, 9, 10, 11 ,12, 13)
somatoria_02 = sum(numeros02)
print(somatoria_02)
````


## Higher Order Functions - Funções de primeira classe
- Uma varíavel apontando para a mesma função na memória.
``` py
# Funções são da mesma classe que as varíaveis no python.
def saudacao(msg):
    return msg


saudacao_2 = saudacao # Aponta para mesma função de saudacao.
# referenciando na memória. 

variavel = saudacao_2("Good")
print(variavel)
```

- Uma mesma função que recebe outra. 
``` py
# Está função executa vai fazer funcionar a outra função saudacao.

def executa(funcao, msg):
    return funcao(msg)

variavel_01 = executa(saudacao, "Great")
print(variavel_01)

```

- Como podemos passar muitas coisas aleatórias nos parâmetros na função, podemos usar *args `empacotando`, para desepacotar na função do interna a outra.

- Passar funções como argumentos de outra e retornar de forma interna.
``` py
# Empacotar no parametro e desempacotar no return.
def saudacao2(msg, nome):
    return f'{msg}, {nome}!'


def executa1(funcao, *args):
    return funcao(*args)


print(
    executa1(saudacao2, 'Bom dia', 'Luiz')
)
print(
    executa1(saudacao2, 'Boa noite', 'Maria')
)
```

## Termos técnicos: Higher Order Functions e First-Class Functions
- Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

- Higher Order Functions - Funções que podem receber e/ou retornar outras funções

- First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

## Closure e funções que retornam outras funções
- Uma **closure** é uma função que **lembra** o ambiente em que foi criada.

1. **Função dentro de outra função**: Uma closure é criada quando uma função é definida dentro de outra e a função interna usa variáveis da função externa.
2. **Preservação de variáveis**: Mesmo quando a função externa termina sua execução, a função interna "lembra" das variáveis da função externa.

``` py
# FUNÇÃO DE SOMA
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # Executa a função e passa os argumento, armazenando o resultado.
    print(f"O resultado da operação = {resultado}")

exibir_resultado(10, 10, somar) # Executa e passo a função somar passando a referência de memória! 
exibir_resultado(10, 10, subtrair) # Executa e passo a função somar passando a referência de memória! 

```


``` py
# função externa
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar # Local da memória. 

# A função criar_saudacao retorna a função saudar (que é definida dentro dela), mas com o valor de saudacao já "lembado". Isso cria uma closure.
falar_bom_dia = criar_saudacao('Good morning')

# Quando chamamos criar_saudacao('Good morning'), a função retorna a função saudar com o valor 'Good morning' já "preso" nela.
falar_boa_noite = criar_saudacao('Good night')

for nome in ['kayque', 'Isabelly', 'Samuel']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
```
#### **Um MODO:**
``` py
# FUNÇÃO DE SOMA
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # Executa a função e passa os argumento, armazenando o resultado.
    print(f"O resultado da operação = {resultado}")

exibir_resultado(10, 10, somar) # Executa e passo a função somar passando a referência de memória! 
exibir_resultado(10, 10, subtrair) # Executa e passo a função somar passando a referência de memória! 

## MODO:
op = somar
op(1, 1) # 2
```


## Closure - Resumo.
Closure (ou "fechamento") é quando **uma função interna lembra** das variáveis da função externa **mesmo depois que a função externa já terminou a execução**.  

Ou seja, a função interna mantém um **"estado" salvo** e pode usá-lo mais tarde.


```python
def saudacao(nome):
    def mensagem():
        return f"Olá, {nome}!"  # "Lembra" de nome mesmo após saudacao terminar
    return mensagem  # Retorna a função interna sem executá-la ainda

# Criando uma função personalizada com nome fixo
cumprimento = saudacao("José")

# Chamando a função armazenada
print(cumprimento())  # Saída: Olá, José!
```

### **O que acontece:
1. **Chamamos `saudacao("José")`**, que cria uma função interna chamada `mensagem`.  
2. Essa função `mensagem` **"lembra"** do nome `"José"` mesmo depois que `saudacao()` já terminou.  
3. Retornamos `mensagem`, que agora está armazenada em `cumprimento`.  
4. **Quando chamamos `cumprimento()`**, ele ainda lembra que `nome = "José"` e imprime `"Olá, José!"`.  

---

## *Exemplo 02* - exercicio `Aula_40.py` 
````py
# Exercício - Adiando (Só depois) execução de funções (Closure)
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# *args = x.
def criar_funcao(funcao, *args):
    """
    Closure: Esta função recebe outra função (funcao) e argumentos fixos (*args).
    Ela retorna uma nova função (mandar) que "lembra" desses argumentos e 
    adia a execução da função original até receber o argumento final (y).
    """
    def mandar(y):  
        # A função interna "mandar" recebe 'y' quando for chamada mais tarde.
        # Ela "lembra" dos argumentos (*args) que foram passados antes,
        # mesmo depois que 'criar_funcao' já terminou sua execução.
        return funcao(*args, y)  
    
    return mandar  # Retorna a função interna sem executá-la ainda (Closure)


# Criando novas funções a partir da função base, com argumentos pré-definidos
soma_com_cinco = criar_funcao(soma, 5)  # A função retornada sempre somará 5 ao valor passado depois
multiplica_por_dez = criar_funcao(multiplica, 10)  # Sempre multiplicará o valor passado por 10

# Chamando as funções armazenadas
print(soma_com_cinco(4))  # 5 + 4 = 9
print(multiplica_por_dez(4))  # 10 * 4 = 40

````