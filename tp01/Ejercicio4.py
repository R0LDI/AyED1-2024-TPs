def calcular_vuelto(total_compra, dinero_recibido):
  """Calcula el cambio a entregar minimizando la cantidad de billetes.

  Args:
    total_compra: El total de la compra.
    dinero_recibido: El dinero recibido del cliente.

  Returns:
    Una lista con la cantidad de billetes de cada denominación, o None 
    si no es posible dar el cambio o el dinero es insuficiente.
  """

  billetes = [5000, 1000, 500, 200, 100, 50, 10]
  cambio = dinero_recibido - total_compra

  if cambio < 0:
    print("Error: El dinero recibido es insuficiente.")
    return None

  vuelto = [0] * len(billetes)

  for i, billete in enumerate(billetes):
    vuelto[i] = cambio // billete
    cambio %= billete

  if cambio != 0:
    print("Error: No es posible entregar el cambio exacto con los billetes disponibles.")
    return None

  return vuelto


total_compra = 3170
dinero_recibido = 5000

vuelto = calcular_vuelto(total_compra, dinero_recibido)

if vuelto:
  print("Entregar el siguiente cambio:")
  for i, cantidad in enumerate(vuelto):
    if cantidad > 0:
      print(f"{cantidad} billete(s) de ${billetes[i]}")
