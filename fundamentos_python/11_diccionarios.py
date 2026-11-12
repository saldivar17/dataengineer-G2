import pprint


users = [
    ["Juan", 25, "m", "juan@gmail.com"],
    ["Maria", 30, "f", "maria@gmail.com"],
    ["Pedro", 28, "m", "pedro@gmail.com"],
    ["Ana", 22, "f", "ana@gmail.com"]
]

new_users = []
i = 1
for user in users:
    user_dict = {
    "id": i,
    "name": user[0],
    "age": user[1],
    "gender": user[2],
    "email": user[3]
    }
    i += 1
    new_users.append(user_dict)

print("primer ejercicio")
pprint.pprint(new_users)
print("Fin del primer ejercicio")

vehiculos = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

""" Modificar y agregar elementos """
vehiculos["marca"] = "Honda"
vehiculos["color"] = "Rojo"
print(vehiculos)

""" Eliminar elementos """
del vehiculos["año"]
vehiculos.pop("color")
print(vehiculos)

# Metodos utiles
print(vehiculos.keys())
print(vehiculos.values())
print(vehiculos.items())

# Iterar sobre un diccionario
for clave in vehiculos:
   print(clave, vehiculos[clave]) # mejor rendimiento

for clave, valor in vehiculos.items():
    print(clave, valor) # mejor legibilidad
