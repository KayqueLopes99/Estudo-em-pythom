try:
    a = 18
    b = int(input("Informe um valor númerico: "))
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as erro_name:
    print("Erro de Divisão por zero.")
    print(erro_name.__class__.__name__)
    print(erro_name)
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as erro_name:
    print('TypeError + IndexError')
    print('MSG:', erro_name)
    print('Nome:', erro_name.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print("Continue.")
