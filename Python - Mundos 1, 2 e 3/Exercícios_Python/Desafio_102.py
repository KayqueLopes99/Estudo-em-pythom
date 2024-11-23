# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Então, quando o parâmetro show não é especificado, a função assume False e não imprime o cálculo passo a passo.
def fatorial(Numero, show=False):
    """ Função para calcular o fatorial de um número.

    Args:
        Numero (_int_): _O número a ser calculado._
        show (_str_): _(opcional) Mostrar ou não a conta._

    Returns:
        _int_: _O valor do Fatorial de um número Numero._
    """
    fator = 1
    for i in range(Numero, 0, -1):     
        if show: 
           print(i, end='')  
           if i > 1:     
            print(" X ", end='')
           else:
              print(" = ", end='')
              
        fator *= i
    return fator
        

print("=+=" * 10)
print("\033[91m- Menu - \033[m")
Numero = int(input("Informe um número: "))
Validade = str(input("Mostrar o cálculo do processo? (S/N): ")).capitalize()

if Validade == "S":
    show = True
else:
    show = False


resultado = fatorial(Numero, show=show)
print("Resultado do fatorial:", resultado)
print("=+=" * 10)

# help(fatorial)
    