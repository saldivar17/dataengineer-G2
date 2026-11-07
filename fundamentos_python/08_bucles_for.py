lista = ["python", "javascript", "c-sharp", "java", "c++", "go", "php", "ruby", "kotlin"]

""" Recorrer una lista con un bucle for """
index = 1
for lenguaje in lista:
    print(f"{index}. {lenguaje}")
    index += 1

""" Recorrer cadenas de texto """
texto = "i Love Python"

for letra in texto:
    print(letra)

""" Recorrer una lista con un indice """
for index, lenguaje in enumerate(lista):
    #print(f"{index}. {lenguaje}")
    print(index, lenguaje)