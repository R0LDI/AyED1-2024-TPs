"""def vuelto(total: int, recibido: int) -> list:
    if total > recibido:
        return -1
    # Crea una lista de 7 elementos en cero
    billetes = [0] * 7 # queda [0, 0, 0, 0, 0, 0, 0]
    # Calcula lo que debe devolver
    devolver = recibido - total
    for v in range(len(valores)):
        billetes[v] = devolver // valores[v]
        devolver %= valores[v]
    return billetes

valores = [500, 100, 50, 20, 10, 5, 1]
pago = 317
billete = 500
if pago > billete:
    print('No alcanza para hacer el pago')
else:
    salida = vuelto(pago, billete)
    # Uso de enumerate para las listas
    for i, s in enumerate(salida): # ver enumerate
        if s:
            print(f'{s} billetes de {valores[i]}')"""

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

# Ejemplo de uso
total_compra = 3170
dinero_recibido = 5000

vuelto = calcular_vuelto(total_compra, dinero_recibido)

if vuelto:
  print("Entregar el siguiente cambio:")
  for i, cantidad in enumerate(vuelto):
    if cantidad > 0:
      print(f"{cantidad} billete(s) de ${billetes[i]}")