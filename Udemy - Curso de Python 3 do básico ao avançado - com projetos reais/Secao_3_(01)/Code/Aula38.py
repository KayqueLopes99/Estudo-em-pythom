qtd_linhas = 5
qtd_colunas = 5

linha = 1 # Iniciamos com a linha 1.
print("-"*10) 
while linha <= qtd_linhas:
    # Cada linha deve estar em 5 colunas.
    coluna = 1
    # Quando executa começa com a linha 1 verificando a condição, depois a declaração de coluna vai para o loop interno while repeindo 5 vezes pois são 5 colunas para linha 1 e ...
    while coluna <= qtd_colunas:
        # print(f'{linha=} {coluna=}')
        print(f'{linha} {coluna}')
        coluna += 1
    linha += 1


print("-"*10) 