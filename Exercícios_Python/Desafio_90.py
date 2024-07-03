Aluno = list()
qtd = int(input('Informe a Quantidade de Alunos que você deseja Cadastrar: '))

for i in range(qtd):
    nome_aluno = input(f"Informe o Nome do Aluno {i + 1}: ").capitalize()
    
    nota1 = float(input("Informe a Primeira Nota: "))
    nota2 = float(input("Informe a Segunda Nota: "))
    nota3 = float(input("Informe a Terceira Nota: "))
    media = (nota1 + nota2 + nota3)/3
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    notas = [nota1, nota2, nota3]


    # Crie um novo dicionário para cada aluno
    aluno = {
        'Nome': nome_aluno,
        'Notas': [nota1, nota2, nota3],
        'Media': media,
        'Situacao': situacao
    }

    Aluno.append(aluno)
print()
print("==== Dados ====")
print("="*15)
for aluno in Aluno:
   print(f"Aluno: {aluno['Nome']}\nNotas: {aluno['Notas']}\nMédia: {aluno['Media']:.2f}\nSituação: {aluno['Situacao']}")
   print("="*15)
print("==== Fim ====")