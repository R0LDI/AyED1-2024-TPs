
def subcadena_slice(c, inicio, longitud):
    return c[inicio:(inicio+longitud)]


def subcadena(c, inicio, longitud):
    salida = ''
    for i in range(longitud):
        salida += c[inicio+i]
    return salida


def main():
    cadena = "El número de teléfono es 4356-7890"
    inicio = 25
    longitud = 9
    print("Extraer subcadena que comienza en la posición", inicio, "y tiene", longitud, "caracteres")
    print("Caso a (utilizando rebanadas):", subcadena_slice(cadena, inicio, longitud))
    print("Caso b (sin utilizar rebanadas):", subcadena(cadena, inicio, longitud))

if __name__ == "__main__":
    main()
    