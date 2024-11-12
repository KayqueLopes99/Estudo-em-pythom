Dicionario = {}
qtd = int(input("Informe Quantas Pessoas Você Deseja Cadastrar: "))
for i in range(0, qtd):
    
    nome = str(input(f"Informe o Nome do {i+1} Jogador: "))
    partidas = int(input("Informe Quantas Partidas o Jogador Participou: "))
    lista_de_gol = []  # Inicialize a lista de gols para cada jogador
    aproveitamento = 0 


    for c in range(partidas):
        gols = int(input(f"Quantos Gols na Partida {c+1}: "))
        lista_de_gol.append(gols)
        aproveitamento += gols
        


    dados_do_jogador = {
        'Nome': nome,
        'Partidas': partidas,
        'Gols': lista_de_gol,
        'Aproveitamento': aproveitamento
    }
    Dicionario[i] = dados_do_jogador  # Usando o índice i do loop numérico como chave

print("-="*50)
print("=================== Jogadores ====================")
print("Cod.Nome             Gols                    Total")
contar = 0
for nome, dados_do_jogador in Dicionario.items():
    
    print(f"{contar} {dados_do_jogador['Nome']}                 {dados_do_jogador['Gols']}                    {dados_do_jogador['Aproveitamento']}")
    contar += 1
    
while True:
    Dicionario_numerado = enumerate(Dicionario)
    pergunta = int(input("(-1 -> Sair)Mostrar Dados de qual Jogador: "))
    
    if pergunta in Dicionario:
        jogador_selecionado = Dicionario[pergunta]
        print(f"--- Levantamento do Jogador {jogador_selecionado['Nome']}:")
        for j, gol_de_partida in enumerate(jogador_selecionado['Gols']):
            print(f"No Jogo {j+1}: {gol_de_partida} Gols.")
        print(f"Total: {jogador_selecionado['Aproveitamento']} Gols")
        print("=" * 45)


    elif pergunta == -1:
        print("Saindo ...")
        break


    else: 
        print("\033[91mInforme algo Válido.\033[m")
