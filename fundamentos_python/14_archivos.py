# r: Modo lectura
# encoding = "utf-8": Ecita errores con tildes, eñes y caracteres especiales.
# with: Gestiona recursos de forma segura y automatica.

""" 
# forma 1. antigua
archivo = open("archivo.txt", "r")
contenido = archivo.read() # leer el contenido
archivo.close()
print(contenido)
"""
# forma 2. recomendable
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    #print(contenido)

""" Leer linea por linea """
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    rows = 0
    for linea in archivo:
        rows +=1
        if rows == 1:
            continue
        linea_sin_espacio = linea.strip()
        lenguaje = linea_sin_espacio.split(",")[-1]
        #print(lenguaje)

""" Guardar las lineas en una lista """
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

#print(lineas[0].strip())

""" Formatos estructurados comunes (CSV y JSON) """
import json     # Recomendacion: que este al inicio del archivo
import csv

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    #print(datos)

with open("datos1.json", "r", encoding="utf-8") as archivo:
    datos1 = json.load(archivo)
    #print(datos1)

with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    rows = 0
    for fila in lector:
        rows +=1
        if rows == 1:
            continue
        print(fila)
