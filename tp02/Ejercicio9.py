def multiplos(A, B):
    return [i for i in range(A, B+1) if i % 7 == 0 and i % 5 != 0]

def main():
    while True:
        try:
            A = int(input("Ingrese A: "))
            B = int(input("Ingrese B: "))
            if A > B:
                raise ValueError("A debe ser menor o igual que B")
            break
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese valores válidos.")

    lista_multiplos = multiplos(A, B)
    print("La lista de múltiplos de 7 que no son múltiplos de 5 entre A y B es:")
    print(lista_multiplos)

if __name__ == "__main__":
    main()