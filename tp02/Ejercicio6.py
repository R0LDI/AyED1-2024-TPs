def normaliza(lista: list[int]) -> list[float]:

    suma = sum(lista)
    nueva = [elem/suma for elem in lista]
    return nueva

lista1 = [1, 1, 2]
print(normaliza(lista1))  