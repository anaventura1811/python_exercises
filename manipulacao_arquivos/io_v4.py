try:
    arquivo = open('pessoas.csv')
    # dados = arquivo.read()
    # arquivo.close()
    for registro in arquivo:
        # print(*registro.split(','))
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

    # Otimizações na formatação e no consumo de memória
    # --> preferir não armazenar a leitura do arquivo numa variável
except IndexError:
    pass
finally:
    arquivo.close()
    if arquivo.closed:
        print('arquivo fechado')
