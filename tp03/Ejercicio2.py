from tabulate import tabulate

def genera_matriz(Num: int):
    matriz = [[0 for _ in range(Num)] for _ in range(Num)]
    for i in range(Num):
        for j in range(Num - i):
            matriz[i][j] = Num - i - j
    return matriz

def main():
    Num = int(input("Ingrese el tamaño de la matriz (N x N): "))
    print(tabulate(genera_matriz(Num)))

if __name__ == "__main__":
    main()