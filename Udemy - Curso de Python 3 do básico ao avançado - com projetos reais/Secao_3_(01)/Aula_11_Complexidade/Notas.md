## Variáveis, constantes e complexidade de código
- Métodos de código limpo.
- Constante, uso de letras maisculas `ABC`, indicando que isso não vai mudar. 
- CONSTANTE = "Variaveis" que não vão mudar.
- Muitas condições no mesmo if (ruim)
- Quando mais dictante do inicio da linha maior a complexidade (ruim).
- Quebrar linha `\` no código, para falar que ele vai continuar na próxima.

``` python
velocidade = 61 # velocidade atual do carro.
local_carro = 90 # local em que o carro está na estrada.

RADAR_1 = 60 # VELICIDADE MÁXIMA DO RADAR 1.
LOCAL_1 = 100 # LOCAL ONDE O  radar 1 está.
RADAR_RANGE = 1 # A distância onde o radar pega.

if velocidade > RADAR_1
```

- As variaveis com condições é uma boa prática quando a condição se repete.
- As variaveis com condições não é para resumir o código e sim qualificar.
- Linha ou comandos gradas fragmenta-se para entendimento futuro. 
- Variaveis não podem ser declaradas dentro do bloco de código.