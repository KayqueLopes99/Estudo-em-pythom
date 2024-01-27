## Operadores Aritméticos
Os operadores aritméticos em Python:

- Adição(+): `a + b`
- Subtração(-): `a - b`
- Multiplicação(*): `a * b`
- Divisão(/): `a / b`
- Exponenciação(**): `a ** b`
- Quociente da divisão (ou divisão inteira)(//): `a // b`
- Módulo (ou resto da divisão)(%): `a % b`
- == é usado para verificar a igualdade entre dois valores.

## Ordem de precedência
. Primeiro: ()
. Segundo: **
. Terceiro: * / // %
. Quarto: + - 
 
# Podemos deixar a formula para calcular primeiro a soma ou qualquer outra oparação
- ex: (2 * (2+4)) 

## OUTRAS OPERAÇÕES COM MATH
1. Potência pow: A função pow(x, y) retorna numero_1 elevado à potência numero_2.
    ```python
    import math
    print(math.pow(numero_1, numero_2))
    # Ou pow(numero_1, numero_2)
    ```

2. Raiz Quadrada sqrt: A função sqrt(x) retorna a raiz quadrada de numero_1.
    ```python
    import math
    print(math.sqrt(numero_1))
    ```


# Curiosidade 
.Multiplicação de uma letra por um número inteiro.
```python 
numero_1 = str(input('Digite um caractere: \n'))
numero_2 = int( input('Digite um algarismo: \n'))

print("multiplicacao = ", numero_1 * numero_2)
```

