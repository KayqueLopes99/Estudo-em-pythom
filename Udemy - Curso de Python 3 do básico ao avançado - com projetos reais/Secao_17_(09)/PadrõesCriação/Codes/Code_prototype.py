"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""

# Obs
"""
Mutáveis (passados por referência)
  list
  set
  dict
  class (o usuário pode mudar isso)
  ...

Imutáveis (copiados)
  bool
  int
  float
  tuple
  str
  ...
"""

from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":

    kayque = Person('José', 'Lopes')
    endereco_kayque = Address('Av. Brasil', '250A')
    kayque.add_address(endereco_kayque)

    esposa_kayque = kayque.clone()
    esposa_kayque.firstname = 'Letícia'

    print(kayque)
    print(esposa_kayque)