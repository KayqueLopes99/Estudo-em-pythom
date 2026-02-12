from abc import ABC, abstractmethod


# Product
class veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# Concrete Product_01
class CarroLuxo(veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente ...")
        
# Concrete Product_02
class CarroPopular(veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente ...")
    
# Concrete Product_03
class Moto(veiculo):
    def buscar_cliente(self) -> None:
        print("Moto está buscando o cliente ...")    
      
      
# Factory  
class VaieculoFactory: 
    # Factory method
    @staticmethod
    def get_carro(tipo: str) -> veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        
        if tipo == 'popular':
            return CarroPopular()
        
        if tipo == 'moto':
            return Moto()
        
        assert 0, 'Veículo não existe!'
        
        

# Client
if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto']
    
    for index in range(10):
        carro = VaieculoFactory.get_carro(choice(carros_disponiveis))

        carro.buscar_cliente()
    