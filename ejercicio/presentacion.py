def imprimir_ventas(ventas):
  for venta in ventas:
    print(venta.cliente)
    print(venta.vendedor)
    print(venta.producto)
    print(venta.cantidad, venta.unitario, venta.cantidad * venta.unitario)
    print("---------------------------------------------")