"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')
# Captura o erro e vai...
try: #File fast (Errar o mais rápido).
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAR:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print("Isso não é um número.")
    



# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')