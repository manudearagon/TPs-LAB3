lista = []
val = -1
while val != 0:
    val = int(input("Ingrese un numero entero: "))
    if val == 0:
        break
    else:
        lista.append(val)
print("La lista ingresada es:",lista)

'''
lista = []
val = int(input("Ingrese un numero entero: "))
while val != 0:
    lista.append(val)
    val = int(input("Ingrese un numero entero: "))
print("La lista ingresada es:",lista)
'''