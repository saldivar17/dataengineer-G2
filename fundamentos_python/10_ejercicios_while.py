""" 1. Validad que una contraseña tenga al menos 8 caracteres"""
# input : "1234567"

print("=== Validar contraseña ===")

while True:
    password = input("Ingrese una contraseña: ")

    if len(password) == 8:
        print("Contraseña valida")
        break
    else:
        print("La contraseña deber tener al menos 8 caracteres")


""" 2. Ingresar un numero y crea una tabla de multiplicacion hasta el 10 """
print("\n=== Tabla de multiplicacion ===")

numero = int(input("Ingrese un numero: "))
contador = 1
while True:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
    if contador > 10:
        break