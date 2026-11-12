import pprint
ventas_crudas = [
    {
        "id_venta": 1001,
        "cliente": " mArÍa fErNaNdA lÓpEz ",
        "email": "maria.lopez@techcorp.pe",
        "subtotal": 250.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4557-8890-1234",
    },
    {
        "id_venta": 1002,
        "cliente": "carlos_ruiz",
        "email": "cruiz_sin_arroba.com",
        "subtotal": 120.0,
        "impuesto": 0.0,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5120-4432-9981",
    },
    {
        "id_venta": 1003,
        "cliente": None,
        "email": "contacto@startup.io",
        "subtotal": -50.0,  # Error de registro (monto negativo)
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4111-2222-3333",
    },
    {
        "id_venta": 1004,
        "cliente": " ROBERTO GÓMEZ ",
        "email": "rgomez@gmail.com",
        "subtotal": 500.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "CANCELADO",  # Debe filtrarse
        "tarjeta": "4916-0098-7765",
    },
    {
        "id_venta": 1005,
        "cliente": "",
        "email": "ventas@logistica.com",
        "subtotal": 80.0,
        "impuesto": 0.18,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5412-7500-8812",
    },
    {
        "id_venta": 1006,
        "cliente": " lucía mendieta",
        "email": "lucia@finanzas.pe",
        "subtotal": 5.0,  # Debajo del monto mínimo
        "impuesto": 0.18,
        "moneda": "EUR",  # Moneda no soportada
        "estado": "COMPLETADO",
        "tarjeta": "4000-1234-5678",
    },
]

""" Elimina los espacios extras y aplica formato título """

def limpiar_nombre(nombre_crudo : str | None): # str es una anotación de tipo string.
    if not nombre_crudo or not nombre_crudo.strip():
        return "Desconocido"
    return nombre_crudo.strip().title()
    
    
    # print(nombre_crudo.strip().title())  # Output: María Fernanda López
    
print(limpiar_nombre(ventas_crudas[0]["cliente"]))  # Output: María Fernanda López


""" Ejercicio 2. Extractor de dominio de correo """
# input: "lucia@finanzas.pe"
# output: "finanzas.pe"
def extraer_dominio(email: str): 
    if "@" not in email:
        return "dominio_desconocido.com"
    return email.split("@")[-1].strip().lower()

print(extraer_dominio(ventas_crudas[0]["email"]))

""" Ejercicios 3. Validador de moneda, solo se permite PEN, USD y montos """

def transaccion_valida(monto: float, moneda: str):
    monedas_permitidas = ("PEN", "USD")
    if monto >=0 and moneda.upper() in monedas_permitidas:
        return True
    return False

""" Ejercicio 4. Conversor de divisas con tasa configurable """
def convertir_usd(monto: float, moneda_origen: str, tasa_cambio: float):
    moneda = moneda_origen.upper()
    if moneda == "PEN":
        return round(monto / tasa_cambio, 2)
    if moneda == "USD":
        return round(monto, 2)

""" Ejercicios 5. Orquestador del pipeline """
# 1. Filtrar por el estado del negocio, tiene que estar COMPLETADO.
# 2. Limpiar los nombres
# 3. Determinar el dominio
# 4. Validar transaccion
# 5. Convertir a USD
# 6. Construir un diccionario de salida

def ejecutar_pipeline(datos_crudos: list[dict]):
    registros_limpios = []
    descartados = 0
    monto_total = 0
    # 1.
    for fila in datos_crudos:
        if fila["estado"] != "COMPLETADO":
            descartados +=1
            continue
        # 2.
        fila["cliente"] = limpiar_nombre(fila["cliente"])
        
        #3.
        fila["dominio"] = extraer_dominio(fila["email"])
        
        # 4.
        if not transaccion_valida(fila["subtotal"], fila["moneda"]):
            continue
        
        # 5.
        fila["subtotal"] = convertir_usd(fila["subtotal"], fila["moneda"], 3.76)
        fila["moneda"] = "USD"
        monto_total+=fila["subtotal"]
        registros_limpios.append(fila)
    
    return{
        "data final": registros_limpios,
        "registro_procesados": len(datos_crudos),
        "registros descartados": descartados,
        "monto_total_usd": monto_total
    }

pprint.pprint(ejecutar_pipeline(ventas_crudas))
    