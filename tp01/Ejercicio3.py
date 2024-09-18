def calcular_gasto_subte(viajes):
  
  gasto = 0
  if viajes <= 20:
    precio_pasaje = float(input("Ingrese el precio del pasaje: "))
    gasto = viajes * precio_pasaje
  elif viajes <= 30:
    precio_pasaje = float(input("Ingrese el precio del pasaje: "))
    gasto = viajes * precio_pasaje * 0.8  
  elif viajes <= 40:
    precio_pasaje = float(input("Ingrese el precio del pasaje: "))
    gasto = viajes * precio_pasaje * 0.7  
  else:
    precio_pasaje = float(input("Ingrese el precio del pasaje: "))
    gasto = viajes * precio_pasaje * 0.6  

  return gasto


def main():
  """Programa para verificar el comportamiento de la función."""

  while True:
    try:
      cantidad_viajes = int(input("Ingrese la cantidad de viajes: "))
      break
    except ValueError:
      print("Por favor, ingrese un número entero.")

  gasto_total = calcular_gasto_subte(cantidad_viajes)

  print(f"El gasto total en viajes es: {gasto_total}")

if __name__ == "__main__":
  main()