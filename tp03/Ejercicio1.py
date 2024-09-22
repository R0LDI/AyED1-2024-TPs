def cargar(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            num = int(input(f'Ingrese un número entero para la fila {i+1} y columna {j+1}: '))
            fila.append(num)
        matriz.append(fila)
    return matriz

def copiar(m):     
    matriz_nueva = []
    for fila in m:
        fila_nueva = []
        for elem in fila:
            fila_nueva.append(elem)
        matriz_nueva.append(fila_nueva)
    return matriz_nueva
# Copia la matriz, iba a usar la funcion .copy pero no me acordaba si se podia
"""return [fila.copy() for fila in m]"""

def ordenar_f(m):
    m1 = copiar(m)
    for i in range(len(m1)):
        m1[i].sort()
    return m1

def intercambiar_f(m, f1, f2):
    m[f1-1], m[f2-1] = m[f2-1], m[f1-1]
    return m

def intercambiar_c(m, c1, c2):
    """Intercambia dos columnas dadas como parámetro."""
    for i in range(len(m)):
        m[i][c1-1], m[i][c2-1] = m[i][c2-1], m[i][c1-1]
    return m

def transponer(m):
    """Transpone la matriz (intercambia filas x columnas)."""
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def promedio_f(m, f):
    """Calcula el promedio de los elementos de una fila."""
    return sum(m[f-1]) / len(m[f-1])

def porcentaje_impar(m, c):
    """Calcula el porcentaje de elementos impares en una columna."""
    largo = len(m)
    contador = 0
    for i in range(largo):
        if m[i][c-1] % 2 == 1:
            contador += 1
    return (contador / largo * 100)

def simetrica_p(m):

    for i in range(len(m)):
        for j in range(i, len(m)):
            if m[i][j] != m[j][i]:
                return False
    return True

def simetrica_s(m):
    for i in range(len(m)-1, -1, -1):
        for j in range(len(m)-1, -1, -1):
            if m[i][j] != m[j][i]:
                return False
    return True

def palindromo_col(m):
    palindromos = []
    for i in range(len(m[0])):
        capicua = True
        for j in range(len(m) // 2):
            if m[i][j] != m[i][len(m) - j - 1]:
                capicua = False
                break
        if capicua:
            palindromos.append(i)
    return palindromos

def imprimir_matriz(m):
    print('-'*16)
    for f in range(len(m)):
        print(f"",end='|')
        for c in range(len(m[f])):
            print(f"{m[f][c]:>2}",end='|')
        print()
    print('-'*16)
    print()

def main():
    n = int(input("Ingrese el tamaño de la matriz (N): "))
    matriz1 = cargar(n)
    print('Matriz original')
    imprimir_matriz(matriz1)

    imprimir_matriz(ordenar_f(copiar(matriz1)))
    imprimir_matriz(intercambiar_f(copiar(matriz1), 2, 3))
    imprimir_matriz(intercambiar_c(copiar(matriz1), 2, 3))
    imprimir_matriz(transponer(copiar(matriz1)))
    print(promedio_f(matriz1, 3))
    print(f'{porcentaje_impar(matriz1, 3)} %')
    if simetrica_p(matriz1):
        print(f'La matriz es simétrica por su diagonal principal')
    else:
        print(f'La matriz no es simétrica por su diagonal principal')
    if simetrica_s(matriz1):
        print(f'La matriz es simétrica por su diagonal secundaria')
    else:
        print

if __name__ == "__main__":
    main()