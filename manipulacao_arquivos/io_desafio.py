import csv

with open('desafio-ibge.csv', encoding='ISO-8859-1') as arquivo:
    with open('desafioIbge-3.txt', 'w') as saida:
        ibgeFile = csv.reader(arquivo)
        next(ibgeFile)
        for row in ibgeFile:
            print(f'{row[8]}: {row[3]}', file=saida)
