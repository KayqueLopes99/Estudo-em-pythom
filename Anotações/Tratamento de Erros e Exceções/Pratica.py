"""try: # Tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('\033[91m== Infelizmente tivemos um problema! ==\033[m')
    print(f'\033[91m== Erro {erro.__class__}==\033[m')
    # Ou
    # print(f'\033[91m== Erro {erro}==\033[m')

# Opcionais.
else: # Evita aparecer mensagem. 
    print(f"O resultado: {r:.1f}")

finally:
    print("\033[92mVolte - Sempre !!!\033[m")"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[91m== Infelizmente tivemos um problema com os tipos de dados! ==\033[m')
except ZeroDivisionError:
    print('\033[91m== Não é possível dividir um número por zero ==\033[m')
except KeyboardInterrupt:
    print('\033[91m== Dados não informados ==\033[m')
except Exception as erro:
    print('\033[91m== Infelizmente tivemos um problema! ==\033[m')
    print(f'\033[91m== Tipo de erro: {erro.__class__.__name__} ==\033[m')  # Exibe o tipo do erro
    print(f'\033[91m== Mensagem de erro: {erro} ==\033[m')                 # Exibe a descrição do erro

# Opcional
else:
    print(f"O resultado: {r:.1f}")
finally:
    print("\033[92mVolte sempre!\033[m")
