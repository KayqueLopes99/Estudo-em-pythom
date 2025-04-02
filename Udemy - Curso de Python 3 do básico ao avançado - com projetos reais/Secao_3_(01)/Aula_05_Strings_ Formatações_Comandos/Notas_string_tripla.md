## String Tripla (`'''` ou `"""`) 
1. **Definição**: Strings triplas são definidas com três aspas simples (`'''`) ou duplas (`"""`).  
2. **Uso principal**:
   - Criar **strings multilinhas** sem precisar usar `\n`.  
   - Documentação de funções, classes e módulos (**docstrings**).  
3. **Exemplo**:
   ```python
   texto = """Este é um exemplo 
   de string multilinha."""
   print(texto)
   ```
4. **Docstrings**:  
   ```python
   def saudacao():
       """Esta função exibe uma saudação."""
       print("Olá, mundo!")
   ```
5. **Preservação de espaços**: Strings triplas mantêm a formatação original do texto.