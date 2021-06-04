listas = []
mayor = 0.0
for x in range(5):
    val = float(input("Ingrese un sueldo: "))
    if val > mayor:
        mayor = val
        listas.append(val)
    else:
        listas.insert(0,val)
print("La lista ingresada es:",listas,"\nEl mayor numero es:",mayor)