def capicua(cadena: str) -> bool:
    ini = 0
    fin = len(cadena) -1 
    while ini < fin:
        if cadena[ini] != cadena[fin]:
            return False
        ini += 1
        fin -= 1
    return True 

def main() -> None:
    cadena = input("Ingresa una cadena: ")
    result = { 'es capicua': capicua(cadena)}

    impr_resultado = lambda resultado: print("la cadena otorgada es capicua" if resultado else "la cadena no es capicua")
    impr_resultado(result['es capicua'])

if __name__ == "__main__":
    main()