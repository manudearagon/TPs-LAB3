string = input("Ingrese su clave: ")
if len(string)<10 or len(string)>20:
    print("Error")
else:
    print("Contraseña correcta")

'''
if len(string)>10 and len(string)<20:
    print("Contraseña correcta")
else:
    print("Error")
'''