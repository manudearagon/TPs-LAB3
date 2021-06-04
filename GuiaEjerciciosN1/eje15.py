string = input("Ingrese una oracion: ")
cantidad = 0
for x in string:
    if x == " ":
        cantidad += 1
print("La cantidad de espacios que tiene la oracion es:",cantidad)