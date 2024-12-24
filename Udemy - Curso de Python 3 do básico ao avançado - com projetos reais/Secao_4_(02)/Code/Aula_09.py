
# função externa
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

# A função criar_saudacao retorna a função saudar (que é definida dentro dela), mas com o valor de saudacao já "lembado". Isso cria uma closure.
falar_bom_dia = criar_saudacao('Good morning')

# Quando chamamos criar_saudacao('Good morning'), a função retorna a função saudar com o valor 'Good morning' já "preso" nela.
falar_boa_noite = criar_saudacao('Good night')

print(falar_bom_dia) # Local da mermória

for nome in ['kayque', 'Isabelly', 'Samuel']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))