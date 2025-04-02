## Operadores de Identidade
- São operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória. 

## id - A identidade do valor que está na memória
- COMO BUSCAR A VARÍAVEL. 
- A identidade das elemento no python.
- O comando `id()` mostra o local(identidade) na memória.
- Varíaveis com o mesmo valor atribuido vai mostrar o mesmo id() => (As varíaveis apontam para um local na memória).

``` python
v1 = 'A'
v2 = 'A'

print(id(v1))
print(id(v2))

```
- id = Identidade
## Flags, is, is not e None
- Flag (Bandeira) - Marcar um local.
- As vezes precisamos saber o local onde o interpretador passou no código(condições ...) e precisamos marca-lo.
- Usando none e is, is not é uma alternativa para ver se passou no local `Condição ou outro bloco de código.` 
- Saber se interpretador se ele entrou ou não na condição, pode-se criar uma variavel dentro do bloco, isto é ruim.
- Deve-se declarar fora do bloco para não depender da condição ou fluxo, logo definimos com `none`.

- None = Não valor.
- Definição  de uma varíavel sem valor em um dado momento ou para sempre.
- Exemplo:
``` python
variavel = None  # Definindo
```

## Comando is 
- O comando is em Python é um operador de identidade usado para comparar se duas variáveis apontam para o mesmo objeto na memória.
- **is e is not =--> é (sim eles ocupam) ou não é (não eles não ocupam), (tipo, valor, identidade).**
- is none = Passou no local.
- is not none = Não passou no local.
- Usado com o `none`

``` python
condicao = True # False.
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo.")
else:
    print("Não faça algo.")

if passou_no_if is None:
    print("Não passou no if.")

if passou_no_if is not None:
    print("Não passou p if.")
# Colocar uma bandeira em determinado local do código, usa-se o None para verificar se essa varíavel em ou não valor(Bandeira está ou não fincada).
# Is e is not checa o id do objeto na memória. 
```