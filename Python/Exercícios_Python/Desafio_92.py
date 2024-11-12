from datetime import datetime

# Obtenha a data e hora atual
hoje = datetime.now()
ano_atual = hoje.year

Dicionario = {}  # Inicialize um dicionário externo vazio

qtd = int(input("Informe Quantas Pessoas Você Deseja Cadastrar: "))
for i in range(qtd):
    nome = input(f"Informe o Nome do {i+1} Trabalhador: ").capitalize()
    ano_nascimento = int(input("Informe o Ano de seu Nascimento: "))
    
    idade = ano_atual - ano_nascimento
    carteira = int(input("Carteira de Trabalho (0 - Não Tenho): "))
    
    if carteira != 0:
        contrato = int(input("Informe o Ano de Contratação: "))
        salario = float(input("Informe o Salário: R$ "))
        aposento = idade + 35
    else:
        print(f"Trabalhador {nome} sem Carteira de Trabalho.")
        carteira = 0
        contrato = 0
        salario = 0
        aposento = 'Aposentado'
    
    
    if aposento >= 65:
        print(f"Situação da Aposentadoria do Senhor(a) {nome}: Aposentado!")
        aposento = 0
        aposento = 'Aposentado'
        
        
    else:
        anos_faltantes = 65 - aposento
        print(f"Situação da Aposentadoria do Senhor(a) {nome}: Falta {aposento} Anos ainda.")
    
    # Crie um dicionário interno para cada conjunto de dados
    dados_trabalhador = {
        'Nome': nome,
        'Idade': idade,
        'Carteira': carteira,
        'Contrato': contrato,
        'Salário': salario,
        'Aposento': aposento
    }
    
    # Adicione o dicionário interno ao dicionário externo
    Dicionario[nome] = dados_trabalhador
# nome é a chave e dados_trabalhador é o valor no dicionario aninhado.

print("="*45)
print("================= Usuários =================")
for nome, dados_trabalhador in Dicionario.items():
    print(f"Nome: {dados_trabalhador['Nome']}")
    print(f"Idade: {dados_trabalhador['Idade']}")
    print(f"Carteira: {dados_trabalhador['Carteira']}")
    print(f"Contrato: {dados_trabalhador['Contrato']}")
    print(f"Salário: {dados_trabalhador['Salário']}")
    print(f"Situação do Aposento: {dados_trabalhador['Aposento']}")
    print("="*45)
