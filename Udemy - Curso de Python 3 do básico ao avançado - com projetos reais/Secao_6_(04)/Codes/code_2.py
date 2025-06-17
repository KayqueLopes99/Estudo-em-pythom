from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

formato = '%d/%m/%Y'
dataInicioEmprestimo = datetime(2020, 12, 20)

valorTotal = 1_000_000
deltaAnos = relativedelta(years=5)
dataFimEmprestimo = dataInicioEmprestimo + deltaAnos

valor_parcela = valorTotal / 60

print("Datas de Vencimento do Empréstimo:")
indice = 1  
for data in range(1, 61):
    print(f"Parcela [{indice}] - {dataInicioEmprestimo.strftime(formato)} - {valor_parcela:,.2f}")
    dataInicioEmprestimo += relativedelta(months=1)
    indice +=1
    

print(
    f'Você pegou R$ {valorTotal:,.2f} para pagar em {deltaAnos.years} anos equivalente a (60 meses) em parcelas de R$ {valor_parcela:,.2f}.')


