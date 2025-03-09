## Criando Exceptions em Python Orientado a Objetos
### Criando Exceções Personalizadas
- Criar **exceções personalizadas** ao herdar da classe `Exception`.  
- O nome da exceção geralmente termina com `Error` para manter o padrão da linguagem.  
- Podemos adicionar métodos personalizados para manipular os erros.  
### Com classes:
```python
class MyError(Exception):
    """Exceção personalizada para erros específicos."""
    def __init__(self, mensagem):
        super().__init__(mensagem)

# Levantando a exceção
def verificar(condicao):
    if condicao:
        raise MeuError("Condição inválida encontrada!")

try:
    verificar(True)
except MeuError as e:
    print(f"Erro tratado: {e}")
```



### Levantando (Raise) Exceções 
- Para **levantar** uma exceção personalizada, usamos `raise` seguido da classe da exceção:  
  ```python
  raise MeuError("Ocorreu um erro específico!")
  ```
- Isso interrompe o fluxo normal do código e exibe a mensagem de erro.
-**Ler Os Traceback e entender-los!!!**

### Relançando Exceções
- Se capturarmos uma exceção com `try-except`, podemos **relançá-la** para manter o rastreamento do erro:
  ```python
  try:
      raise MeuError("Algo deu errado!")
  except MeuError as e:
      print(f"Erro capturado: {e}")
      raise  # Relança a mesma exceção
  ```
- Isso é útil quando queremos adicionar logs ou fazer alguma ação antes de permitir que o erro continue.

### Adicionando Notas em Exceções (Python 3.11+) 
- Podemos adicionar **notas extras** a uma exceção com `.add_note()`, útil para depuração:
  ```python
  try:
      raise MeuError("Erro crítico")
  except MeuError as e:
      e.add_note("Verifique a configuração do sistema.")
      raise
  ```
- Isso ajuda a documentar a exceção sem precisar modificar a mensagem principal.
- Se definir com algum deve fazer tudo segundo a ele. 
- Se tiver string nos parâmetros de um método? use __str__
- obj!r Ou s.
+ OBS: **Para fazer operações com objetos na classe pai deve ter métodos relacionados a cada operação que será feita.**

