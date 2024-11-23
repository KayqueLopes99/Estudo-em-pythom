def contador(i,f,p):
    """_Reaização da contagem_

    Args:
        i (_type_): _inico do contador_
        f (_type_): _fim do contador_
        p (_type_): _passo do contador_
    """
    c=i
    while c <= f:
        print(f"{c}", end='..')
        c+=p
    print("Fim!")


contador(1,100,2)
