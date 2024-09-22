hotel = [[[{} for _ in range(6)] for _ in range(10)]]

def registrar_huesped(dni, nombre, checkin, checkout, ocupantes):
    for piso in hotel:
        for habitacion in piso:
            if habitacion and 'dni' in habitacion and habitacion['dni'] == dni:
                print("El DNI ya existe en el hotel")
                return

    if checkout <= checkin:
        print("La fecha de salida debe ser posterior a la fecha de entrada")
        return

    for piso in range(10):
        for habitacion in range(6):
            if not hotel[piso][habitacion]:  # habitación disponible
                hotel[piso][habitacion] = {
                    'dni': dni,
                    'nombre': nombre,
                    'checkin': checkin,
                    'checkout': checkout,
                    'ocupantes': ocupantes
                }
                return
    print("No hay habitaciones disponibles")

def mostrar_resultados():
    piso_mas_ocupado = max(range(10), key=lambda x: sum(1 for habitacion in hotel[x] if habitacion))
    print(f"Piso {piso_mas_ocupado+1} tiene la mayor cantidad de habitaciones ocupadas")

    habitaciones_vacias = sum(1 for piso in hotel for habitacion in piso if not habitacion)
    print(f"Hay {habitaciones_vacias} habitaciones vacías en el hotel")

    piso_mas_personas = max(range(10), key=lambda x: sum(habitacion['ocupantes'] for habitacion in hotel[x] if habitacion))
    print(f"Piso {piso_mas_personas+1} tiene la mayor cantidad de personas")

    fecha_actual = input("Ingrese fecha actual (DDMMYYYY): ")
    proximas_checkout = [(piso, habitacion) for piso, habitaciones in enumerate(hotel) for habitacion in habitaciones if habitacion and habitacion['checkout'] == fecha_actual]
    print("Próximas habitaciones en desocuparse:")
    for piso, habitacion in proximas_checkout:
        print(f"Piso {piso+1}, Habitación {hotel[piso].index(habitacion)+1}")

    huespedes = [(habitacion['nombre'], habitacion['dni']) for piso in hotel for habitacion in piso if habitacion]
    huespedes.sort(key=lambda x: x[0])
    print("Lista de huéspedes:")
    for huesped in huespedes:
        print(f"{huesped[0]} - {huesped[1]}")

def main():
    while True:
        while True:
            try:
                dni = int(input("Ingrese DNI (-1 para finalizar): "))
                if dni == -1:
                    break
                if len(str(dni)) != 8:
                    print("El DNI debe tener 8 dígitos")
                    continue
                break
            except ValueError:
                print("El DNI debe ser un número")

        if dni == -1:
            break

        while True:
            nombre = input("Ingrese Apellido y Nombre: ")
            if nombre:
                break
            print("El nombre no puede estar vacío")

        while True:
            checkin = input("Ingrese Fecha de ingreso (DDMMYYYY): ")
            if len(checkin) == 8 and checkin.isdigit():
                break
            print("La fecha de ingreso debe tener 8 dígitos")

        while True:
            checkout = input("Ingrese Fecha de egreso (DDMMYYYY): ")
            if len(checkout) == 8 and checkout.isdigit():
                break
            print("La fecha de egreso debe tener 8 dígitos")

        while True:
            try:
                ocupantes = int(input("Ingrese Cantidad de ocupantes: "))
                if ocupantes < 1:
                    print("La cantidad de ocupantes debe ser mayor que 0")
                    continue
                break
            except ValueError:
                print("La cantidad de ocupantes debe ser un número")

        registrar_huesped(dni, nombre, checkin, checkout, ocupantes)

    mostrar_resultados()

if __name__ == "__main__":
    main()