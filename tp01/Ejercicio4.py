def calcular_vuelto(total_compra, recibido):
  """Calcula el cambio a entregar minimizando la cantidad de billetes.

  Argumentos:
    Total de compra.
    recibido: la plata recibida del cliente.

  Retorna una lista con la cantidad de billetes de cada denominación, o None 
    si no es posible dar el cambio o el dinero es insuficiente.
  """

  billetes = [5000, 1000, 500, 200, 100, 50, 10]
  cambio = recibido - total_compra

  if cambio < 0:
    print("Error: El monto recibido es insuficiente.")
    return None

  vuelto = [0] * len(billetes)

  for i, billete in enumerate(billetes):
    vuelto[i] = cambio // billete
    cambio %= billete

  if cambio != 0:
    print("Error: No es posible entregar el cambio debido a falta de billetes con denominaciones adecuadas.")
    return None

  return vuelto, billetes  


total_compra = 3170
dinero_recibido = 5000

vuelto, billetes = calcular_vuelto(total_compra, dinero_recibido)  # descomprime los valores devueltos x el programa

if vuelto:  # entrega de los billetes
  print("Entregar el siguiente cambio:")
  for i, cantidad in enumerate(vuelto):
    if cantidad > 0:
      print(f"{cantidad} billete(s) de ${billetes[i]}")  


