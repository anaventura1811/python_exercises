from math import pi
PI = pi


def square(side):
    '''Calcula metro quadrado'''
    return side ** 2


def rectangle(length, width):
    return length * width


# raio = input('Informe o valor do raio: ')
# print('Área da circunferência: ', PI * float(raio) ** 2)

def circle():
    raio = input('Informe o valor do raio da circunferência: ')
    circleValue = PI * float(raio) ** 2
    print('Área da circunferência: ', circleValue)

# def circle(raio):
# print('Área do círculo: ', PI * raio ** 2)


if __name__ == "__main__":
    print('Área do quadrado:', square(10))
    print('Área do retângulo:', rectangle(2, 2))
    circle()
    # print('Área do círculo:', circle(3))
