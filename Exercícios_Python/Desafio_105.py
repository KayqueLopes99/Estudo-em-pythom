# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

def notas(*Numeros, sit=False):
    """_Está função irá colocar os dados dos discente no dicionario conforme solicitado_

    Args:
        sit (bool, optional): _description_. Defaults to False.
        *Numeros: _Conjunto de Notas_

    Returns:
        _type_: _dicionário_
    """
    maior = max(Numeros)
    menor = min(Numeros)
    media = sum(Numeros) / len(Numeros)
    total = len(Numeros)

    dados = {'Total': total,
             'maior_nota': maior,
             'menor_nota': menor,
             'média': media}

    if sit:
        if media >= 7:
            situacao = 'Boa'
        elif media >= 5:
            situacao = 'Razoavel'
        else:
            situacao = 'Ruim'
        dados['situação'] = situacao

    return dados

Situation = str(input("Mostrar a situação do Discente também? (S/N): ")).upper()

if Situation == "S":
    show = True
else:
    show = False

resp = notas(9.5,9.0,8.5,8.0, sit=show)

print("=+=" * 10)
print(f"\033[92m{resp}\033[m")
print("=+=" * 10)