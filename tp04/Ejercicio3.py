def main():
    clave_maestra = int(input("Ingrese la clave maestra: "))
    clave_maestra_str = str(clave_maestra)
    clave_1 = "".join([clave_maestra_str[i] for i in range(0, len(clave_maestra_str), 2)])
    clave_2 = "".join([clave_maestra_str[i] for i in range(1, len(clave_maestra_str), 2)])
    print("Clave 1:", clave_1)
    print("Clave 2:", clave_2)

if __name__ == "__main__":
    main()