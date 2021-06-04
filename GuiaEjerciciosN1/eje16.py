string = input("Ingrese una oracion: ")
string_low = string.lower()
contador = 0
for x in string_low:
    if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
        contador += 1
print("La cantidad de vocales es:",contador)