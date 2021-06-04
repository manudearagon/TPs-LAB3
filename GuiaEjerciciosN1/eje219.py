lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
print("Lista antes:",lista)
for x in range(len(lista)):
    for j in range(len(lista[x])):
        if lista[x][j] > 10:
            lista[x][j] = 0
print("Lista despues:",lista)
