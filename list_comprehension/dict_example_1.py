dicionario = {f'{i}': i ** 2 for i in range(10) if i % 2 == 0}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} elevado a 2 = {dobro}')
