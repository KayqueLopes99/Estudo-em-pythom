from random import randint
from random import randint
from FileAccount import FileAccount

def error_message(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def success_message(text: str) -> None:
    print(f"\033[92m{text}\033[m")


class BankAccount:
    file: FileAccount = FileAccount()
    MAXLIMIT: int = 50000  
    
    cpf: str
    accountHolder: str
    branch: str
    initialBalance: float
    accountType: str

    def __init__(self, cpf: str = "", accountHolder: str = '', branch: str = "", initialBalance: float = 0.0, accountType: str = ""):
        self.__cpf: str = cpf
        self.__accountNumber: int = randint(100000, 500000)
        self.__accountHolder: str = accountHolder
        self.__branch: str = branch
        self.__balance: float = initialBalance
        self.__accountType: str = accountType

    @property
    def cpf(self):
        return self.__cpf

    @property
    def accountNumber(self):
        return self.__accountNumber

    @property
    def accountHolder(self):
        return self.__accountHolder

    @property
    def branch(self):
        return self.__branch

    @property
    def balance(self):
        return self.__balance

    @property
    def accountType(self):
        return self.__accountType

    @accountType.setter
    def accountType(self, value):
        self.__accountType = value
        
    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @branch.setter
    def branch(self, value):
        self.__branch = value

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @accountType.setter
    def accountType(self, value):
        self.__accountType = value

    def __repr__(self) -> str:
        return f"\033[1;38;5;46mAccount: {self._accountNumber} | Holder: {self._accountHolder} | CPF: {self._cpf} | Branch: {self._branch} | Balance: {self._balance:.2f} | Type: {self._accountType}\033[m"

    def createAccount(self):
        self.file.white(self.cpf, self.accountNumber, self.accountHolder, self.branch, self.balance, self.accountType)
    
    def deposit(self, cpf: str, value: float) -> float:
      try:
        # Lê os dados da conta do arquivo
        dates = self.file.read(cpf)
        if not dates:
            print(f"\033[91mAccount with CPF {cpf} not found!\033[m")
            return None

        currentBalance: float = float(dates[4])  # índice 4 = saldo

        # Verifica se o depósito é maior que zero
        if value <= 0:
            print(f"\033[91mError: The value of deposit must be greater than zero\033[m")
            return None

        # Verifica se o depósito ultrapassaria o limite máximo
        if currentBalance >= self.MAXLIMIT:
            print(f"\033[91mError: Max limit reached for account with CPF {cpf}.\033[m")
            return None

        # Atualiza o saldo
        newBalance = currentBalance + value
        self.file.updateBalance(cpf, newBalance)

        print(f"\033[92mDeposit of {value:.2f} successfully carried out! New balance: {newBalance:.2f}\033[m")
        return newBalance

      except Exception as error:
        print(f"\033[91mError saving data: {error}\033[m")
        return None

 
    def withdraw(self, cpf: str, value: float):
        """Método genérico para saque"""
        raise NotImplementedError("Method withdraw need implemented.")
    
    @staticmethod
    def printDataAccount(cpf: str) -> None:
      fileRegister = FileAccount()
      accountData: list[str] | None = fileRegister.read(cpf)
        
      if accountData is None:
        error_message("Customer data not found or customer not registered.")
      else:
        print("\033[1;38;5;46m=== ACCOUNT DATA OF CLIENT ===\033[m")
        print(f"\033[1;38;5;46mCPF: {accountData[0].strip()}\033[m")
        print(f"\033[1;38;5;46mAccount Number: {accountData[1].strip()}\033[m")
        print(f"\033[1;38;5;46mAccount Holder: {accountData[2].strip()}\033[m")
        print(f"\033[1;38;5;46mBranch: {accountData[3].strip()}\033[m")
        print(f"\033[1;38;5;46mBalance: {accountData[4].strip()}\033[m")
        print(f"\033[1;38;5;46mAccount Type: {accountData[5].strip()}\033[m")

    
        
    
    
 
class CheckingAccount(BankAccount):
    BANK_CREDIT_LIMIT: int = 20000

    def __init__(self, cpf: str = "", accountHolder: str = "", branch: str = "", initialBalance: float = 0.0, accountType: str = "Checking Account"):
        super().__init__(cpf, accountHolder, branch, initialBalance, accountType)
        self.limit: int = self.BANK_CREDIT_LIMIT
        
  
    def withdraw(self, cpf: str, value: float) -> None:
        try:
            dates = self.file.read(cpf)
            if not dates:
                print(f"\033[91mAccount with CPF {cpf} not found!\033[m")
                return None

            currentBalance: float = float(dates[4])
            available_balance = currentBalance + self.limit  # saldo + limite

            if value <= 0:
                print(f"\033[91mError: The value of withdraw must be greater than zero\033[m")
                return None

            print(f"Current balance: {currentBalance:.2f} | Limit: {self.limit:.2f}")

            if value > available_balance:
                print(f"\033[91mError: Insufficient balance to withdraw {value:.2f}.\033[m")
                return None

            newBalance: float
            if value <= currentBalance:
                newBalance = currentBalance - value
            else:
                difference = value - currentBalance
                newBalance = 0
                self.limit -= difference  # atualiza o limite

            self.file.updateBalance(cpf, newBalance)

            print(f"\033[92mWithdrawal of {value:.2f} successfully carried out! New balance: {newBalance:.2f} | Remaining limit: {self.limit:.2f}\033[m")

        except Exception as error:
            print(f"\033[91mError saving data: {error}\033[m")
            return None

        
    
    


        
class SavingsAccount(BankAccount):
  def __init__(self, cpf: str = "", accountHolder: str = "", branch: str = "", initialBalance: float = 0.0, accountType: str = "Savings Account"):
        super().__init__(cpf, accountHolder, branch, initialBalance, accountType)
        
  def withdraw(self, cpf: str, value: float) -> None:
    try:
        dates = self.file.read(cpf)
        if not dates:
            print(f"\033[91mAccount with CPF {cpf} not found!\033[m")
            return None

        currentBalance: float = float(dates[4])  

     
        if value <= 0:
            print(f"\033[91mError: The value of withdraw must be greater than zero\033[m")
            return None

        print(f"Current balance: {currentBalance:.2f}")

        if value > currentBalance:
            print(f"\033[91mError: Insufficient balance to withdraw {value:.2f}.\033[m")
            return None

        newBalance = currentBalance - value
        self.file.updateBalance(cpf, newBalance)

        print(f"\033[92mWithdrawal of {value:.2f} successfully carried out! New balance: {newBalance:.2f}\033[m")

    except Exception as error:
        print(f"\033[91mError saving data: {error}\033[m")
        return None

    