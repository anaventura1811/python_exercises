import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        with open('desafioIbge-solucao.txt', 'w') as saida:
            print('Baixando csv...')
            dados = entrada.read().decode('latin1')
            # ibgeFile = csv.reader(dados)
            # next(ibgeFile)
            print('download completo')
            for cidade in csv.reader(dados.splitlines()):
                print(f'{cidade[8]}: {cidade[3]}', file=saida)


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
