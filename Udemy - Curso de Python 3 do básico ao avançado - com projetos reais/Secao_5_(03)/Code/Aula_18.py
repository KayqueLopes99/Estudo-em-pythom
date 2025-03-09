from abc import ABC, abstractmethod
# Classe Pai - Abstrata passada por herança
# Não pode usar diretamente.
class Log(ABC):
    # Método obrigatório. 

    @abstractmethod
    def _log(self, msg): ...
    
    # Essas são passadas!
    # métodos concretos qua fazer coisas.
    def log_error(self, msg):
        return self._log(f"Error: {msg}")
    
    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogPrintMixin(Log):

    # Esse método é obrigatório! 
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

l = LogPrintMixin()
l.log_error("Erro.")