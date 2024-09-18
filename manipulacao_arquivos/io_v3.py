arquivo = open('pessoas.csv')
# dados = arquivo.read()
# arquivo.close()
for registro in arquivo:
    # print(*registro.split(','))
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()


# Otimizações na formatação e no consumo de memória
# --> preferir não armazenar a leitura do arquivo numa variável
