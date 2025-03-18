def my_repr(self):
    return f"{type(self).__name__}({self.__dict__})"


class MetaClass(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia
    

class People(metaclass= MetaClass):

    def __new__(cls, *args, **kwargs):
        print("MEU NEW")
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print("MEU INIT")

    def falar(self):
        print("Good morning!")
    
p1 = People('Luiz')
p1.falar()