from random import randint
from pathlib import Path
from file import ArquivoConta

class Conta():
  LIMITE_MAXIMO = 50000
  arquivo = ArquivoConta()

  def __init__(self, cpf=0, titular='', agencia="", saldo_inicial=0, tipoConta = ""):
        self.cpf = cpf
        self.numero_conta = randint(10000, 50000)
        self.titular = titular
        self.saldo = saldo_inicial
        self.agencia = agencia 
        self.tipoConta = tipoConta

  def depositar(self, valor):
    dados = self.arquivo.ler(self.cpf)
    if not dados:
        print(f"\033[91mErro: Conta com CPF {self.cpf} não encontrada.\033[m")
        return None
    saldo_atual = float(dados[3])


    if saldo_atual >= self.LIMITE_MAXIMO:
        print(f"\033[91mErro: Limite máximo de depósito atingido para a conta com CPF {self.cpf}.\033[m")
        return None

    if valor <= 0:
        print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
        return None
    
    novo_saldo = saldo_atual + valor

    # Atualiza o arquivo com o novo saldo
    self.arquivo.escrever(self.cpf, dados[1], dados[2], novo_saldo, dados[4])

    print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {novo_saldo:.2f}\033[m")
    return novo_saldo
  
  def imprimir_dados(self):
      self.arquivo.imprimir()

  def criar_conta(self):
      self.arquivo.escrever(self.cpf, self.titular, self.agencia, self.saldo, self.tipoConta)
      print(f"\033[92mConta criada com sucesso! Número da conta: {self.numero_conta}\033[m")

class ContaPoupanca(Conta):    
    def __init__(self, cpf, titular, agencia, saldoInicial=0, tipoConta="Conta Poupança"):
        super().__init__(cpf, titular, agencia, saldoInicial, tipoConta)
        
    
   
    def depositar(self, valor):
        return super().depositar(valor)


    def sacar(self, valor):
        dados = self.arquivo.ler(self.cpf)
        if not dados:
           print(f"033[91mErro: Conta com CPF {self.cpf} não encontrada.\033[m")
           return None

        self.saldo = float(dados[3])

        if valor <= 0:
            print(f"033[91mErro: O valor {valor} é inválido. Informe um valor maior que zero.\033[m")
            return None
         
        print(f"O saldo atual da conta: {self.saldo:.2f}")

        if valor > self.saldo:
            print(f"033[91mErro: Saldo insuficiente para realizar o saque de {valor}.\033[m")
            return None
        
        self.saldo -= valor
        self.arquivo.escrever(self.cpf, self.titular, self.agencia, self.saldo, self.tipoConta)

        print(f"Saque de {valor:.2f} realizado com sucesso! Novo saldo: {self.saldo:.2f}")
        return self.saldo
    
class ContaCorrente(Conta):

    LIMITE_DO_BANCO_CREDITO = 20000
    def __init__(self, cpf=0, titular='', agencia="", saldoInicial=0, tipoConta="Conta Corrente"):
        super().__init__(cpf, titular, agencia, saldoInicial, tipoConta)
        self.limite = self.LIMITE_DO_BANCO_CREDITO
        self.limite_utilizado = False

    def depositar(self, valor):
        return super().depositar(valor)
    
    def sacar(self, valor):
        dados = self.arquivo.ler(self.cpf)
        if not dados:
           print(f"\033[91mErro: Conta com CPF {self.cpf} não encontrada.\033[m")
           return None
        
        self.saldo = float(dados[3])
        saldo_disponivel = self.saldo + self.limite  

        if valor <= 0:
            print(f"\033[91mErro: O valor {valor} é inválido. Informe um valor maior que zero.\033[m")
            return None
        

        print(f"O saldo atual da conta: {self.saldo:.2f} | Limite disponível: {self.limite:.2f}")

        if valor > saldo_disponivel:
            print(f"\033[91mErro: Saldo insuficiente para realizar o saque de {valor}.\033[m")
            return None
        
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            diferenca = valor - self.saldo  
            self.saldo = 0  
            self.limite -= diferenca  
        
        self.arquivo.escrever(self.cpf, self.titular, self.agencia, self.saldo, self.tipoConta)
        print(f"Saque de {valor:.2f} realizado com sucesso! Novo saldo: {self.saldo:.2f} | Novo limite: {self.limite:.2f}")


        return self.saldo

 


    

    

# if __name__ == "__main__":

    
#main -- teste
conta = ContaPoupanca(cpf=123456789, titular="João", agencia="1234", saldoInicial=1000)
conta.criar_conta()
conta.depositar(valor=500)
conta.sacar(valor=200)
conta.imprimir_dados()

conta1 = ContaPoupanca(cpf=123, titular="Joana", agencia="1234", saldoInicial=3000)
conta1.criar_conta()
conta1.depositar(valor=500)
conta1.sacar(valor=200)
conta1.imprimir_dados()


conta1 = ContaCorrente(cpf=12334565, titular="hili", agencia="1234", saldoInicial=3000)
conta1.criar_conta()
conta1.depositar(valor=-500)
conta1.sacar(valor=-20000)
conta1.imprimir_dados()


# Tratativas para o valor e os demais atributos - cpf=0, titular='', agencia=""