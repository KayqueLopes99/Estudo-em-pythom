## Variáveis, constantes e complexidade de código
- Métodos de código limpo.
- **Constante, uso de letras maisculas** `ABC`, indicando que isso não vai mudar. 
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

- **Constantes são usadas em o que será fixo no código**
+ 1. O padrão de nomes deve ser snake case, OU SEJA USAR O **_** para separar ou separar deixando as primeira letras maiusculas das palavras juntas: `CONSTANTE_01` ou `Contante01Primeira`.
- 2. Maiúsculo.
- 3. Nomes detalhados. 

```` Python
CONSTANTE_NUMERICA = 100
NomePesooa = 'Kayque'
print(CONSTANTE_NUMERICA)
limite_saque_diario = 1000

STATES = ["RN", "SP", "RJ"]
````


### variavel obs:
- Pode Sobrescrever uma varíavel a outra.
- Podemos definilas todas em uma mesma linha.
``` py
nome, idade = "kayque", 20
``` 