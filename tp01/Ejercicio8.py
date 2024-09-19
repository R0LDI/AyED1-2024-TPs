def dia_dela_semana(dia: int, mes: int, anio: int) -> int:
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100 
    diasemana = (((26 * mes - 2) // 10 ) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasemana < 0:
        diasemana = diasemana + 7 
    return diasemana 

def ames(dia: int, dias: int) -> list:
    lista_mes = []  
    return [0] * dia + list(range(1, dias + 1))

def imprime_el_mes(mes: int, anio: int, lista_mes: list) -> None:
    print()
    print(f'{meses[mes - 1]} de {anio}')
    for d in semana:
        print(f'{d}', end=' ')
    print()
    print(f'{"-" * (len(semana) * 4)}')
    contador = 0
    for d in lista_mes:
        if d:
            print(f'{str(d):>2}', end='  ')
        else:
            print(f'{" ":>2}', end='  ')
        contador += 1
        if contador % 7 == 0:
            print()
            contador = 0
    print()
    print(f'{"-" * (len(semana) * 4)}')
    return None

def main() -> None:
    mes = int(input("ingrese un numero de mes: "))
    anio = int(input("ingrese un numero del año: "))

    if mes in treintayuno:
        dias = 31
    elif mes in treinta:
        dias = 30
    elif not anio % 4 and (anio % 100 or not anio % 400):
        dias = 29
    else:
        dias = 28

    dia = dia_dela_semana(1, mes, anio)
    lista_mes = ames(dia, dias)
    imprime_el_mes(mes, anio, lista_mes)
    return None

treintayuno = (1, 3, 5, 7, 8, 10, 12)
treinta = (4, 6, 9, 11)
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
semana = ('DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB')
if __name__ == "__main__":
    main()