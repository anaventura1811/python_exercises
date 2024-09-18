from functools import reduce


# for nota, val in enumerate(notas):
#   notas[nota] = val + 1.5

# print(notas)
def mais_um_meio(nota):
  return nota + 1.5

def somar_nota(delta):
  def calc(nota):
    return nota + delta
  return calc

notas = [6.4, 7.2, 5.8, 8.4]
notas_finais = map(somar_nota(2.5), notas)

def somar(a, b):
  return a + b

total = reduce(somar, notas, 0)
print(total)