# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print("Exemplo: Abrir um arquivo.")
    8/0
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
    print("Divisão por zero encontrada.")
except IndexError as error:
    print(error.__class__.__name__)
    print(error)
    print("IndexError.")
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')