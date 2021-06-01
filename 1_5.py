def sumar(nombre:str):
    return len(nombre)
num1= input("Ingrese el primer nombre: ")
num2= input("Ingrese el segundo nombre: ")
cant1 = sumar(num1)
cant2 = sumar(num2)

if cant1 > cant2:
    print("El nombre", num1, "tiene mas caracteres que", num2)
else:
    print("El nombre", num2, "tiene mas caracteres que", num1)