def romanos(numero):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    sim = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    numero_romano = ''
    i = 0
    while  numero > 0:
        for _ in range(numero // valores[i]):
            numero_romano += sim[i]
            numero -= valores[i]
        i += 1
    return numero_romano

def main():
    numero = int(input("Ingresa un número entero entre 0 y 3999: "))
    if 0 <= numero <= 3999:
        print(f"El número romano de {numero} es {romanos(numero)}")
    else:
        print("El número está fuera de los permitidos.")

if __name__ == "__main__":
    main()