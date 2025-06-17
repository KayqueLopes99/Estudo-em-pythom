from datetime import datetime, timedelta
from pytz import timezone
agora = datetime.now()  # Obtém a data e hora atual
print(agora)  # formato AAAA-MM-DD HH:MM:SS.mmmmmm)

data_str = '2024-05-15 21:59:26'

# Converte a string para um objeto datetime
data_obj = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
print(data_obj)  

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

print(dataInicio.strftime('%Y'), dataInicio.year)
print(dataInicio.strftime('%m'), dataInicio.month)
print(dataInicio.strftime('%d'), dataInicio.day)
