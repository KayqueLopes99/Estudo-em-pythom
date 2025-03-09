# Abstração.
# Se eu estou criando uma classe, eu estou ciando meu proprio tipo.
# Herança: é um ...

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

# Classe Pai - Abstrata passada por herança
class Log:
    # Método obrigatório. 
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")
    
    # Essas são passadas!
    # métodos concretos qua fazer coisas.
    def log_error(self, msg):
        return self._log(f"Error: {msg}")
    
    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        print(f"Salvando no log: {msg}")
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n")
       

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("Mensagem de Erro!")
    lp.log_success("Mensagem de Sucesso!")

    lf = LogFileMixin()
    lf.log_error("Mensagem de Erro!")
    lf.log_success("Mensagem de Sucesso!")
