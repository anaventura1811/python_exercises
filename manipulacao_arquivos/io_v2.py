arquivo = open('pessoas.csv')
# dados = arquivo.read()
# arquivo.close()
for registro in arquivo:
    # print(*registro.split(','))
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
