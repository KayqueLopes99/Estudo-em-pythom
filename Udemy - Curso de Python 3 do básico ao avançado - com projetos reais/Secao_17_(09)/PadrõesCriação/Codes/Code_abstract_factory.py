from abc import ABC, abstractmethod

# Product
class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class VeiculoPapular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass



# Concrete product
class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')


class CarroPopularZN(VeiculoPapular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está buscando o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN está buscando o cliente...')


class MotoPopularZN(VeiculoPapular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN está buscando o cliente...')

# Concrete product
class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está buscando o cliente...')


class CarroPopularZS(VeiculoPapular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está buscando o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está buscando o cliente...')


class MotoPopularZS(VeiculoPapular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS está buscando o cliente...')

# INTERFACE
class VeiculoFactory(ABC):
    
    # Factories methods
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPapular: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPapular: pass
    



# Implementadno a interface fornecendo o objeto.
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: return CarroLuxoZN()
    
    @staticmethod  
    def get_carro_popular() -> VeiculoPapular: return CarroPopularZN()
    
    @staticmethod 
    def get_moto_luxo() -> VeiculoLuxo: return MotoLuxoZN()
    
    @staticmethod 
    def get_moto_popular() -> VeiculoPapular: return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: return CarroLuxoZS()
    
    @staticmethod  
    def get_carro_popular() -> VeiculoPapular: return CarroPopularZS()
    
    @staticmethod 
    def get_moto_luxo() -> VeiculoLuxo: return MotoLuxoZS()
    
    @staticmethod 
    def get_moto_popular() -> VeiculoPapular: return MotoPopularZS()



# Aplicando a composição.
class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()
            
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()
            
            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()
            
            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()
            
            

            
if __name__ == "__main__":
    
    cliente = Cliente()
    cliente.busca_clientes()