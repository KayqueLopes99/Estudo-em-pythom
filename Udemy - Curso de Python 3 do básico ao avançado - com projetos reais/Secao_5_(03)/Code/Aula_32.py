from collections import namedtuple
from typing import NamedTuple
class Carta(NamedTuple):
    valor: str = 'VALOR_PADRÃO'
    naipe: str = 'NAIPE_PADRÃO'


as_espadas = Carta('A')

## Como é uma Tupla pode-se: 
print(as_espadas)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)

# Percorrer
for valor in as_espadas:
    print(valor)

# fields
print(as_espadas._fields)
print(as_espadas._field_defaults) # Mostra os valores padrão.


print(as_espadas._asdict())



