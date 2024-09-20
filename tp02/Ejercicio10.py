import random

def generar_lista():
    return [random.randint(1, 100) for _ in range(20)]

def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

def main():

    lista_original = generar_lista()
    print("Lista original:")
    print(lista_original)

    lista_impares = filtrar_impares(lista_original)
    print("\nLista de números impares:")
    print(lista_impares)

if __name__ == "__main__":
    main()