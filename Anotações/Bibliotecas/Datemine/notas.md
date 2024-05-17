# Conceito:
- Uma das principais ferramentas para trabalhar com datas e horas. Ela oferece várias classes que permitem manipular datas, horas e intervalos de tempo de forma eficiente e intuitiva.

Aqui está uma explicação e alguns comandos básicos:

### Classes Principais:
- `date`: Representa uma data (ano, mês, dia).
- `time`: Representa um horário, independente da data.
- `datetime`: Combinação de `date` e `time`.
- `timedelta`: Representa a diferença entre duas datas ou tempos.
- `timezone`: Representa um fuso horário.

### Exemplos de Uso:

**Obtendo a Data Atual:**
```python
from datetime import date

hoje = date.today()
print(hoje)  # Saída: 2024-05-15 (formato AAAA-MM-DD)
```

**Formatando Datas:**
```python
from datetime import datetime

agora = datetime.now()
print(agora.strftime('%d/%m/%Y %H:%M:%S'))  # Saída: 15/05/2024 21:59:26
```

**Calculando Diferenças de Tempo:**
```python
from datetime import datetime, timedelta

agora = datetime.now()
daqui_a_uma_semana = agora + timedelta(weeks=1)
print(daqui_a_uma_semana)  # Saída: Data e hora daqui a uma semana
```
