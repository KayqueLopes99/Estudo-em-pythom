from abc import abstractmethod, ABC
from random import randint

class Conta(ABC):
    LIMITE_DO_BANCO = 3500
   
    def __init__(self, titular, agencia=None, conta='', saldo=0):
        self.titular = titular  # sairrrrrrrrrrr
        self.agencia = agencia if agencia else randint(10000, 50000)
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor 
    
    def depositar(self, valor):
        if valor <= 0:
            print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
            return None

        saldo_atual = self.saldo
        limite_atual = self.LIMITE_DO_BANCO

        # Verifica se o novo saldo ultrapassa o limite do banco
        if saldo_atual + valor > limite_atual:
            print(f"\033[91mErro: O saldo total não pode ultrapassar o limite do banco ({limite_atual}).\033[m")
            return None

        # Atualiza o saldo com o depósito
        saldo_atual += valor

        # Atualiza o saldo da conta
        self.saldo = saldo_atual

        print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {self.saldo:.2f}, Limite disponível: {limite_atual:.2f}\033[m")
        return self.saldo
    
    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
            return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    LIMITE_DO_BANCO = 10000

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: O valor {valor} é inválido. Informe um valor maior que zero.")
            return None
        
        saldo_atual = self.saldo + self.LIMITE_DO_BANCO  # Saldo total disponível, incluindo o limite

        print(f"O saldo atual da conta: {saldo_atual:.2f}")

        # Verifica se o saldo disponível é suficiente para o saque
        if saldo_atual < valor:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            print(f"Limite na conta: {-self.LIMITE_DO_BANCO:.2f}")
            return None
        
        # Realiza o saque se o saldo for suficiente
        self.saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo:.2f}")
        
        return self.saldo


class ContaCorrente(Conta):
    
    def __init__(self, titular, agencia, conta, saldo=0, limite=0):
        super().__init__(titular, agencia, conta, saldo)
        self.limite = limite

    
    
    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: O valor {valor} é inválido. Informe um valor maior que zero.")
            return None
        
        saldo_disponivel = self.saldo + self.limite  # Total disponível para saque, considerando o limite
        if valor > saldo_disponivel:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            print(f"Limite na conta: {-self.limite:.2f}")
            return None
        
        # Realiza o saque se o saldo for suficiente
        self.saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo:.2f}")
        
        return self.saldo



if __name__ == "__main__":
    conta_poupanca_01 = ContaPoupanca("Kayque", 11111, 222)
    conta_poupanca_01.depositar(1)  
    conta_poupanca_01.sacar(253)
#    conta_poupanca_01.depositar(100)
    print("-")

    conta_corrente_01 = ContaCorrente("Felipe", 23333, 777, 0, 350)
    conta_corrente_01.depositar(100)  
    conta_corrente_01.sacar(450)
    conta_corrente_01.sacar(450)
    print("-")

