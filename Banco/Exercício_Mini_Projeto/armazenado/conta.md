
"""
    def obter_saldo_e_limite(self):
        return f"Conta Poupança - Saldo: {self.saldo:.2f} - Limite Disponível: {self.limite:.2f}"
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
    def obter_dados_conta(self):
        Retorna os dados da conta poupança como uma lista de dicionários
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
        self.limite = limite  

    
    
    def obter_saldo_e_limite(self):
        return f"Conta Corrente - Saldo: {self.saldo:.2f} - Limite Disponível: {self.limite:.2f}"
    
    def obter_dados_conta(self):
        Retorna os dados da conta corrente como uma lista de dicionários.
        return [{
            "tipo": "Conta Corrente",
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self.saldo,
            "limite": self.limite
        }]
    
    
    def adicionar_conta(self, conta: Conta):
        dados_conta = conta.obter_dados_conta()
       
        print("Dados da Conta a ser adicionada:")
        for dados in dados_conta:
            print(dados)
        
       
        self.contas.append(conta)
        print(f"\033[92mConta adicionada com sucesso! Agora temos {len(self.contas)} contas cadastradas.\033[m")
    

    



    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
            return f'{class_name}{attrs}'



"""
        

