## Introdução aos tipos de dados
- Python = Linguagem de programação Dinâmica e Forte.
- O tipo pode ser atribuido dinamicamente pelo python.

## Tipo str (string)
- str -> string -> Texto
- Strings são textos que estão dentro de aspas simples `''`ou duplas `""`.
-Exemplo:
``` python
print('Kayque "Lopes"')
```
- Sequências de caracteres.


## Tipo int (inteiros)
- int -> Número inteiro.
- O tipo int representa qualquer número Positivo ou Negativo.
- Int sem sinal é considerado positivo.
- Inteiros **(int)**: São números sem casas decimais. 
``` python
# print(Numero_Inteiro)
print(19)
```

## Tipo Float (Flutuante ou Real)
- float -> Número com ponto flutuante.
- O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
- float sem sinal é considerado positivo.
- Não se utiliza a `,` e sim o `.`.
``` python
# print(Numero_Flutuante)
print(1.1, 10.11)
print(0.0, -1.5)
```
## A função **type()** (Saber a tipagem)
- Mostra o tipo da varíavel que o Python inferiu ao valor.
``` python
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
```
- Tudo em python é um objeto.

```` python
# É usado para verificar o tipo da variável.
#- Exemplo:
x = 10
y = 3.14
z = "Olá, mundo!"
w = True

print(type(x))  # saída: <class 'int'>
print(type(y))  # saída: <class 'float'>
print(type(z))  # saída: <class 'str'>
print(type(w))  # saída: <class 'bool'>
````

# Tipo Boll (Boolean)
- Tipo de dado bool (boolean)
- Ao questionar algo em um programa, só existem duas respostas possíveis:
- sim (True) ou não (False).
- São valores lógicos que podem ser `True` (verdadeiro) ou `False` (falso). 
- Existem vários operadores lógicos para "questionar".
- Dentre eles o ==, que é um operador lógico que questiona se um valor é igual a outro.
- Mudar o fluxo do programa `Se for sim ou não` a execução vai para outro local do código.

``` python
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))
```
## Coerção de tipos (convertendo um tipo para outro)
- Conversão de tipos, coerção, type convertion, typecasting, coercion.
- É o ato de converter um tipo em outro tipos imutáveis e primitivos:
- str, int, float, bool.


``` python
int()
float()
str()
bool()
```
- Imutaveis e primitivos.


## Imprecisão dos números de ponto flutuante + round e decimal.Decimal
- Em operações matemáticas `0.1 + 0.7 = 0.79999999`, com a formatação o resultado será `0.8`.
- 1* formataçao do resultado final `{numero:.casas_decimais.f}`.
- 2* Comando **`round`** -> recebe o número e no segundo argumento é o número de casas decimais.
- 3* import decimal: ``decimal.Decimal(numero)``.
- exemplo
``` python
"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
```


