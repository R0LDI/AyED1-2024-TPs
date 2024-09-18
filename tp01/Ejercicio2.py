def fecha_gregoriana(d: int, m: int, a: int) -> bool:
    """
    Verifica si una fecha es válida.

    Argumentos:
        d (int): Día.
        m (int): Mes.
        a (int): Año.

    Retorna:
        bool: True si la fecha es válida, False en caso contrario.
    """
    treinta = [4, 6, 9, 11]
    anio = (a >= 0 and a <= 2100)
    mes = (m >= 1 and m <= 12)

    if m in treinta:
        dialim = 30
    elif m == 2:
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            dialim = 29
        else:
            dialim = 28
    else:
        dialim = 31

    dia = (d >= 1 and d <= dialim)
    return (dia and mes and anio)


def main():
    """
    Programa principal que solicita una fecha al usuario y verifica si es válida.
    """
    while True:
        dia = int(input('Ingrese día: '))
        if dia > 0 and dia <= 31:
            break

    while True:
        mes = int(input('Ingrese mes: '))
        if mes > 0 and mes <= 12:
            break

    while True:
        anio = int(input('Ingrese año: '))
        if anio > 0 and anio <= 2100:
            break

    if fecha_gregoriana(dia, mes, anio):
        print('La fecha es válida')
    else:
        print('Fecha inválida')


assert fecha_gregoriana(31, 2, 2022) == False
assert fecha_gregoriana(2, 6, 2560) == False
assert fecha_gregoriana(27, 2, 2100) == True

if __name__ == '__main__':
    main()