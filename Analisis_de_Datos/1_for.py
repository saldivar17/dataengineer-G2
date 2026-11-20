#iterar: recorrer
#iterador: variable que recorre
#iterable: conjunto de datos

ventas = [320, 410, 280, 560]
dias = ['lunes', 'martes', 'miercoles', 'jueves']
datos = list(zip(ventas, dias))
datos2 = list(ventas, dias)

print(datos2)

for venta, dia in datos:
  print(f"venta del día {dia}: {venta}")

print(datos)

#resultado  
#venta del día lunes: 320
#venta del día martes: 410
#venta del día miercoles: 280
#venta del día jueves: 560