from random import randint
from random import randint
from FileAccount import FileAccount
class BankAccount:
    file: FileAccount = FileAccount()
    MAXLIMIT: int = 50000  
    
    cpf: str
    accountHolder: str
    branch: str
    initialBalance: float
    accountType: str

    def __init__(self, cpf: str = "", accountHolder: str = '', branch: str = "", initialBalance: float = 0.0, accountType: str = ""):
        self.cpf: str = cpf
        self.accountNumber: int = randint(100000, 500000)
        self.accountHolder: str = accountHolder
        self.branch: str = branch
        self.balance: float = initialBalance
        self.accountType: str = accountType


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
 
class CheckingAccount(BankAccount):
    BANK_CREDIT_LIMIT: int = 20000

    def __init__(self, cpf: str = "", accountHolder: str = "", branch: str = "", initialBalance: float = 0.0, accountType: str = "Checking Account"):
        super().__init__(cpf, accountHolder, branch, initialBalance, accountType)
        self.limit: int = self.BANK_CREDIT_LIMIT
        self.limitUsed: bool = False


        
class SavingsAccount(BankAccount):
    def __init__(self, cpf: str = "", accountHolder: str = "", branch: str = "", initialBalance: float = 0.0, accountType: str = "Savings Account"):
        super().__init__(cpf, accountHolder, branch, initialBalance, accountType)
    