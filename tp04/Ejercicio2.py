def main():
    cadena = input("Ingrese una cadena: ")
    espacios = (80 - len(cadena)) // 2
    print(" " * espacios + cadena + " " * espacios)

if __name__ == "__main__":
    main()