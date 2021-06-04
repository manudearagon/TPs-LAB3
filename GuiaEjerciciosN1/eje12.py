string = input("Ingrese su nombre: ")
string = string.lower()
print("Su nombre es:",string)
if (string[0]=="a" or string[0]=="e" or string[0]=="i" or string[0]=="o" or string[0]=="u"):
    print("El nombre empieza con una vocal")
else:
    print("El nombre no empieza con una vocal")
    