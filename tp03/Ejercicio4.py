import random

def generar_matriz_fabricacion(n: int) -> list:
    matriz = []
    for i in range(n):
        fila = [random.randint(0, 150) for _ in range(6)] 
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz: list, nombre_filas: str = "Fábrica") -> None:
    print(f"|{nombre_filas:^7}|Lun|Mar|Mie|Jue|Vie|Sáb|")
    print("-" * 35)  
    for i, fila in enumerate(matriz):
        print(f"|{i + 1:0>3}      |", end="")  
        for valor in fila:
            print(f"{valor:>3}|", end="") 
        print()
    print("-" * 35)


def calcular_produccion_total(matriz: list) -> list:
    return [sum(fila) for fila in matriz]


def encontrar_maxima_produccion_diaria(matriz: list) -> tuple:
    max_produccion = 0
    max_fabrica = 0
    max_dia = 0

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor > max_produccion:
                max_produccion = valor
                max_fabrica = i + 1
                max_dia = j + 1

    return max_produccion, max_fabrica, max_dia


def encontrar_dia_mas_productivo(matriz: list) -> tuple:
    produccion_dias = [sum([fila[j] for fila in matriz]) for j in range(6)]
    dia_mas_productivo = produccion_dias.index(max(produccion_dias)) + 1
    max_produccion = max(produccion_dias)

    return dia_mas_productivo, max_produccion


def calcular_menor_produccion_fabrica(matriz: list) -> list:
    return [min(fila) for fila in matriz]


if __name__ == "__main__":
    n = int(input("Ingrese el número de fábricas (n): "))

    matriz_produccion = generar_matriz_fabricacion(n)

    print("\nMatriz de Fabricación:")
    imprimir_matriz(matriz_produccion)

    print("\nProducción Total por Fábrica:")
    produccion_total = calcular_produccion_total(matriz_produccion)
    for i, total in enumerate(produccion_total):
        print(f"Fábrica {i+1}: {total}")

    max_produccion, max_fabrica, max_dia = encontrar_maxima_produccion_diaria(
        matriz_produccion
    )
    print(
        f"\nMáxima producción diaria: {max_produccion} bicicletas (Fábrica {max_fabrica}, Día {max_dia})"
    )

    dia_mas_productivo, produccion_dia = encontrar_dia_mas_productivo(
        matriz_produccion
    )
    print(
        f"Día más productivo: Día {dia_mas_productivo} ({produccion_dia} bicicletas)"
    )

    menor_produccion = calcular_menor_produccion_fabrica(matriz_produccion)
    print("\nMenor Producción por Fábrica:")
    for i, menor in enumerate(menor_produccion):
        print(f"Fábrica {i+1}: {menor}")
