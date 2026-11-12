""" Definiciones de funciones """
def saludar():
    print("¡Hola maldito!")

# Llamada a la función
saludar() 


""" Funcion con parametros """
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)  # Output: 8

""" Función con parámetros y valor por defecto """

def saludar_persona(nombre="invitado"):
    print(f"Hola {nombre} !!")

saludar_persona("Juan")  # Output: Hola Juan!
saludar_persona()  # Output: Hola invitado!!

""" Funciones con número variables de argumentos """
# *args (es una tupla)
def mostrar_numeros(*numeros):
    # args: (1, 2, 3, 4, 5)
    for num in numeros:
        print(num)

mostrar_numeros(1, 2, 3, 4, 5)  # Output: 1 2 3 4 5

""" **kwargs (es un diccionario)"""
# sin kwargs
def mostrar_informacion(nombre, edad):
    print(nombre, edad)

mostrar_informacion(nombre="Eduardo", edad=30)  # Output: Juan 30

def mostrar_informacion_kwargs(**info):
    # kwargs: {'nombres': 'Eduardo', 'edad': 30, 'ciudad': 'Madrid'}
    for clave in info:
        print(f"{clave}: {info[clave]}")

mostrar_informacion_kwargs(nombre="Eduardo", edad=30, ciudad="Madrid")