def subcadena(c, n):
    return c[-n:]

def main():
    cadena = "El número de teléfono es 4356-7890"
    n = 9
    print("Últimos", n, "caracteres de la cadena:", subcadena(cadena, n))

if __name__ == "__main__":
    main()