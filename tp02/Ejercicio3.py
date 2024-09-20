def crea_cuadrado(n: int) -> list[int]:
    return [i**2 for i in range(1, n+1)]

while True:
    num = int(input('ingresa un numero mayor que 1: '))
    if num > 1:
        break

lista_cuadrados = crea_cuadrado(num)
print(lista_cuadrados[-10:] if len(lista_cuadrados) > 19 else lista_cuadrados)