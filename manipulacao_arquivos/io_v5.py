with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo foi fechado')
# Mais otimizado e alternativa mais pythonica para abrir e ler arquivos
# with pode acessar para abertura e fechamento de conexões tbm,
# alternativa menos complicada do que blocos de try e finally
