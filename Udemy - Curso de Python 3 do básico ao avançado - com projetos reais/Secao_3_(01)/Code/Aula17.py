# if  / elif      / else
# se / se não se / se não
condicao = True # True exive | False não exibe.

if condicao:
    print('Este é o código do if.')
else:
    print('Este é o código do else.')

if 10 == 10: # If a solo. 
    print("Outro if.")


print('Fora dos blocos.')

 
condicao1 = True # Daqui vai até a condição.
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


