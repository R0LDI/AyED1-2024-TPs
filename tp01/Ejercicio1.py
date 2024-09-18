def numentero(a,b,c):
    valores = [a,b,c]
    val_max = max(valores)
    count = valores.count(val_max)
    #val_max = max(a,b,c)
    #count = 0

    if count == 1:
        return val_max
    else:
        return -1
    """if a == val_max:
        count += 1
    elif b == val_max:
        count += 1
    elif c == val_max:
        count += 1

    elif count == 1:
        return val_max
    else:
        return -1"""
    


def main():
    print("Ingresa tres numeros enteros positivos: ")
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    c = int(input("Numero 3: "))

    resultado = numentero(a,b,c)

    if resultado == -1:
        print("no hay un maximo unico")
    else:
        print("el maximo unico es:", resultado)

if __name__ == "__main__":
    main()