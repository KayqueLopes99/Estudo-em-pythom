## datetime
- Uma das principais ferramentas para trabalhar com datas e horas. Ela oferece várias classes que permitem manipular datas, horas e intervalos de tempo.

### Classes Principais:
- `date`: Representa uma data (ano, mês, dia).
- `time`: Representa um horário, independente da data.
- `datetime`: Combinação de `date` e `time`.

```py
from datetime import datetime, date

data = datetime(2025, 6, 14, 20, 43, 25)
data_date = date(2025, 6, 14)
print(data_date)
print(data)

```

### datetime:
- Sintaxe:
```python
from datetime import datetime
```
- Escolha:
> datetime(ano, mês, dia)
> datetime(ano, mês, dia, hora, minuto, segundo, microsegundo)
> datetime.now()  # Obtém a data e hora atual
> datetime.today()  # Obtém a data atual (sem hora)
> datetime.strftime(variavel, formato)  # Formata a data/hora como string


## Comparar e Diferenciar datas:
- *timedelta*:
- Representa uma diferença entre duas datas ou horas.
``` py
from datetime import datetime, timedelta
from pytz import timezone
agora = datetime.now()  # Obtém a data e hora atual
print(agora)  # formato AAAA-MM-DD HH:MM:SS.mmmmmm)

data_str = '2024-05-15 21:59:26'

# Converte a string para um objeto datetime
data_obj = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
print(data_obj)  

# Obter data e hora atual em UTC dE ALGUM LUGAR
dataTokyo = datetime.now(timezone("Asia/Tokyo"))
print(dataTokyo)


fmt = '%Y-%m-%d %H:%M:%S'
dataInicio = datetime.strptime('2024-05-15 21:59:26', fmt)
dataFim = datetime.strptime('2025-05-15 21:59:26', fmt)

print(dataFim > dataInicio)
print(dataFim < dataInicio)
print(dataFim == dataInicio)

delta = dataFim - dataInicio
print(delta.days, delta.total_seconds())


delta1 = timedelta(days=10, hours=10) # com diferenã de 10 dias.
print(dataFim + delta1)
print(dataFim - delta1)
```

## Formatando datas:
- `strftime`: Formata a data/hora como string.
- Podemos mudar a posição dos elementos e o formato da data/hora.
- Pode-se remover.

```py
from datetime import datetime
data = datetime(2025, 6, 14, 20, 43, 25)
fmt = '%d/%m/%Y %H:%M:%S'
formato = data.strftime(fmt)
print(formato)  # Saída: 14/06/2025 20:43:25

print(dataInicio.strftime('%Y'), dataInicio.year)
print(dataInicio.strftime('%m'), dataInicio.month)
print(dataInicio.strftime('%d'), dataInicio.day)
```

#### Constantes:
- 
## Métodos:
- strftime: Formata a data/hora como string.
- strptime: Converte uma string em um objeto datetime. Este serve para criar datas a partir de strings.

- relativedelta: Permite manipular datas de forma mais flexível, como adicionar meses ou anos.
```py

```

## Manipulando datas com timedelta
- Necessidade: Adicionar ou subtrair dias, horas, minutos, segundos, etc., de uma data específica.
```py
from datetime import datetime, timedelta
data_atual = datetime.now()
print("Data Atual:", data_atual)
# Adicionando 10 dias
nova_data = data_atual + timedelta(days=10)
print("Data após adicionar 10 dias:", nova_data)
# Subtraindo 5 horas
nova_data_menos_horas = data_atual - timedelta(hours=5)
print("Data após subtrair 5 horas:", nova_data_menos_horas)
```
- `days`: Número de dias.
- `seconds`: Número de segundos.
- `microseconds`: Número de microssegundos.
- `milliseconds`: Número de milissegundos.
- `minutes`: Número de minutos.
- `hours`: Número de horas.
- `weeks`: Número de semanas.


> Somando e subtraindo datas com timedelta.
- utcnow(): Obtém a data e hora atual em UTC (Tempo Universal Coordenado).
- é um melhor padrão para projetos. 


## timezone
> Permite trabalhar com fusos horários.
- pip install pytz
```py
from datetime import datetime, timezone
from pytz import timezone
dataTokyo = datetime.now(timezone("Asia/Tokyo"))
dataBrasilia = datetime.now(timezone("America/Sao_Paulo"))
print(dataBrasilia)
print(dataTokyo)

datetime_utc = datetime.now(timezone("UTC"))
print(datetime_utc)
```
> Melhor para projetos com banco de dados.
> Mais dinâmico.


## Se você quiser que seu objeto datetime seja "naive" (não atrelado a um fuso horário específico), qual atributo desse objeto deve ser None?
>Um objeto naive tem tzinfo=None, ou seja, não contém informações de fuso horário.

>Um objeto aware possui tzinfo definido, indicando o fuso horário associado.