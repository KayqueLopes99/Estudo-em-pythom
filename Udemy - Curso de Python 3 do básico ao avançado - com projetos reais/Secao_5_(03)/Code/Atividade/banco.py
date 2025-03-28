from conta import *
from pessoa import *

class Banco:
    def __init__(
                 self,
                 agencias: list[int] | None =  None,
                 clientes:  list[Pessoa] | None =  None, 
                 contas:  list[Conta] | None =  None,
                 ):
        
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
