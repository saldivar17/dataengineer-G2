# POO = uso de clases en python
"""
Las clases nos permite implementar el paradigma de Programación Orientado a Objetos (POO).
Nos permite crear tipos de datos, encapsular atributos y comportamientos; y organizar 
codigo de forma modular y reutilizable
"""

class Persona:
    pass

class Vehiculo:
    def __init__(self, marca, color, modelo): # Es un metodo magico (magic method), por convencio utilizamos self por defecto.
        self.marca = marca
        self.color = color
        self.modelo = modelo
        # Encapsulacion
        self.__codigo = "VW00001"
    
    def ver_datos(self):
        print(f"Este vehiculo es de marca {self.marca}, color: {self.color}, modelo: {self.modelo} y codigo: {self.__codigo}")

    ##Encapsulacion
    def __informacion_privada(self):
        print(f"Esta información es privada : {self.__codigo}")

camioneta = Vehiculo("Toyota", "Blanco", "Hilux")
print(camioneta.color)

coches = Vehiculo("VW", "Negro", "Polo R")
coches.color = "Azul"
print(coches.color)
coches.ver_datos()
#print(coches.__codigo) 



# Hacer un contador de tiempo para el refrigerio, quizas con una control de barra, pero todo en la consola. (pendiente)

# Herencia: Permite crear clases derivadas que heredan atributos y metodos.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saltar(self):
        print(f"{self.nombre} ha saltado")

    @staticmethod # Decorador: es una funcion(la que esta debajo), modifica su comportamiento
    def vacunas(mensaje):
        print(mensaje)

# Herencia
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Miauu!")

perro = Animal("Roberto")
perro.saltar()
perro.vacunas("Las vacunas estan al día")

#Herencia
gato = Gato("Pelusa")
gato.saltar()
gato.hablar()