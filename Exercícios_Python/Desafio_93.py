Dicionario = {}
qtd = int(input("Informe Quantas Pessoas Você Deseja Cadastrar: "))
for i in range(0, qtd):
    nome = str(input(f"Informe o Nome do {i+1} Jogador: "))
    partidas = int(input("Informe Quantas Partidas o Jogador Participou: "))
    lista_de_gol = []  # Inicialize a lista de gols para cada jogador
    aproveitamento = 0 
    for c in range(0, partidas):
        gols = int(input(f"Quantos Gols na Partida {c+1}: "))
        lista_de_gol.append(gols)
        aproveitamento += gols
        
    dados_do_jogador = {
        'Nome': nome,
        'Partidas': partidas,
        'Gols': lista_de_gol,
        'Aproveitamento': aproveitamento
    }
    Dicionario[nome] = dados_do_jogador

print("="*45)
print("================= Usuários =================")
for nome, dados_do_jogador in Dicionario.items():
    print(dados_do_jogador)
    print("="*45)
    print(f"Nome: {dados_do_jogador['Nome']}")
    print(f"Partidas: {dados_do_jogador['Partidas']}")
    print(f"Gols: {dados_do_jogador['Gols']}")
    print(f"Aproveitamento: {dados_do_jogador['Aproveitamento']}")
    print("="*45)


    # Enumerar a parte dos gols na lista dentro do dicionário.
    for j, gol_de_partida in enumerate(dados_do_jogador['Gols']):
        print(f"O jogador {dados_do_jogador['Nome']} na {j+1} Partida: {gol_de_partida}")
    print(f"Total: {aproveitamento} Gols")
    print("="*45)
