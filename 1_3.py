numero = []

def carga():
    for i in range(3):
        num = int(input("Introduce el número: "))
        numero.append(num)
carga()
a = sorted(numero)
print("El mayor numero es:",numero[-1])
