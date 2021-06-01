
enteros=[]
contador=0

for x in range(8):
    auxiliar = int(input("ingrese el entero que desea almacenar:" ))
    enteros.append(auxiliar)
    if auxiliar>100:
        contador = contador + 1

print("los numeros almacenados son: ", enteros)
print("los enteros mayores a 100, son:",contador)