## "def" define uma função personalizada - Introdução às funções em Python
- Incluimos Funcionalidades, de forma personalizada a necessidade escolhida.
- Uma rótina de uma informação ou código que deve ser reduzido. 
- Otimização do Código.
- Funções são trechos de código usados para replicar determinar ação ao longo do seu código. Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
- Por padrão, funções Python retornam None (nada).

- Sintaxe:
``` py
def Nome_da_Função(Parâmetros):
    # Bloco Corespondente.
## Chamada no programa inicial:


# Argumentos
Nome_da_Função()
```

## Valores já declarados com atribuições:
```py
# Se não passar um valor
def saudacao(nome='Desconhecido'):
    print(f"Olá, {nome}!")

saudacao("Kay")
saudacao()
```

## As funções em Python também suportam parâmetros nomeados. (key=value)
```py
def mensagem(msg):
    print('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_')
    print(msg)
    print('_+_+_+_+_+_+_+_+_+_+_+_+_+_+_')

# Essa Frase Vai Pra o Parâmetro.
mensagem('Sistema de Alunos.')
```

## Observações:
````python
def somatoria(a, b):
    soma = a + b
    print(f'A = {a}\nB = {b}\nResultado = {soma}')

# Programa Principal.
somatoria(4, 5)
somatoria(8, 9)
somatoria(2, 1)
# Maneira:
somatoria(a = 1, b = 5)
# Troca a Ordem:
somatoria(b = 1, a = 5)
````

- Argumento posicional, Ver os valores, ordenação.
- Paremtro = Função, Argumento = chamada.
- se um argumento é nomeados os da frente devem ser também.
- Quando falamos em argumentos, estamos falando sobre os valores passados para as funções no ato da sua execução. Existem argumentos nomeados e argumentos posicionais.

- Argumentos nomeados recebem o nome do parâmetro antes do valor, argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem
``` py
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição e para cer os valores inroduzidos em cada variavel
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
```

## Valores padrão para parâmetros em funções Python + NoneType e None
- Refatoração do código.
- Em uma varíavel que recebe um valor que é opicional, se ele não for enviado é atribuido algo diretamente a ele. 
- Quando uma variavel no parametro na função tem um valor padrão as depois dela devem ter também.
- Valores padrão para parâmetros.
- Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
-Refatorar: editar o seu código.

- COMO: `0 0.0 " "` -> FALSE.
- Como podemos saber se um parametro foi enviado, usando valor padrão.
- Ao definir um valor para um parâmetro, séria melhor ultilizar `None`.

``` python
def soma(x, y, z = None): # z recebe um valor Valor padrão.
    if z is not None: # Mesmo com 0 entra. 
        print(f'{x=} {y=} {z=}:', x + y + z) 
    else:
        print(f'{x=} {y=}', x + y)

soma(1,2)
soma(3,2)
soma(100,200)

soma(y = 9,z = 2, x = 7)
```

```python
def saudacao(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")
```

## (Parte 1) Escopo de funções e módulos em Python + global
- O código pode ir e voltar para locais do código específicos
- Escopo de funções em Python.
- Escopo significa o local onde aquele código pode atingir.
- Existe o escopo global e local.
- O escopo global é o escopo onde todo o código é alcançavel.
- O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
- o comando `global var` manipular as variavel fora do bloco, mudando seu valor em todos os locais. 

```` py
x = 1 # Está varíavel é global externo.

def escopo():
    global x # Manipula do x de fora.

    x = 10 # Está varíavel so funciona aqui, neste local interno.

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
````

``` py
def teste():
    x = 8 # Local
    print(f"Na função teste, n vale {n}") # 2
    print(f"Na função teste, x vale {n}") # 8 


# Prgrama principal:
n = 2 # Global
print(f"Na função principal, n vale {n}")
print(f"Na função principal, x vale {x}") # ERRO, x está só em teste.

```

## (Parte 2) Escopo de funções e módulos em Python + global
- Não temos acesso a nomes de escopos internos nos escopos externos.
- A palavra global faz uma variavel do escopo externo ser a mesma no escopo interno. 
- O escopo mais proximos "Dentro -> Fora", tudo o que está dentro da função está protegido. 

- Uma varíavel dentro de uma função só funciona dentr dela.
- Callstack - Pilha de chamadas no depurador. 
- É como se de fosse um local para definir as varíaveis.

- Escopo é algo muito usado na computação para delimitar e proteger determinadas partes do código. Em Python, o único escopo que vimos até então foi o escopo de funções (existem outros).

## Retorno de valores das funções (return)
- As funções retornam algum resultado. 
- O `return` é usada dentro de uma função para **devolver um valor ao código que chamou a função**.
-  Quando o `return` é executado, ele encerra a execução da função imediatamente e envia de volta o valor especificado. 

```python
def nome_da_funcao(parametros):
    # Operações ou cálculos
    return valor_a_retornar
```

Exemplo simples:
```python
def soma(a, b):
    resultado = a + b
    return resultado
```

```python
resultado = soma(3, 4)  # resultado agora é 7
print(resultado)        # Saída: 7
```

### Funcionamento do `return`
- Assim que `return` é executado, a função é encerrada e não continua a execução do código que vem após ele.
   ```python
   def exemplo():
       print("Início")
       return "Fim"
       print("Esta linha não será executada")

   print(exemplo())  # Saída: "Início" e depois "Fim"
   ```

- Python permite retornar múltiplos valores ao mesmo tempo, usando uma tupla.
   ```python
   def calculos(a, b):
       soma = a + b
       produto = a * b
       return soma, produto

   resultado_soma, resultado_produto = calculos(3, 4)
   print(resultado_soma)   # Saída: 7
   print(resultado_produto) # Saída: 12
   ```

- Exemplo da aula:
```` py
def soma(x, y):
    if x > 10:
        return [10, 20, 30]
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma1 + soma2)

print(soma(11, 2))
````

