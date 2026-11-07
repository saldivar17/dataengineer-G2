# Son colecciones ordenados y mutables de elementos que permiten almacenar mutiples elementos en una sola variable.
""" Son colecciones ordenados y mutables de elementos que permiten almacenar mutiples elementos en una sola variable. """

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ["python", "javascript", "c-sharp", "java", "c++", "go", "php", "ruby", "kotlin"]
lista3 = [1, 2, 3.1416, "Hola", True]

""" Acceder a elementos de una lista """
print(lista2[0])
print(lista3[-1])


""" Slicing(Rebanado) de listas """
print(lista1[1:4])
print(lista1[:5])
print(lista1[3:])
print(lista1[::2]) # paso 2
print(lista1[::3]) # paso 3

""" Modificar elementos de una lista """
lista1[3] = 10
print(lista1)

""" Agregar elementos a una lista """
lista1 = lista1 + [7, 8]
print(lista1)

""" Obtener la longitud de una lista """
print(len(lista1))

""" metodos de listas """
lista = ["python"]
lista.append("TypeScript")
print(lista)

lista.insert(1, "JavaScript")
print(lista)

lista.remove("python")
print(lista)

lista.pop(0)    #Por defecto elimina el último elemento.
print(lista)

print(lista.index("TypeScript"))

lista.append("TypeScript")
print(lista.count("TypeScript"))

""" Ordenar una lista """
lista_numeros = [5, 2, 9, 1, 7]
lista_numeros.sort()
print(lista_numeros)

lista_numeros.reverse()
print(lista_numeros)

#limpiar todo
lista_numeros.clear()
print(lista_numeros)