with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo foi fechado')
if saida.closed:
    print('arquivo de saída foi fechado')
# Mais otimizado e alternativa mais pythonica para abrir e ler arquivos
# with pode acessar para abertura e fechamento de conexões tbm,
# alternativa menos complicada do que blocos de try e finally
