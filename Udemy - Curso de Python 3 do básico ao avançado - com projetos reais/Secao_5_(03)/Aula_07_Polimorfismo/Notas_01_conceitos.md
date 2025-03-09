## Teoria: polimorfismo, assinatura de métodos e Liskov Substitution Principle
- O **Polimorfismo** permite que diferentes classes, derivadas de uma mesma superclasse, implementem **métodos com o mesmo nome e mesma assinatura**, mas com comportamentos distintos.

### Características
- O método deve ter o **mesmo nome** em todas as classes que o implementam.
- O método deve ter a **mesma assinatura**, ou seja, o mesmo número e tipo de parâmetros.
- As subclasses podem fornecer uma **implementação diferente** do método definido na superclasse.

```python
# 0.1 Criamos uma **superclasse** que define um método genérico.
class Superclasse:
    def metodo(self, parametro1, parametro2):
        pass  # A implementação será feita nas subclasses

# 0.2 Criamos **subclasses** que sobrescrevem esse método, mantendo a mesma assinatura.
class Subclasse1(Superclasse):
    def metodo(self, parametro1, parametro2):
        pass  # Implementação específica da Subclasse1

# 0.3 Podemos chamar o método de forma genérica, sem precisar verificar o tipo da classe.
class Subclasse2(Superclasse):
    def metodo(self, parametro1, parametro2):
        pass  # Implementação específica da Subclasse2
```

---
## Assinatura de Métodos
- Define sua estrutura e a forma como ele deve ser chamado.INCLUI:
1. **O nome do método**
2. **Os parâmetros (quantidade e tipo)**
3. **A ordem dos parâmetros**
4. **Os valores padrão dos parâmetros (se houver)**
+ (O **tipo de retorno** **não** faz parte da assinatura do método em Python).
+ Assinatura do método: nome, parâmetros e mas CONSIDERA-SE (retorno iguais)
---

##  Liskov Substitution Principle (LSP)
- Afirma que **uma subclasse deve ser capaz de substituir a superclasse sem quebrar a aplicação**.
- **As subclasses devem manter o comportamento esperado da superclasse.**
- **A assinatura dos métodos não pode ser alterada.**

```python
class Superclasse:
    def metodo(self, parametro):
        pass

class SubclasseCorreta(Superclasse):  # ✅ Segue o LSP
    def metodo(self, parametro):
        pass  # Implementação compatível com a superclasse

class SubclasseIncorreta(Superclasse):  # 🚨 Quebra o LSP
    def metodo(self, parametro, extra):  # Mudança na assinatura (ERRO)
        pass
```

- Aula_20.py
```py
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
```