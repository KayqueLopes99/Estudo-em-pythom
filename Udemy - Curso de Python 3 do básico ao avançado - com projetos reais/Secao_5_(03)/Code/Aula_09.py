class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None


    # getter: Obtendo o valor 
    @property
    def cor(self):
        print('PROPERTY no Getter.')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor



caneta = Caneta('Azul') 
caneta.cor = "Verde"
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)