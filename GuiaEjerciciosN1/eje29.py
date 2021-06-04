lista = []
for x in range(5):
    val = float(input("Ingrese las alturas: "))
    lista.append(val)
promedio = sum(lista)/5
bajas=0
altos=0
for x in lista:
    if x<promedio:
        bajas += 1
    elif x>=promedio:
        altos += 1
print("La alturas ingresadas son:",lista,"\nEl promedio es:",promedio,"\nLas personas mayores al promedio son:",altos,"\nLas personas menores al promedio son:",bajas)