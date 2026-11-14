# resultado = 5 / 0

# Dentro de este bloque se ejecuta el codigo en el que puede ocurrir un error.
try:
    numero = int(input("Ingrese un numero : "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")

# Este bloque solo se ejecuta cuando ocurre un error.
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero")
except ValueError:
    print("Error: Debes ingresar un numero valido, no texto")
except Exception:
    print("Error: Ha ocurrido un error desconocido")

# Se ejecuta SOLO SI NO HUBO NINGUN ERROR en el bloque try
else:
    print("Proceso finalizado con exito")
    print(f"Resultado: {resultado}")

# Se ejecuta SIEMPRE (haya ocurrido un error o no)
finally:
    print("Proceso finalizado")


try:
    with open("file.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe")
else:
    print("Archivo leido con exito")
    print(contenido)
finally:
    print("El proceso de lectura a finalizado")