from time import sleep

# lista = ["python", "javascript", "c-sharp", "java"]
# tupla = ("c++", "go", "php", "ruby", "kotlin")

contador = 0

while contador < 10:
    contador += 1
    sleep(.5)
    print(f"El contador es: {contador}")

""" Salir de un bucle while con break """
while True:
    contador += 1
    sleep(.2)
    print(f"El contador es: {contador}")

    if contador == 20:
        print("Se termino el bucle")
        respuesta = input("quieres deterner el bucle? (s/n): ")

        if respuesta == "s":
            break
        else:
            print("Continuamos con el bucle")
            respuesta = "n"
            contador = 0

""" Salir de un bucle while con continue """
contador = 0
while True:
    contador += 1
    if contador % 2 == 0:
        continue # Salta la iteracion cuando el contador es 5
    print(f"El contador es: {contador}")

    if contador >= 9:
        break
else: 
    print("Se termino el bucle 🐍")