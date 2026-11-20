# year = int(input("Ingrese el año : "))
# for i in range(year):
#     print(f"año : {i + 1}")

num = int(input("Ingrese un numero entero positivo: "))
if (num > 0):
    for i in range(num):
        if (i % 2 != 0):
            print(i)
else:
    print("Ingreso mal el numero : if")   