# if  / elif      / else
# se / se não se / se não
# o depurador Debuger vai procurar a condição True.
# Selecionamos a linha. 

condicao1 = True # Daqui vai até a condição e o depurador finaliza.
condicao2 = False
condicao3 = True # Só uma condição é atendida
condicao4 = False

if condicao1:
    # Se ele for True.
    print("Código da condição 01.")
elif condicao2:
    print("Código da condição 02.")
elif condicao3:
    print("Código da condição 03.")
elif condicao4:
    print("Código da condição 04.")
else:
    print('Nenhuma condição escolhida.')

