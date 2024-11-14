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
