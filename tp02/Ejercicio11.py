from typing import List

def cargar_pacientes() -> List[dict]:
    pacientes = []
    while True:
        numero_afiliado = int(input('Ingresa el número de afiliado (-1 para salir) > '))
        if numero_afiliado == -1:
            break
        tipo_atencion = int(input('Ingresa el tipo de atención (0: Urgencias, 1: Turnos) > '))
        pacientes.append({'numero_afiliado': numero_afiliado, 'tipo_atencion': tipo_atencion})
    return pacientes

def mostrar_pacientes(pacientes: List[dict]) -> None:
    print('Socios atendidos por emergencias:')
    for paciente in pacientes:
        if paciente['tipo_atencion'] == 0:
            print(paciente['numero_afiliado'])
    print('\nSocios atendidos por turno:')
    for paciente in pacientes:
        if paciente['tipo_atencion'] == 1:
            print(paciente['numero_afiliado'])

def buscar_paciente(pacientes: List[dict]) -> None:
    while True:
        numero_afiliado = int(input('Ingrese el número de afiliado (-1 para salir): '))
        if numero_afiliado == -1:
            break
        urgencia_count = 0
        turno_count = 0
        for paciente in pacientes:
            if paciente['numero_afiliado'] == numero_afiliado:
                if paciente['tipo_atencion'] == 0:
                    urgencia_count += 1
                else:
                    turno_count += 1
        if urgencia_count > 0:
            print(f'fue atendido {urgencia_count} veces por urgencias')
        if turno_count > 0:
            print(f'fue atendido {turno_count} veces con turnos')
        if urgencia_count == 0 and turno_count == 0:
            print('no fue nunca atendido')

def main() -> None:
    pacientes = cargar_pacientes()
    mostrar_pacientes(pacientes)
    buscar_paciente(pacientes)

if __name__ == '__main__':
    main()