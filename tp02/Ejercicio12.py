from typing import Dict

def carga_ingresos() -> Dict[int, int]:
    socios = {}
    while True:
        socio = int(input('Ingrese el número de socio | 0 para finalizar: '))
        if socio == 0:
            break
        if socio >= 10000 and socio <= 99999:
            if socio in socios:
                socios[socio] += 1
            else:
                socios[socio] = 1
        else:
            print('num de socio invalido')
    return socios

def listado(socios: Dict[int, int]) -> None:
    for socio in socios:
        print(f'El socio {socio} tuvo: {socios[socio]} ingresos al club.')
    return None

def bajas(socios: Dict[int, int]) -> None:
    print('Ingresos de socios')
    for socio in socios:
        print(f'El socio {socio} tuvo {socios[socio]} ingresos al club.')
    while True:
        socio = int(input('Ingrese el número de socio para la baja: '))
        if socio == 0:
            break
        if socio >= 10000 and socio <= 99999:
            if socio in socios:
                ingresos = socios[socio]
                del socios[socio]
                print(f'Se eliminaron {ingresos} ingresos del socio {socio}.')
            else:
                print('Código de socio no encontrado!')
        else:
            print('Código de socio no válido!')
    print('\nLa nueva lista es')
    for socio in socios:
        print(f'El socio {socio} tuvo {socios[socio]} ingresos al club.')
    return None

socios = carga_ingresos()
print()
listado(socios)
print()
bajas(socios)