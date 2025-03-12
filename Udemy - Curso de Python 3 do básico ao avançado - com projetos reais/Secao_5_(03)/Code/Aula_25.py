# Funções decoradoras e decoradores com métodos
# Função decoradora
def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

# cls = classe.
def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def my_planet(method):
    def intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
 
        if 'Terra' in result:
             return 'Are you at home'
        return result
    return intern


@add_repr
class Time:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def speak_name(self):
        return f'The planet is {self.name}'
    
brazil = Time('Brasil')
portugal = Time('Portugal')
 
Earth = Planet('Terra')
Mars = Planet('Marte')
 
print(brazil)
print(portugal)
 
print(Earth)
print(Mars)
 
print(Earth.speak_name())
print(Mars.speak_name())