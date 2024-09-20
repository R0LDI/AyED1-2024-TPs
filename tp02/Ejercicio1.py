import random as rn 
#import math
from typing import List

def cargar() -> List[int]:
    lista = []
    for i in range(rn.randint(10, 99)):
        lista.append(rn.randint(1000, 9999))
    return lista

def producto(lista: List[int]) -> int:
    resultado = 1
    for elem in lista:
        resultado *= elem
    return resultado
    #return math.prod(lista)

def eliminar(dato: int, lista: List[int]) -> List[int]:
    return [elem for elem in lista if elem != dato]

def capicua(lista: List[int]) -> bool:
    return lista == lista[::-1]

if __name__ == '__main__':
    lista1 = cargar()
    print(f"lista original: {lista1}")
    print(f"longitud: {len(lista1)}")
    print(f"producto: {producto(lista1)}")
    print(f"es capicua: {capicua(lista1)}")
    valor_eliminar = int(input("Ingresa un valor para eliminar:  "))
    lista1 = eliminar(valor_eliminar, lista1)
    print(f"despues de eliminar, la lista es {valor_eliminar}: {lista1}")

