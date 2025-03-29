from abc import abstractmethod, ABC
from random import randint

class Conta(ABC):
    LIMITE_DO_BANCO = 3500
   
    def __init__(self, agencia=None, conta=0, saldo=0):
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
    LIMITE_DO_BANCO = 10000  # Limite inicial

    def __init__(self, agencia, conta, saldo=0):
        super().__init__(agencia, conta, saldo)
        self.limite = self.LIMITE_DO_BANCO  # Inicializa o limite da conta
        

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: O valor {valor} é inválido. Informe um valor maior que zero.")
            return None
        
        saldo_disponivel = self.saldo + self.limite  # Total disponível para saque

        print(f"O saldo atual da conta: {self.saldo:.2f} | Limite disponível: {self.limite:.2f}")

        if valor > saldo_disponivel:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            return None
        
        # Primeiro usa o saldo disponível
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            diferenca = valor - self.saldo  # Quanto falta além do saldo?
            self.saldo = 0  # Zera o saldo
            self.limite -= diferenca  # Usa o limite disponível

        print(f"Saque de {valor:.2f} realizado com sucesso! Novo saldo: {self.saldo:.2f} | Novo limite: {self.limite:.2f}")
        
        return self.saldo
    def obter_saldo_e_limite(self):
        return f"Conta Poupança - Saldo: {self.saldo:.2f} - Limite Disponível: {self.limite:.2f}"

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
    
    def obter_dados_conta(self):
        """Retorna os dados da conta poupança como uma lista de dicionários."""
        return [{
            "tipo": "Conta Poupança",
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self.saldo,
            "limite": self.limite
        }]


class ContaCorrente(Conta):
    LIMITE_DA_CONTA_CORRENTE = 4000
    def __init__(self, agencia, conta, saldo=0, limite=LIMITE_DA_CONTA_CORRENTE):
        super().__init__(agencia, conta, saldo)
        self.limite = limite  # Limite personalizado para a conta corrente

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: O valor {valor} é inválido. Informe um valor maior que zero.")
            return None
        
        saldo_disponivel = self.saldo + self.limite  # Total disponível para saque

        print(f"O saldo atual da conta: {self.saldo:.2f} | Limite disponível: {self.limite:.2f}")

        if valor > saldo_disponivel:
            print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
            return None

        # Primeiro usa o saldo disponível
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            diferenca = valor - self.saldo  # Quanto falta além do saldo?
            self.saldo = 0  # Zera o saldo
            self.limite -= diferenca  # Usa o limite disponível

        print(f"Saque de {valor:.2f} realizado com sucesso! Novo saldo: {self.saldo:.2f} | Novo limite: {self.limite:.2f}")

        return self.saldo
    
    def obter_saldo_e_limite(self):
        return f"Conta Corrente - Saldo: {self.saldo:.2f} - Limite Disponível: {self.limite:.2f}"
    
    def obter_dados_conta(self):
        """Retorna os dados da conta corrente como uma lista de dicionários."""
        return [{
            "tipo": "Conta Corrente",
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self.saldo,
            "limite": self.limite
        }]
    
     # Função para adicionar a conta à lista de contas cadastradas
    def adicionar_conta(self, conta: Conta):
        dados_conta = conta.obter_dados_conta()
        # Exibe os dados da conta a ser adicionada
        print("Dados da Conta a ser adicionada:")
        for dados in dados_conta:
            print(dados)
        
        # Adiciona a conta à lista de contas
        self.contas.append(conta)
        print(f"\033[92mConta adicionada com sucesso! Agora temos {len(self.contas)} contas cadastradas.\033[m")
    

    



    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
            return f'{class_name}{attrs}'







