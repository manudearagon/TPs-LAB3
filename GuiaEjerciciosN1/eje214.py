lista = []
mayor = 0
cantidad = 0
for x in range(5):
    val = int(input("Ingrese un numero entero: "))
    lista.append(val)
    if val > mayor:
        mayor = val
        cantidad = 1
    elif val == mayor:
        cantidad += 1
print("La lista ingresada es:",lista,"\nEl mayor numero es:",mayor,"\nLa cantidad de mayores es:",cantidad)