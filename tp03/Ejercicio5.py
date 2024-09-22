import os
import random
from typing import List, Tuple

def mostrar_butacas(sala: List[List[str]]) -> None:
 
    print("  ", end="")
    for i in range(len(sala[0])):
        print(i+1, end=" ")
    print()
    print("---------------------")
    for i, fila in enumerate(sala):
        print(i+1, end=" |")
        for butaca in fila:
            print("X" if butaca == 'X' else "-", end=" ")
        print("|")
    print("---------------------")

def reservar(sala: List[List[str]], fila: int, butaca: int) -> bool:

    if sala[fila-1][butaca-1] == 'L':
        sala[fila-1][butaca-1] = 'X'
        return True
    return False

def cargar_sala(n_filas: int, m_butacas: int) -> List[List[str]]:

    sala = [['L' if random.random() < 0.5 else 'X' for _ in range(m_butacas)] for _ in range(n_filas)]
    return sala

def butacas_libres(sala: List[List[str]]) -> int:

    return sum(1 for fila in sala for butaca in fila if butaca == 'L')

def butacas_contiguas(sala: List[List[str]]) -> Tuple[int, int]:

    max_contiguas = 0
    coordenadas_inicio = (0, 0)
    for i, fila in enumerate(sala):
        contiguas = 0
        for j, butaca in enumerate(fila):
            if butaca == 'L':
                contiguas += 1
                if contiguas > max_contiguas:
                    max_contiguas = contiguas
                    coordenadas_inicio = (i+1, j+1-contiguas+1)
            else:
                contiguas = 0
    return coordenadas_inicio

def main():
    n_filas = 5
    m_butacas = 10
    sala = cargar_sala(n_filas, m_butacas)

    while True:
        print("Menu:")
        print("1. Hacer reservas")
        print("2. Cantidad butacas libres")
        print("3. Butacas contiguas")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_butacas(sala)
            fila_reserva = int(input("Ingrese la fila de la butaca a reservar: "))
            butaca_reserva = int(input("Ingrese la butaca a reservar: "))
            if reservar(sala, fila_reserva, butaca_reserva):
                print(f"Reserva exitosa en fila {fila_reserva}, butaca {butaca_reserva}")
            else:
                print(f"No se pudo reservar en fila {fila_reserva}, butaca {butaca_reserva}")
            mostrar_butacas(sala)
        elif opcion == "2":
            print(f"Butacas libres: {butacas_libres(sala)}")
        elif opcion == "3":
            print(f"Butacas contiguas: {butacas_contiguas(sala)}")
        elif opcion == "4":
            print(f"saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()