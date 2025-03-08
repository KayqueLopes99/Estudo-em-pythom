class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    
    def inserir_endereco(self, rua, numero):
        # Estou ciriando a instancia de endereços dentro desta classe, quando ele sumir ela se vai também.
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        
        self.enderecos.append(endereco)


    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

     ## Apagando
    def __del__(self):
        print("Apagando:", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
     ## Apagando
    def __del__(self):
        print("Apagando:", self.rua, self.numero)
    
cliente_01 = Cliente('Maria')
cliente_01.inserir_endereco("Rua das estrelas", 18)
cliente_01.inserir_endereco("Av Brasil", 200)
cliente_01.listar_enderecos()

endereco_externo = Endereco('Sítio catolé', 11111)
cliente_01.inserir_endereco_externo(endereco_externo)
cliente_01.listar_enderecos()

del cliente_01
print(endereco_externo.rua, endereco_externo.numero)
print("fim")