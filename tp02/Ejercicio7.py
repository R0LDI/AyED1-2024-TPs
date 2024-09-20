def intercala(lista1, lista2):
    for i in range(len(lista2)):
        lista1[(i*2+1):(i*2+1)] = lista2[i:i+1]
    return lista1

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]

print(intercala(lista1, lista2))