def diasiguiente(d, m, a):
    if m in [4, 6, 9, 11]:
        dialimit = 30
    elif m == 2:
        dialimit = 29 if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) else 28
    else:
        dialimit = 31
    d = (d + 1) % (dialimit + 1)
    if d == 0:
        d = 1
        m = (m + 1) % 12  
        if m == 0:
            m = 1
            a += 1
    return d, m, a

def main():
    fecha = (27, 2, 2024)
    dias = 365
    dia, mes, anio = fecha
    for _ in range(dias):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    print(f'despues de {dias} dias desde {fecha[0]}/{fecha[1]}/{fecha[2]} la fecha sera {dia}/{mes}/{anio}')

    hasta = (2, 10, 2024)
    dia, mes, anio = fecha
    contador = 0
    while (dia, mes, anio) != hasta:
        dia, mes, anio = diasiguiente(dia, mes, anio)
        contador += 1
    print(f'Hay {contador} dias entre {fecha[0]}/{fecha[1]}/{fecha[2]} y {hasta[0]}/{hasta[1]}/{hasta[2]}')

if __name__ == "__main__":
    main()