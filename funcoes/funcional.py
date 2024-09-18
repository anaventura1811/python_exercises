def soma_nums(a, b):
    return a + b

somar = soma_nums
print(somar(3, 4))

def operation_binary(fn, op_um, op_dois):
  return fn(op_um, op_dois)

resultado = operation_binary(soma_nums, 1, 2)
print(resultado)

def soma_parcial(a):
  def concluir_soma(b):
    return a + b
  return concluir_soma

# funções aninhadas
fn = soma_parcial(10)
resultado = fn(12)
print(resultado)

result = soma_parcial(20)(10)
print(result)