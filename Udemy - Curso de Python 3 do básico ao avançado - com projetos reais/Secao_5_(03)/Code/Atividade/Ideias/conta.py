from abc import abstractmethod, ABC
from random import randint
from file import Arquivo

class Conta(ABC):
  LIMITE_DO_BANCO = 2500

  def __init__(self, titular, agencia=None, conta='', saldo=0, limite=LIMITE_DO_BANCO):
        self.titular = titular  
        self.agencia = agencia if agencia else randint(10000, 50000)
        self.conta = conta
        self.saldo = saldo
        self.limite = limite

  @abstractmethod
  def sacar(self, valor):
        self.saldo -= valor 
    
  def depositar(self, nome, valor):
    arquivo = Arquivo()

    if valor <= 0:
        print("\033[91mErro: O valor do depósito deve ser maior que zero.\033[m")
        return None

    # Lê os dados do arquivo TXT
    dados = arquivo.ler_ou_imprimir_dados()

    if not dados:
        print("\033[91mErro: Nenhuma conta encontrada.\033[m")
        return None

    conta_encontrada = None

    # Procura a conta do usuário
    for linha in dados:
       pessoa = dict(item.split(": ") for item in linha.strip().split("; "))  # Converte a linha para dicionário
    
       if pessoa.get('titular', '').lower() == nome.lower():  # Usa .get() para evitar erro
         conta_encontrada = pessoa
         break


    if conta_encontrada is None:
        print(f"\033[91mErro: Conta não encontrada para o usuário {nome}.\033[m")
        return None

    saldo_atual = float(conta_encontrada['saldo'])
    limite_atual = float(conta_encontrada['limite'])

    
    if saldo_atual < 0:
        valor_para_repor = min(abs(saldo_atual), valor)
        saldo_atual += valor_para_repor
        valor -= valor_para_repor
        limite_atual += valor_para_repor 

    if saldo_atual + valor > self.LIMITE_DO_BANCO:
       print(f"\033[91mErro: O saldo total não pode ultrapassar o limite do banco ({self.LIMITE_DO_BANCO}).\033[m")
       return None
    
    
    if valor > 0:
        saldo_atual += valor

    # Atualiza a conta com os novos valores
    conta_encontrada['saldo'] = f"{saldo_atual:.2f}"
    conta_encontrada['limite'] = f"{limite_atual:.2f}"

    # Atualiza os dados no arquivo TXT
    arquivo.atualizar_saldo_limite(nome, novo_saldo=conta_encontrada['saldo'], novo_limite=conta_encontrada['limite'])

    print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {conta_encontrada['saldo']}, Novo limite disponível: {conta_encontrada['limite']}\033[m")
    return conta_encontrada['saldo']




  def adiciona_dados_da_conta(self):
        arquivo = Arquivo()

        # Cria os dados da nova conta
        dados_nova_conta = {
            "agencia": self.agencia,
            "saldo": self.saldo,
            "limite": self.limite,
            "conta": self.conta,
            "titular": self.titular  

        }

        arquivo.escrever_dados([dados_nova_conta])

        print(f"\033[92mConta criada com sucesso para {self.titular}. Número da conta: {self.conta}\033[m")
        return dados_nova_conta
    
  def obter_saldo(self, nome):
       arquivo = Arquivo()
       linhas = arquivo.ler_ou_imprimir_dados()  # Lê as linhas do arquivo

       if not linhas:  
         print("\033[91mNenhuma conta encontrada.\033[m")
         return None

    # Percorre as linhas e converte para dicionário
       for linha in linhas:
         dados = dict(item.split(": ") for item in linha.strip().split("; "))  # Converte a string em dicionário
        
         if dados.get('titular') == nome:  # Usa .get() para evitar KeyError
            return float(dados.get('saldo', 0))  # Retorna o saldo como float

       print(f"\033[91mNenhuma conta encontrada para o titular {nome}.\033[m")
       return None
    



class ContaPoupanca(Conta):

    def cria_conta(self):
        return self.adiciona_dados_da_conta()  

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(Saque: {valor})")
            return self.saldo
        
        print("Não foi possível sacar o valor desejado.")
        self.detalhes(f"(Saque Negado {valor}.)")



if __name__ == "__main__":
    conta_poupanca_01 = ContaPoupanca("Kayque", 11111, 222, 0)
    conta_poupanca_01.cria_conta()

    conta_poupanca_01.depositar("Kayque", 1000)
    conta_poupanca_01.depositar("Kayque", 1500)
    conta_poupanca_01.depositar("Kayque", 1000)
    # conta_poupanca_01.sacar(500)
