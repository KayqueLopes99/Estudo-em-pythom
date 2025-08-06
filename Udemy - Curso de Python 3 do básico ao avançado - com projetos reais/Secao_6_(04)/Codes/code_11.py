## csv.reader e csv.DictReader.
## csv.reader: Lê linhas de um arquivo CSV como listas.
## csv.DictReader: Lê linhas de um arquivo CSV como dicionários.

from pathlib import Path 
import csv
PATH_CSV = Path(__file__).parent / "arquivo_Aula_11.csv"

with open(PATH_CSV, 'r', encoding='utf-8') as file:
    scanner = csv.reader(file)

    for line in scanner:
        print(line)
        # print(line[0])
  
with open(PATH_CSV, 'r', encoding='utf-8') as file:
    scanner = csv.DictReader(file)

    for line in scanner:
        print(line)
        print(line['nome'], line['idade'], line['email'])


## Escrevendo dados em um arquivo CSV.
## csv.writer e csv.DictWriter para escrever em CSV
## csv.writer: Escreve linhas como listas.
## csv.DictWriter: Escreve linhas como dicionários.


list_data_client = [
    {'nome': 'isa', 'idade': 20, 'email': 'isa4556@gmail.com'},
    {'nome': 'joão', 'idade': 30, 'email': 'joao123@gmail.com'},
    {'nome': 'maria', 'idade': 25, 'email': 'maria.silva@gmail.com'},
    {'nome': 'carlos', 'idade': 28, 'email': 'carlos_oliveira@gmail.com'},
    {'nome': 'ana', 'idade': 22, 'email': 'ana.souza@gmail.com'},
    {'nome': 'pedro', 'idade': 35, 'email': 'pedro.lima@gmail.com'},
]

with open(PATH_CSV, 'a', encoding='utf-8', newline='') as file:
    # colocar nome das colunas
    # colum_names =  list_data_client[0].keys()
    scanner = csv.writer(file)

    #scanner.writerow(colum_names)

    for client in list_data_client:
        scanner.writerow(client.values())
        




