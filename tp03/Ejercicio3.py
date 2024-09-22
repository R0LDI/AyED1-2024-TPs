import random

def generar_numeros_aleatorios_unicos(n):
    números = set()
    while len(números) < n ** 2:
        números.add(random.randint(0, n ** 2 - 1))
    return list(números)

def llenar_matriz(n, números):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(números[i * n + j])
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    números = generar_numeros_aleatorios_unicos(n)
    matriz = llenar_matriz(n, números)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()