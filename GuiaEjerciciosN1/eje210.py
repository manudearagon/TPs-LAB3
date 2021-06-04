'''
mañana = []
tarde = []
for x in range(8):
    if x<=4:
        val = float(input("Ingrese los sueldos del turno mañana: "))
        mañana.append(val)
    else:
        val = float(input("Ingrese los sueldos del turno tarde: "))
        tarde.append(val)
print("Sueldos mañana:",mañana,"\nSueldos tarde:",tarde)
'''
mañana = []
tarde = []
cant_mañana = int(input("Ingrese la cantidad de empleados de la mañana: "))
cant_tarde = int(input("Ingrese la cantidad de empleados de la tarde: "))
for x in range(cant_mañana):
    val = float(input("Ingrese los sueldos del turno mañana: "))
    mañana.append(val)
for x in range(cant_tarde):
    val = float(input("Ingrese los sueldos del turno tarde: "))
    tarde.append(val)
print("Sueldos mañana:",mañana,"\nSueldos tarde:",tarde)