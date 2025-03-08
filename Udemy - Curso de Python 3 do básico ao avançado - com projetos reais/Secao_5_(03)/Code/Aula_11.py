# associação
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None # Privado!

    @property # captar o valor do atributo
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter # manipular
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Kayque')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever


# Associação
print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())