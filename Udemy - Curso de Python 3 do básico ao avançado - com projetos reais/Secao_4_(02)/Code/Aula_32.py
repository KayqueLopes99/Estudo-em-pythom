try:
    a = 18
    b = int(input("Informe um valor númerico: "))
    print('Linha 1'[1000])
    c = a / b
except ZeroDivisionError:
    print("Erro de Divisão por zero.")
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print("Continue.")
