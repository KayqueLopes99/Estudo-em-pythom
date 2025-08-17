import datetime
from Tratatives import Tratatives
from datetime import datetime
 
class Person:
    name: str
    dateOfBirth: datetime.date
    cpf: str
    address: str
    email: str

    def __init__(self, name: str = "", dateOfBirth: datetime.date = None, cpf: str = "", address: str = "", email: str = ""):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__cpf = cpf
        self.__address = address
        self.__email = email


    # Name property
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, newName: str) -> None:
        self.__name = newName

    # Date of Birth property
    @property
    def dateOfBirth(self) -> datetime.date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, newDate: datetime.date) -> None:
        self.__dateOfBirth = newDate

    # CPF property
    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, newCpf: str) -> None:
        self.__cpf = newCpf

    # Address property
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, newAddress: str) -> None:
        self.__address = newAddress

    # Email property
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, newEmail: str) -> None:
        self.__email = newEmail
    


    def __repr__(self) -> str:
        return f"\033[1;38;5;46mClient Data: Name - {self.name} - CPF: {self.cpf} - Date of Birth: {self.dateOfBirth} - Address: {self.address} - Email: {self.email}.\033[m"
