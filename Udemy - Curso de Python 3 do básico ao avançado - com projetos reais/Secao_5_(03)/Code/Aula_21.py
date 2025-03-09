class MeuError(Exception):
     ...
 
 
class OutroError(Exception):
     ...
 
 
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    # Notes
    exception_.add_note('Anotação de erro 1')
    raise exception_
 
 
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()

    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Anotação de erro 2')

    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error