def eliminar_subcadena_slice(c, inicio, longitud):
    return c[:inicio] + c[(inicio+longitud):]

def eliminar_subcadena(c, inicio, longitud):
    salida = ''
    for i in range(len(c)):
        if i < inicio or i >= (inicio + longitud):
            salida += c[i]
    return salida

def main():
    cadena = "El número de teléfono es 4356-7890"
    inicio = 25
    longitud = 9
    print("Eliminar subcadena que comienza en la posición", inicio, "y tiene", longitud, "caracteres")
    print("Caso a (utilizando rebanadas):", eliminar_subcadena_slice(cadena, inicio, longitud))
    print("Caso b (sin utilizar rebanadas):", eliminar_subcadena(cadena, inicio, longitud))

if __name__ == "__main__":
    main()