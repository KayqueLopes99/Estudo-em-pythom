## CSV (Comma Separated Values - Valores separados por vírgulas)
- É um formato de arquivo que armazena dados em forma de tabela, onde cada
- linha representa uma linha da tabela e as colunas são separadas por vírgulas.
- Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
- plataformas, como por exemplo, para importar ou exportar dados para uma
- planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
- Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
- editor de texto ou em uma planilha eletrônica.
- Um exemplo de um arquivo CSV pode ser:
- Nome,Idade,Endereço
- Luiz Otávio,32,"Av Brasil, 21, Centro"
- João da Silva,55,"Rua 22, 44, Nova Era"
- A primeira linha do arquivo define os nomes das colunas da, enquanto as
- linhas seguintes contêm os valores das linhas, separados por vírgulas.
- Regras simples do CSV
- 1 - Separe os valores das colunas com um delimitador único (,)
- 2 - Cada registro deve estar em uma linha
- 3 - Não deixar linhas ou espaços sobrando
- 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

## Leitura com csv.reader e csv.DictReader.
- csv.reader: Lê linhas de um arquivo CSV como listas.
- csv.DictReader: Lê linhas de um arquivo CSV como dicionários.

```` python
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
        
        
````

## Escrevendo dados em um arquivo CSV.
## csv.writer e csv.DictWriter para escrever em CSV
## csv.writer: Escreve linhas como listas.
## csv.DictWriter: Escreve linhas como dicionários.

`````python
from pathlib import Path
import csv
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
        
````


