import random as rn

def genera() -> list[int]:
    lista = []
    for i in range(50):
        lista.append(rn.randint(1, 100))
    return lista

def repetidos(lista: list[int]) -> bool:
    return len(set(lista)) != len(lista)

def unica(lista: list[int]) -> list[int]:
    return lista(set(lista))

if __name__ == '__main__':
    lista1 = genera()
    print(len(lista1))
    print(repetidos(lista1))
    lista2 = unica(lista1)
    print(f'{len(lista2)}\n{lista2}')

    