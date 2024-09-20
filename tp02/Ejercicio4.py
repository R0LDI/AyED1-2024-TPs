def eliminar_valores(lista_original: list, lista_eliminar: list) -> None:

    for valor in lista_eliminar:
        while valor in lista_original:
            lista_original[lista_original.index(valor)] = None
            lista_original[:] = [x for x in lista_original if x is not None]

def main() -> None:
   
    lista_original = [int(x) for x in input("Ingrese la lista original (separada por espacios): ").split()]
    lista_eliminar = [int(x) for x in input("Ingrese la lista de valores a eliminar (separada por espacios): ").split()]
    
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar:", lista_eliminar)
    
    eliminar_valores(lista_original, lista_eliminar)
    
    print("Lista después de eliminar los valores:", lista_original)

if __name__ == "__main__":
    main()