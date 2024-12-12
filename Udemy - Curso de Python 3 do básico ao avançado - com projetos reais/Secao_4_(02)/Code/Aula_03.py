def soma(x, y, z = None): # z recebe um valor Valor padrão.
    if z is not None:
        print(f'{x=} {y=} {z=}:', x + y + z) 
    else:
        print(f'{x=} {y=}', x + y)



soma(1,2)
soma(3,2)
soma(100,200)
soma(y = 9,z = 2, x = 7)
