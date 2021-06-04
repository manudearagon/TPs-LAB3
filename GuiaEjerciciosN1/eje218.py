lista1 = [1]
lista2 = [2,3]
lista3 = [4,5,6]
lista4 = [7,8,9,10]
lista5 = [11,12,13,14,15]
lista_anidada = [lista1,lista2,lista3,lista4,lista5]
suma = 0
for x in lista_anidada:
    suma += sum(x)
print("La lista es:",lista_anidada,"\nLa suma es:",suma)