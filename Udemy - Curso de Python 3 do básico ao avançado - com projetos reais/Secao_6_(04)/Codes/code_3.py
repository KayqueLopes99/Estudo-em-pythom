import calendar
print(calendar.calendar(2025)) # ano - Imprime o calendário no terminal.
print(calendar.month(2025, 2)) # ano / mes

# Numero do dia da semana  - Ultimo dia do mês.
print(calendar.monthrange(2023, 4))

# dias da semana
print(list(enumerate(calendar.day_name)))

primeiroDia, ultimoDia = calendar.monthrange(2022, 12)
## weekday retorna ao o numero do dia.
print(calendar.day_name[calendar.weekday(2022, 12, ultimoDia)])

# criar um calendario com [semana1] [semana n].

for week in calendar.monthcalendar(2022, 12):
    print(week)

