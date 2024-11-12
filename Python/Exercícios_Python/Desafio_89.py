# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista_alunos = list()

while True:
    print("1 - Cadastrar Alunos.")
    print("2 - Selecionar Notas de um aluno.")
    print("0 - Sair.")
    opcao = int(input("Escolha Uma opção: "))
    if opcao == 1:
       QTD = int(input("Informe a quantidade de Alunos: "))
       for i in range(QTD):
           nome = str(input("Nome do Aluno(a): "))
           nota1 = float(input("Informe a primeira Nota: "))
           nota2 = float(input("Informe a segunda Nota: "))
           media = (nota1 + nota2)/2

           aluno = [nome]
           notas = [nota1, nota2]
           medial = [media]
           # Organizar as sublistas em uma lista de alunos
           aluno_completo = [aluno, notas, medial]
           lista_alunos.append(aluno_completo)
    elif opcao == 0:
        print("Saindo...")
        break
    elif opcao == 2:
        print("="*35)
        print("No.        NOME        MÉDIA")
        print("="*35)
        for i, aluno in enumerate(lista_alunos):
            print(f"Aluno({i:<4}): {aluno[0][0]:<10}  Média: {aluno[2][0]:<8}")
# A varíavel Aluno vai percorrer a lista_alunos, lembrando que a variavel está em loop for, logo ela vai atualizando para o próxima sub lista até o fim.
# Assim, no primeiro iteração teremos o acesso a primeira sublista dentro da lista_alunos.
# o nome que está na posição [0] dentro de outra lista na posição [0] e a média que está na posição [2] dentro de um outra lista na posição [0].
# E assim por Diante ATÉ O FIM.
            print("="*35)
        indice = int(input("Informe o Número Correspondente ao Aluno: "))
        print(f"As Notas do Aluno {lista_alunos[indice][0][0]}: {lista_alunos[indice][1][0]} e {lista_alunos[indice][1][1]}")
    else:
        print("Opção Invalida.")



