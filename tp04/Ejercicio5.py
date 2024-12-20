
def filtrar_palabras_a(c, n):
    lista = c.split(' ')
    salida = []
    for palabra in lista:
        if len(palabra) >= n:
            salida.append(palabra)
    return ' '.join(salida)


def filtrar_palabras_b(c, n):
    lista = c.split(' ')
    salida = [palabra for palabra in lista if len(palabra) >= n]
    return ' '.join(salida)

def filtrar_palabras_c(c, n):
    salida = filter(lambda x: (len(x) >= n), c.split(' '))
    return ' '.join(salida)

def main():
    cadena = 'Para imprimir más largo y aún mucho más'
    n = 5
    print("Filtrar palabras con longitud mayor o igual a", n)
    print("Caso a (ciclos normales):", filtrar_palabras_a(cadena, n))
    print("Caso b (listas por comprensión):", filtrar_palabras_b(cadena, n))
    print("Caso c (función filter):", filtrar_palabras_c(cadena, n))
    assert filtrar_palabras_c('Para imprimir más largo y aún mucho más', 5) == 'imprimir largo mucho'

if __name__ == "__main__":
    main()