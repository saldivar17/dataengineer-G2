stock = int(input("Ingrese un numero: "))
while (stock > 0):
  print(f'Quedan {stock} unidades')
  stock = stock - 1   # stock -= 1 (operadores de asignación)

print("Se acabo el stock")