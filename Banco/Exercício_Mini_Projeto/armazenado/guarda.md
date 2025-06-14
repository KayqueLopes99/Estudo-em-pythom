"""
    
   
  def adiciona_dados_da_conta(self, nome):
    arquivo_contas = Arquivo_Contas()
    arquivo_usuarios = Arquivo()

    # Verifica se o nome existe no arquivo de usuários
    self.titular = arquivo_usuarios.obter_nome(nome)
    if not self.titular:
        print(f"\033[91mErro: Nenhuma pessoa encontrada com o nome '{nome}'.\033[m")
        return None

    # Garante que a leitura dos dados da conta seja uma lista
    dados_contas = arquivo_contas.ler_ou_imprimir_conta() or []

    # Verifica se já existe uma conta para essa pessoa
    for conta in dados_contas:
        if conta["nome"] == self.titular:
            print(f"\033[91mErro: A conta para {self.titular} já existe com o número {conta['numero da conta']}.\033[m")
            return None

    # Cria os dados da nova conta
    dados_nova_conta = {
        "nome": self.titular,
        "numero da conta": self.numero_conta,
        "agencia": self.agencia,
        "saldo": self.saldo,
        "limite": self.limite,
    }

    # Adiciona a nova conta ao arquivo JSON
    arquivo_contas.escrever_conta([dados_nova_conta])

    print(f"\033[92mConta criada com sucesso para {self.titular}. Número da conta: {self.numero_conta}\033[m")
    return dados_nova_conta


    
  def obter_saldo(self, nome):
    arquivo = Arquivo_Contas()
    dados = arquivo.ler_ou_imprimir_conta()

    if not dados:  # Se 'dados' for None ou lista vazia, evita erro
        print("\033[91mNenhuma conta encontrada.\033[m")
        return None
    
    for pessoa in dados:
        if pessoa['nome'] == nome:
            return pessoa['saldo']
    
    print(f"\033[91mNenhuma pessoa encontrada com o nome {nome}.\033[m")
    return None

    
    
  def mostrar_saldo(self, nome):
    arquivo = Arquivo_Contas()
    dados = arquivo.ler_ou_imprimir_conta()

    # Encontra a conta mais recente (última conta inserida no arquivo)
    conta_encontrada = None
    for pessoa in reversed(dados):  # Percorre a lista de trás para frente
        if pessoa['nome'] == nome:
            conta_encontrada = pessoa
            break

    if conta_encontrada is None:
        print(f"Nenhuma pessoa encontrada com o nome {nome}.")
        return None

    # Exibe as informações da última conta encontrada
    print(f"Usuário: {conta_encontrada['nome']}\nSaldo: {conta_encontrada['saldo']}\nLimite disponível: {conta_encontrada['limite']}")
    return conta_encontrada


  def depositar(self, nome, valor):
    arquivo = Arquivo_Contas()

    # Obtém todos os dados da conta
    dados = arquivo.ler_ou_imprimir_conta()

    # Encontra a conta mais recente (última conta inserida no arquivo)
    conta_encontrada = None
    for pessoa in reversed(dados):  # Percorre a lista de trás para frente (última conta inserida)
        if pessoa['nome'] == nome:
            conta_encontrada = pessoa
            break

    if conta_encontrada is None:
        print(f"\033[91mErro: Não foi possível encontrar a conta para o usuário {nome}.\033[m")
        return None
    
    saldo_atual = conta_encontrada['saldo']

    if valor <= 0:
        print("\033[91mErro: O valor deve ser maior que zero.\033[m")
        return None

    # Verifica se o saldo total após o depósito não ultrapassa o limite
    if hasattr(self, "limite") and saldo_atual + valor > self.limite:
        print(f"\033[91mErro: O depósito ultrapassaria o limite da conta ({self.limite}).\033[m")
        return None

    # Calcula o novo saldo após o depósito
    novo_saldo = saldo_atual + valor

    # Atualiza o saldo da conta mais recente
    conta_encontrada['saldo'] = novo_saldo

    # Chama o método para salvar os dados no arquivo
    arquivo.escrever_conta(dados)

    print(f"\033[92mDepósito de {valor:.2f} realizado com sucesso! Novo saldo: {novo_saldo:.2f}\033[m")
    return novo_saldo

    
  def realizar_saque(self, nome, valor):
    if valor <= 0:
        print(f"Erro: O valor {valor} é inválido. Informe um valor maior que zero.")
        return None

    arquivo = Arquivo_Contas()
    
    # Obtém todos os dados da conta
    dados = arquivo.ler_ou_imprimir_conta()

    # Encontra a conta mais recente (última conta inserida no arquivo)
    conta_encontrada = None
    for pessoa in reversed(dados):  # Percorre a lista de trás para frente (última conta inserida)
        if pessoa['nome'] == nome:
            conta_encontrada = pessoa
            break

    if conta_encontrada is None:
        print(f"Erro: Não foi possível encontrar a conta para o usuário {nome}.")
        return None

    saldo_atual = conta_encontrada['saldo']

    print(f"O saldo atual da conta de {nome} é: {saldo_atual:.2f}")

    # Verifica se o valor de saque não ultrapassa o limite da conta
    if valor > saldo_atual + conta_encontrada['limite']:
        print(f"Erro: Saldo insuficiente para realizar o saque de {valor}.")
        return None

    # Realiza o saque, atualizando o saldo
    novo_saldo = saldo_atual - valor
    conta_encontrada['saldo'] = novo_saldo  # Atualiza o saldo da conta

    # Salva os dados atualizados no arquivo
    arquivo.escrever_conta(dados)

    print(f"Saque de {valor} realizado com sucesso. Novo saldo: {novo_saldo:.2f}")
    return conta_encontrada




"""