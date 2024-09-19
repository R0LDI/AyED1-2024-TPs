def concatenar(a: int, b: int) -> int:
    b_copia = b
    num_digitos = 0

    while b_copia > 0:
        b_copia //= 10
        num_digitos += 1

    a_copia = a * (10 ** num_digitos)
    a_copia += b
    return a_copia

def main():
    print(concatenar(1234, 567))

if __name__ == "__main__":
    main()

""" 
def concatenar(a: int, b: int) -> int:
    a_copia = a
    while b > 0:
        x = b % 10
        b //= 10
        a_copia = a_copia * 10 + x 
    
    return a_copia

def main():
    print(concatenar(1234, 567))

if __name__ == "__main__":
    main() """