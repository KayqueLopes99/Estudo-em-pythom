def fatorial(Numero, show):
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
           print(f"{i} ", end="* ")
        fator *= i
    if show:
        print(f" = {fator}")
    return fator
        

print("=+=" * 10)
print("\033[91m- Menu de Votação - \033[m")
Numero = int(input("Informe um número: "))
Validade = str(input("Mostrar o cálculo do processo? (S/N): ")).capitalize()

if Validade == "S":
    show = True
else:
    show = False


resultado = fatorial(Numero, show=show)
print("Resultado do fatorial:", resultado)
print("=+=" * 10)

help(fatorial)
    