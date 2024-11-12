# Em Python:
## bin(numero_decimal)[2:]
## oct(numero_decimal)[2:]
## hex(numero_decimal)[2:]

# o [2:], é para retirar o 0b.
# Decimal:
- De base 10.
- 1234:
- 1 * 1000
- 2 * 100
- 3 * 10
- 4 * 1
- Somando tudo resultará em 1234.

>  Unidade 10^0
>  Dezenas 10^1
>  Centenas 10^2
>  Milhar 10^3

## Notação Posicional:
- Cada algariso tem um valor.
- Combinações numéricas.

# Binário:
- De base 2, pois 2^numero da casa.
- Contar: Direita para Esquerda.
- Tabela de conversão de decimal para binário para os números de 1 a 10:

| Decimal | Binário |
|---------|---------|
| 1       | 1       |
| 2       | 10      |
| 3       | 11      |
| 4       | 100     |
| 5       | 101     |
| 6       | 110     |
| 7       | 111     |
| 8       | 1000    |
| 9       | 1001    |
| 10      | 1010    |

##  Logo: binário -> decimal.
> 1 -> 1
> 2 -> 10
> 4 -> 100
> 8 -> 1000
> 16 -> 10000
> 32 -> 100000
> Duplicando ...

## Logo: Decimal -> Binário.
- Dividir por dois até chegar em zero se possivel.

- Vamos converter o número decimal 13 para binário:

| Divisão por 2 | Quociente | Resto |
|:-------------:|:---------:|:-----:|
|     13 / 2    |     6     |   1   |
|     6 / 2     |     3     |   0   |
|     3 / 2     |     1     |   1   |
|     1 / 2     |     0     |   1   |

- Aqui estão os passos:
1. Comece com o número decimal que você deseja converter (neste caso, 13).
2. Divida esse número por 2.
3. Anote o quociente e o resto.
4. Continue dividindo o quociente por 2 até que o quociente seja 0.
5. O número binário é a sequência de restos lida de baixo para cima (neste caso, 1101).

