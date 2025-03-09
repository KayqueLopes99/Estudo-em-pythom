from abc import abstractmethod, ABC
# -> Classes abstratas nõo podem ser instânciadas até que o método seja concreto.

# Ela herda de ABC (Abstract Base Class), garantindo que a classe não possa ser instanciada diretamente.
class Notificacao(ABC):

    def __init__(self, mensagem):
        self.mensagem = mensagem


    # Ela herda de ABC (Abstract Base Class), garantindo que a classe não possa ser instanciada diretamente.
    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("E-mail: enviando - ", self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print("SMS: enviando - ", self.mensagem)
        return True



## Objeto polimorfo. 
# A função notificar() recebe um objeto da classe base (Notificacao), mas pode trabalhar com qualquer subclasse dela.
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print("Notificação enviada.")
    else:
        print("Notificação não enviada.")

    
# em ação! As duas classes (NotificacaoEmail e NotificacaoSMS) têm o mesmo método (enviar()), mas implementações diferentes.
notificacao_email = NotificacaoEmail("Teste")
notificar(notificacao_email)


notificacao_sms = NotificacaoSMS("Teste")
notificar(notificacao_sms)
 
