### Resumo sobre Classes Abstratas e Tipagem de Parâmetros
- Classes Abstratas:
- Não podem ser **instanciadas** diretamente.  
- Precisam ter pelo menos um **método abstrato** (`@abstractmethod`).  
- As subclasses devem **implementar** esses métodos antes de serem usadas.

- Uso de Tipagem em Funções:
- Podemos definir o **tipo esperado** de um parâmetro em uma função:  
  ```python
  def funcao(parametro: TipoClasse):
      # Agora podemos usar os métodos da classe diretamente
  ```
- Isso significa que `parametro` **deve ser** um objeto da classe `TipoClasse` ou de suas subclasses. 

``` py
def notificar(notificacao: Notificacao):
    notificacao.enviar()  # Garantimos que o objeto tem o método enviar()
```
