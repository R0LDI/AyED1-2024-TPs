def naipes():
    palos = ['Oros', 'Bastos', 'Espadas', 'Copas']
    return [' '.join([str(x), y]) for y in palos for x in range(1, 13)]

def main():
    lista_naipes = naipes()
    print("Lista de naipes de la baraja española:")
    for naipe in lista_naipes:
        print(naipe)

if __name__ == "__main__":
    main()