# Operadores lógicos 
## Operador Lógico "and"
- and (e) - Todas as condições precisam ser verdadeiras `True`.
- Retorna True (boll) se ambas as condições forem verdadeiras.
- Se uma condição for False retorna a False(boll)
    ```python
    x = 5
    print(x > 3 and x < 10)  # Saída: True
    ```
- Todas as condições precisam ser verdadeiras.
- Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

- São considerados falsy (que vc já viu) -> 0 0.0 '' (Quando você confronta ele com bool são falso) False.
- Também existe o tipo None que é usado para representar um não valor

- Ele vai avaliar as duas codições
- Avaliação de curto circuito, ipo ele achou a expressão falsa todos serão falso, logo ele não confere a condição do código inteiro. 
```` python
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if condicao1 and condicao2: <Sintaxe.>

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
# Ele vai parar no 0 pois virou false
print(True and 0 and True)
````


## Operador Lógico "or"
- or (ou): 
- Retorna True se pelo menos uma das condições for verdadeira.
-  or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
- Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
- São considerados falsy (que vc já viu) 0 0.0 '' False.
- Também existe o tipo None que é
- usado para representar um não valor

````python
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
````

```python
x = 5
print(x > 3 or x > 10)  # Saída: True
```
- Envolver entre paranteses para precedência para essa condição ser avaliada primeiro. 
- Retorna ao valor verdadeiro.

- No proprio `ìnput()`
``` python
senha = input('Senha: ') or 'Sem senha' # Se ele não digitar nada coloca Sem senha.
print(senha)
```
## Operador lógico "not"
- not (não).
- Operador lógico "not"
- Usado para inverter expressões:
- not True = False
- not False = True
- Se ele NÃO está de acordo com algo.
    ```python
    x = 5
    print(not(x > 3 and x < 10))  # Saída: False
    ```

````python
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
p = (n1 > n2)
q = (n1 != n2)
r = not (p or q) and (not p)
print('p =', p)
print('q =', q)
print('r =', r)
````

## Operadores in e not in
- in: está entre.
- Strings são iteráveis (Navegar Item por Item).
- Se um Item está ou não está no Local escolhido podendo ser uma variavel, estrutura e etc
- not in: não está entre. 
- Começo do Zero.
```
 0 1 2 3 4 5
 O t á v i o
-6-5-4-3-2-1
```

- tipo(Varíavel[indice]) -> Retorna a Letra.
- Sintaxe:
```
Item in Local
```
- Retorna a um boll(False ou True).

```python
nome = 'Kayque'
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[-3])
print(nome[-2])
print(nome[-1])

print("-" * 10)

print('que' in nome) # True
print('Ky' in nome) # False
print("-" * 10) 
print('que' not in nome) # False
print('Ky' not in nome) # True

nome = input("Digite seu nome: ")
encontrar = input("Digite o ue deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está no seu Nome {nome}.")
else:
    print(f"{encontrar} não está em {nome}")
```


## Comando In 2.0:
- O operador **`in`** em Python é utilizado para verificar se um determinado elemento está presente em uma sequência, estrutura de dados ou iterável. Ele retorna um valor **booleano (`True` ou `False`)**, dependendo da existência do item.

- Sintaxe:

```python
elemento in estrutura
```

- Verificando a Presença de um Item em uma Lista
- Verificando em Tuplas
- Verificando em Conjuntos (`set`)
- Verificando a Existência de uma Chave em um Dicionário
- Verificando Caracteres em Strings

📌 Para grandes coleções, **prefira `set` ao invés de `list`**