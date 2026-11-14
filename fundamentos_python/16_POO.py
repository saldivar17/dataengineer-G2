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

camioneta = Vehiculo("Toyota", "Blanco", "Hilux")
print(camioneta.color)

coches = Vehiculo("VW", "Negro", "Polo R")
coches.color = "Azul"
print(coches.color)