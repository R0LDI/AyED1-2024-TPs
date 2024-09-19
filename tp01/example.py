from typing import List
from random import randint

def cosecha(n: int) -> List[int]:
    lista = []
    for _ in range(n):
        lista.append(randint(150, 350))
    return lista

def total_cajones(l: List[int]) -> tuple[List[int], int, int]:
    cajones = []
    cantidad = 0
    peso = 0
    for naranja in l:
        if naranja >= 200 and naranja <= 300:
            peso += naranja
            cantidad += 1
        if cantidad == 100:
            cajones.append(peso)
            cantidad = 0 
            peso = 0
    if cantidad:
      cajones.append(peso)
    sobrante = cantidad
    return cajones, len(cajones), sobrante

def jugo(l: List[int]) -> int:
    total = 0 
    for naranja in l:
        if naranja < 200 or naranja > 300:
            total += 1
    return total

def carga_camion(p_camion: int, p_cajones: List[int]) -> int:
    camiones_necesarios = 0
    peso_actual = 0
    for cajon in p_cajones:
        if peso_actual + cajon > p_camion:
            camiones_necesarios += 1
            peso_actual = cajon
        else:
            peso_actual += cajon
    if peso_actual > 0:
        camiones_necesarios += 1
    return camiones_necesarios

if __name__ == '__main__':
    cantidad_cajon = 100
    cantidad_camiones = 40
    capacidad_camion = 500000 
    cantidad_naranjas = 100000

    cosechadas = cosecha(cantidad_naranjas)
    peso_cajones, cant_cajones, sobraron = total_cajones(cosechadas)
    peso_total = sum(cosechadas)

    print(f'Se cosecharon {peso_total / 1_000_000:.3f} toneladas de naranjas.')
    print(f'Hay {jugo(cosechadas)} naranjas para jugo de un total de {cantidad_naranjas}\n')

    print(f'Hay {cant_cajones} cajones para cargar')
    print(f'Y sobraron {sobraron} naranjas que no completaron el último cajón.\n')

    camiones_necesarios = carga_camion(capacidad_camion, peso_cajones)
    print(f'Se necesitan {camiones_necesarios} camiones para transportar la cosecha.')
    if camiones_necesarios > cantidad_camiones:
        print(f'No hay suficientes camiones para transportar la cosecha. Faltan {camiones_necesarios - cantidad_camiones} camiones.')
    else:
        print(f'Hay suficientes camiones para transportar la cosecha.')
