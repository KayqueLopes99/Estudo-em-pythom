# 
# Dobrar os Valores da Lista.
def dobra_valores(lista):
    pos = 0
    while pos < len(lista):
        # [pos] -> Posições. 
        lista[pos] *= 2
        pos += 1



Valores = [1,2,3,4,5,6,7,8,9,10]
dobra_valores(Valores)
print(Valores)