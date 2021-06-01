def cuadrado():
    print("1. AREA")
    print("2. PERIMETRO")
    x = int(input("Introduce la opción que desea:  "))
    if x == 1:
        perimetro()
    elif x == 2:
        area()
def perimetro():
    lado = int (input ("Ingrese el lado del cuadrado: "))
    p = 4*lado
    print("El perimetro es: ", p)
def area():
    lado = int (input ("Ingrese el lado del cuadrado: "))
    a = lado*lado
    print("El area es: ", a)
cuadrado()