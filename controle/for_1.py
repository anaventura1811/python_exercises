# for i in range(10):
#   print(i)

# for i in range(1, 11):
#   print(i)

# for i in range(1, 100, 7):
#   print(i)

# for i in range(20, 0, -3):
#   print(i)

# nums = [1, 2, 3, 4, 5]
# for n in nums:
#   print(n, end=' ')

# texto = 'python'
# for letra in texto:
#   print(letra, end=' ')

# for n in { 1, 2, 3, 4, 4, 5, 6, 5 } :
#   print(n, end=' ')

produto = {
  'nome': 'caderno',
  'preco': 20.00,
  'desc': 0.2
}
# for atributo in produto:
#   print(atributo, produto[atributo])
#  chave, valor + métodos de dict
# for atributo, valor in produto.items():
#   print(atributo, '==>', valor)

# for valor in produto.values():
#   print(valor, end=" ")

for atributos in produto.keys():
  print(atributos)
