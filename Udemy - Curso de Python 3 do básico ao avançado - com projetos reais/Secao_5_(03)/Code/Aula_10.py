class Modificadores_de_Acesso:
    def __init__(self):
        self.public = 'Público'
        self._protected = 'Protegido'
        self.__private = "Privado"

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
f = Modificadores_de_Acesso()
# print(f.public)
print(f.metodo_publico())
