lista = []
for x in range(5):
    val = input("Ingrese un nombre: ")
    lista.append(val)
lista.sort()
print("La lista ingresada es:",lista,"\nEl primer nombre en orden alfabetico es:",lista[0])