from typing import List
from random import randint

def cosecha(n: int) -> List[int]:
    lista = []
    for _ in range(n):
        lista.append(randint(150, 350))
    return lista

def total_cajones(l: List[int]) -> tuple[int]:
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


def carga_camion(p_camion: int, p_cajones: int) -> tuple[int]:
    cajones_cargados = []
    peso = 0 
    for cajon in p_cajones:
        peso =+ cajon
        if peso > p_camion:
            cajones_cargados.append((peso - cajon) / 1_000)
            peso = cajon
    return cajones_cargados, peso

if __name__ == '__main__':
    cantidad_cajon = 100
    cantidad_camiones = 25
    capacidad_camion = 400000
    cantidad_naranjas = 100000

    cosechadas = cosecha(cantidad_naranjas)
    peso_cajones, cant_cajones, sobraron = total_cajones(cosechadas)
    peso_total = sum(cosechadas)


    print(f'Se cosecharon {peso_total / 1_000_000:.3f} toneladas de naranjas.')
    print(f'Hay {jugo(cosechadas)} naranjas para jugo de un total de {cantidad_naranjas}\n')

    print(f'Hay {cant_cajones} cajones para cargar')
    print(f'Y sobraron {sobraron} naranjas que no completaron el último cajón.\n')

camiones_cargados, ultimo = carga_camion(capacidad_camion, peso_cajones)
for i, peso in enumerate(camiones_cargados):
    if i < cantidad_camiones:
        print(f'En el camion {i + 1:>2} van {peso} kilos')

if len(camiones_cargados) >= cantidad_camiones:
    print(f'\nHay carga para despachar {len(camiones_cargados) - cantidad_camiones} camiones mas')
else:
    print(f'\nHay carga para despachar {len(camiones_cargados)} camiones llenos.')
if (ultimo / 1000) < (capacidad_camion / 1000 * 0.80):
    print(f'no hay suficiente carga para despachar el ultimo camion\nsolo hay {ultimo} para el ultimo camion')
          