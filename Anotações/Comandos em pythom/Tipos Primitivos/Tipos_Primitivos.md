## Tipos Primitivos e Saída de dados:

# Int
. Conversão para um número inteiro.
. Inteiros (int)**: São números sem casas decimais. 
. Para receber um inteiro do usuário, temos `int()`.
. Assim, iremos converter a entrada do usuário em um número inteiro. 

. Exemplo com sintaxe:
- x = int(input('Digite um número inteiro: ')) # O número digitado pelo usuário será armazenado na variável.

# None
. Definição  de uma varíavel sem valor em um dado momento ou para sempre.
. Exemplo:
``` python
variavel = None  # Definindo

```
# FLOAT
. Números de ponto flutuante (float).
. São números com casas decimais. 
Para receber um número de ponto flutuante do usuário, temos `float()`. 

. Exemplo com sintaxe:
- altura = float(input('Digite sua altura: ')) # A altura digitada pelo usuário será armazenada na variável.

# Str
. Strings (str) são sequências de caracteres.
. Para receber uma string do usuário, temos `input()`. 
. Exemplo com sintaxe:
nome = input('Digite seu nome: ') # O nome digitado pelo usuário será armazenado na variável.

# Boll
. Booleanos (bool).
. São valores lógicos que podem ser `True` (verdadeiro) ou `False` (falso). 
. Para receber um valor booleano do usuário, precisamos comparar.
. Aqui está um exemplo:
- is_true = input('Digite True ou False: ') == 'True'
- O programa pedirá ao usuário para digitar "True" ou "False".
- Se o usuário digitar "True", a variável `is_true` será `True`. 
- Se o usuário digitar qualquer outra coisa, a variável `is_true` será `False`.

# Lower
. Converter todos os caracteres de uma string para minúsculas. 
. Símbolos e números são ignorados.

. Sintaxe:
- string_name.lower()

. Exemplo:
texto = "Hello my FRIENDS"
xyz = txt.lower()
print(xyz)  # Saída será "hello my friends"

# Type
. É usado para verificar o tipo da variável.
- Exemplo:
x = 10
y = 3.14
z = "Olá, mundo!"
w = True

print(type(x))  # saída: <class 'int'>
print(type(y))  # saída: <class 'float'>
print(type(z))  # saída: <class 'str'>
print(type(w))  # saída: <class 'bool'>

# isnumeric()
. Verificar se tem apenas caracteres numéricos.
. Retorna a `True` se  numéricos (0-9), e `False` caso contrário.
. Sintaxe: 
string.isnumeric()

- Exemplo:
```python
num = input ("Digite algo:")
print(num.isnumeric()) 
```
# Comandos de teste de tipo:

1. isinstance(): Verifica se um objeto é de um determinado tipo.
    - Sintaxe: `isinstance(object, type)`

2. isdigit(): Verifica se uma string contém apenas dígitos.
    - Sintaxe: `string.isdigit()`

3. isalpha(): Verifica se uma string contém apenas caracteres alfabéticos.
    - Sintaxe: `string.isalpha()`

4. isalnum(): Verifica se uma string contém apenas caracteres alfanuméricos.
    - Sintaxe: `string.isalnum()`

5. isdecimal(): Verifica se uma string contém apenas caracteres decimais.
    - Sintaxe: `string.isdecimal()`

6. isnumeric(): Verifica se uma string contém apenas caracteres numéricos.
    - Sintaxe: `string.isnumeric()`

7. isidentifier(): Verifica se uma string é um identificador válido em Python.
    - Sintaxe: `string.isidentifier()`

8. isprintable(): Verifica se todos os caracteres na string são imprimíveis ou a string está vazia.
    - Sintaxe: `string.isprintable()`

9. isspace(): Verifica se a string contém apenas espaços em branco².
    - Sintaxe: `string.isspace()`

10. islower(): Verifica se todos os caracteres na string estão em minúsculas².
    - Sintaxe: `string.islower()`

11. isupper(): Verifica se todos os caracteres na string estão em maiúsculas².
    - Sintaxe: `string.isupper()`

12. istitle(): Verifica se a string é um título².
    - Sintaxe: `string.istitle()`
