# Conceitos  Notas
# E          De 2,0 a 1,1
# E-         De 1,0 a 0,0
def nota():
    notaAluno = input('Digite a nota: ')
    if (float(notaAluno) >= 9.1):
        print('Conceito A')
    elif (float(notaAluno) >= 8.1 <= 9.0):
        print('Conceito A-')
    elif (float(notaAluno) >= 7.1 <= 8.0):
        print('Conceito B')
    elif (float(notaAluno) >= 6.1 <= 7.0):
        print('Conceito B-')
    elif (float(notaAluno) >= 5.1 <= 6.0):
        print('Conceito C')
    elif (float(notaAluno) >= 4.1 <= 5.0):
        print('Conceito C-')
    elif (float(notaAluno) >= 3.1 <= 4.0):
        print('Conceito D')
    elif (float(notaAluno) >= 3.1 <= 4.0):
        print('Conceito D')
    elif (float(notaAluno) >= 2.1 <= 3.0):
        print('Conceito D-')
    elif (float(notaAluno) >= 1.1 <= 2.0):
        print('Conceito E')
    else:
        print('Conceito E-')


nota()
