from Person import Person
import datetime
from Tratatives import Tratatives
from FileClient import FileClient
from Accounts import BankAccount
def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")


class Client(Person):
    
    def __init__(self, name: str = "", dateOfBirth: datetime.date = None, cpf: str = "", address: str = "", email: str = ""):
        super().__init__(name, dateOfBirth, cpf, address, email)  
        self.__account: BankAccount | None = None
        
        @property
        def account(self):
            return self.__account
        
        @account.setter
        def account(self, value):
            self.__account = value
        
        
    
    def dateOfBirthRegister(self) -> str:
        valid = Tratatives()  
        fmt: str = "%d/%m/%Y"

        while True:
            print("Enter your date of birth (dd/mm/yyyy):")

            day: int = valid.validate_integer(input("Enter the day: "))
            
            if day is None:
                print("\033[91mInvalid day. Try again.\033[m")
                continue
            
            month: int = valid.validate_integer(input("Enter the month: "))
            
            if month is None:
                print("\033[91mInvalid month. Try again.\033[m")
                continue
            
            
            year: int = valid.validate_integer(input("Enter the year: "))

            if year is None:
                print("\033[91mInvalid year. Try again.\033[m")
                continue
            

            if not valid.validate_date_of_birth(day, month, year):
                print("\033[91mInvalid date. Try again.\033[m")
                continue

            try:
                
                date_obj = datetime.date(year, month, day)
                formatted_date = date_obj.strftime(fmt)
                print("\033[92mDate successfully registered!\033[m")
                return formatted_date
            except ValueError:
                print("\033[91mInvalid date. Try again.\033[m")


    
    def registerClient(self) -> None:
        fileRegister = FileClient()
        validator = Tratatives()
        tempDataStorage = []

        # Name
        while True:
            self.name = validator.validate_name(input("Please enter your full name: "))
            if self.name:
                break
            else:
                error_message("-"*30)

        # Date of Birth
        while True:
            self.dateOfBirth = self.dateOfBirthRegister()
            if self.dateOfBirth:
                break
            else:
                error_message("-"*30)

        # CPF
        while True:
            self.cpf = validator.validate_cpf(input("Please enter your CPF (numbers only): "))
            if self.cpf:
                break
            else:
                error_message("-"*30)

        # Email
        while True:
            self.email = validator.validate_email(input("Please enter your email address: "))
            if self.email:
                break
            else:
                error_message("-"*30)

        # Address
        self.address = input("Please enter your full address: ").title()
        if self.address == '':
            self.address = "Not Provided"



        tempDataStorage.append({
            "name": self.name,
            "dateOfBirth": self.dateOfBirth,
            "cpf": self.cpf,
            "email": self.email,
            "address": self.address,
            "registrationTime": self.registrationTime,
        })
        
        fileRegister.write(tempDataStorage)
        
        
    

        
    @staticmethod
    def listDatesOfClients() -> None:
        fileRegister = FileClient()
        fileRegister.listClients()
    
    @staticmethod
    def printDataClient(cpf: str) -> None:
      fileRegister = FileClient()
      data: list[str] | None = fileRegister.read(cpf)
    
      if data is None:
          error_message("Customer data not found or customer not registered.")
      else:
        cpf_value: str = data[0].strip()
        name: str = data[1].strip()
        date_str: str = data[2].strip()       
        email: str = data[3].strip()
        address: str = data[4].strip()
        
        date_of_birth =  datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        client: Person = Person(name, date_of_birth, cpf_value, address, email)
    
        print(client)

        
        