def carga():
    num1 = int (input ("Ingrese el primer valor"))
    num2 = int (input ("Ingrese el segundo valor"))
    return num1,num2
def suma(num1,num2):
    return (num1 + num2)
def mensaje():
    print("Cierre de programa")

valores = carga()
print("El valor de la suma es: ", suma( valores[0], valores[1]))
mensaje()
