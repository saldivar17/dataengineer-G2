""" Recuperar la informacion de datos.CSV y construir una lista de diccionarios con estos datos, ademas se debe ordenar por 
orden alfabetico en base a los apellidos, tambien se les debe generar una constraseña encriptada por defecto en base a la fecha de nacimiento"""
# Output [{"id": 1, "nombre": "...", ... , "activo": True}, {}, ... , {}]

import csv
import hashlib


class Usuario:
    def __init__(
        self,
        id, 
        nombre, 
        apellidos, 
        email, 
        telefono, 
        ciudad,
        pais,
        fecha_registro,
        activo
    ):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_registro = fecha_registro
        self.activo = activo
        self.password = self.__generar_password_encriptada()

    def __generar_password_encriptada(self):
        fecha_registro_bytes = self.fecha_registro.encode("utf-8")
        return hashlib.sha256(fecha_registro_bytes).hexdigest()

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellidos,
            "email": self.email,
            "telefono": self.telefono,
            "ciudad": self.ciudad,
            "pais": self.pais,
            "fecha_registro": self.fecha_registro,
            "activo": self.activo,
            "password": self.password
        }

def main():
    usuarios_objetos = []

    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        rows = 0
        for fila in lector:
            rows +=1
            if rows == 1:
                continue
            usuario = Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
                fila[8]
            )
            usuario_dict = usuario.to_dict()
            # print(usuario_dict)
            usuarios_objetos.append(usuario)

    def obtener_apellido(usuario):
        return usuario.apellidos.lower()

    usuarios_ordenados = sorted(
        usuarios_objetos,
        key=obtener_apellido
        # key=lambda u: u.apellidos.lower()
    )

    resultado_final = []
    for user in usuarios_ordenados:
        resultado_final.append(user.to_dict())

    print(resultado_final)

if __name__ == "__main__":
    main()

