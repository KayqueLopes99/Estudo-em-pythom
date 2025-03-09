##  (Parte 1) Mixins, Abstração e a união de tudo até aqui
### Necessidade de adicionar funcionalidades extras sem criar uma hierarquia complexa.

- Pensa nos Mixins como "complementos" que você pode adicionar às suas classes. Eles não funcionam sozinhos, mas servem para dar habilidades extras para outras classes.

- Um **Mixin** é uma classe que fornece funcionalidades adicionais para outras classes, **sem ser uma classe base completa**.  

- **Não funciona sozinho**, precisa ser herdado por outra classe.
- **Fornece funcionalidades específicas**, sem representar um objeto real.


```python
# Mixin de log (só adiciona uma funcionalidade extra)
class LogMixin:
    def log(self, mensagem):
        print(f"LOG: {mensagem}")

# Classe normal de um computador
class Computador:
    def __init__(self, modelo):
        self.modelo = modelo

    def ligar(self):
        print(f"{self.modelo} ligado.")

# Computador que também pode fazer log
class ComputadorComLog(Computador, LogMixin):
    def ligar(self):
        self.log(f"Ligando {self.modelo}...")  # Usa o log do mixin
        super().ligar()  # Mantém o comportamento original de ligar

# Criando um computador que tem log
pc = ComputadorComLog("Dell XPS 15")
pc.ligar()

```
 
- A classe `LogMixin` fornece um método `log()`.  
- A classe `ComputadorComLog` herda tanto de `Computador` quanto de `LogMixin`.  
---

## Abstração 
- A abstração significa esconder detalhes e mostrar apenas o necessário. No Python, usamos classes abstratas para forçar outras classes a implementarem certos métodos.  
- Cria uma base obrigatória para outras classes seguirem.

- *Exemplo*: Criamos uma classe Veiculo com um método ligar(), e qualquer classe que herde Veiculo precisa implementar esse método.

+ **Mixins são como acessórios (opcionais)**.
+ **Abstração é como uma regra (obrigatória)**.
+ Prefira composição(ASSICIAÇÃO, AGRAGAÇAO E COMPOSIÇÃO - OS TRÊS JUNTOS.) ao inves de herança. 
+ `Aula_17`
````py
from pathlib import Path  
LOG_FILE = Path(__file__).parent / 'log.txt'  

# Classe Abstrata - Define a estrutura, mas não pode ser usada diretamente
class Log:
    """
    Classe base abstrata que define uma estrutura para logging.
    Qualquer classe que herdar de Log deve implementar o método _log().
    """
    
    def _log(self, msg):
        """
        Método abstrato que deve ser implementado pelas subclasses.
        Se uma subclasse não implementar este método, um erro será gerado.
        """
        raise NotImplementedError("Implemente o método log")
    
    # Métodos concretos que chamam _log() - São herdados e podem ser usados diretamente.
    def log_error(self, msg):
        return self._log(f"Error: {msg}")  
    def log_success(self, msg):
        return self._log(f"Success: {msg}") 


# Mixin para salvar logs em arquivos
class LogFileMixin(Log):
    """
    Classe Mixin que implementa o método _log() para salvar logs em arquivos.
    Essa classe herda de Log e é um mixin porque adiciona funcionalidade específica.
    """
    
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"  
        print(f"Salvando no log: {msg}")  

        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n")


# Mixin para exibir logs no terminal
class LogPrintMixin(Log):
    """
    Classe Mixin que implementa o método _log() para exibir mensagens no console.
    Essa classe herda de Log e é um mixin porque adiciona funcionalidade específica.
    """
    
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})") 


# Testando os Mixins
if __name__ == "__main__":

    lp = LogPrintMixin()
    lp.log_error("Mensagem de Erro!") 
    lp.log_success("Mensagem de Sucesso!") 

  
    lf = LogFileMixin()
    lf.log_error("Mensagem de Erro!")  
    lf.log_success("Mensagem de Sucesso!")  

````