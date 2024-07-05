Lista_de_informações = []
media1 = media2 = 0
qtd = int(input("Informe Quantas Pessoas Você Deseja Cadastrar: "))
for i in range(0, qtd):
    nome = str(input(f"Informe o Nome do {i+1} Pessoa: ")).capitalize()
    idade = int(input("Informe a Idade da Pessoa: "))
    genero = str(input("Informe o Gênero da Pessoa[M OU F]: ")).upper()
    media1 += idade
    
    Dados = {
        'Nome': nome,
        'Gênero': genero,
        'Idade': idade
    }
    Lista_de_informações.append(Dados)
media2 = media1/qtd

print(f"=== Lista_de_informações ===")
for pessoa in Lista_de_informações:
    print(f"Nome: {pessoa['Nome']} | Gênero: {pessoa['Gênero']} | Idade: {pessoa['Idade']} anos")

print("-="*30)
print("-="*30)
print('=========  Menu  ========')
print(f"Total de Pessoas Cadastradas: {qtd}")
print(f"A Média de Idade é de {media2:.2f} Anos.")
print("=== Lista de Mulheres ===")
for pessoa in Lista_de_informações:
    if pessoa['Gênero'] == 'F':
        print(f"Mulher: {pessoa['Nome']} Idade: {pessoa['Idade']} Anos")
print("=== Lista de Pessoas Acima da Média ===")
for pessoa in Lista_de_informações:
    if pessoa['Idade'] >= media2:
        print(f"Mulher: {pessoa['Nome']} Idade: {pessoa['Idade']} Anos")

print("-="*30)
