# Empacotamento. 

def contador(* núm):
    for valor in núm:
        print(f"{valor} ", end='')
    print("Fim!!!")


def Tamanho(* núm):
    Total = len(núm)
    print(f"Recebi os Valores {núm} e são ao todo {Total} Números.")



contador(1,2,3,5,6,7,8)
Tamanho(1,2,3,5,6,7,8)

