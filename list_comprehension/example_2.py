dobros = [i ** 2 for i in range(1, 22) if i % 2 == 0]
print(dobros)


dobro = []
for i in range(1, 22):
    if i % 2 == 0:
        dobro.append(i ** 2)
print('dobro: ', dobro)
