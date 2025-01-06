string = 'Kay'
dir = dir(string)

metodo = 'upuper'

if hasattr(string, metodo):
    print('Existe.')
    print(getattr(string, metodo)())
else:
    print('Não existe.')