class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
    }
    
    def __init__(self, nome=None):
        self.__dict__ = self._state
        
        if nome is not None:
            self.nome = nome
    

# Estado compartiilhado: se mudr algo em uma, muda na outra também.   

if __name__ == "__main__":
    m1 = MonoStateSimple("kayque")
    m2 = MonoStateSimple()
    
    print(m1)
    print(m2)