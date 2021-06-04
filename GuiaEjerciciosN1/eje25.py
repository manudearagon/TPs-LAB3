lista = ["Manuel","Juan","Lucas","Matias","Federico"]
contador = 0
for x in lista:
    if len(x) >= 5:
        contador +=1
print("La cantidad de nombres que tienen mas de 5 caracteres son:",contador)