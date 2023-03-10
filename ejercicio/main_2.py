import random
from classes import Cliente, DetalleVenta, Producto, Vendedor
from presentacion import continuar, editar_cliente, imprimir_ventas, menu_principal, menu_clientes, listar_clientes
from presentacion import encontrar_cliente
from datos_clase import Datos

datos = Datos()
datos.recuperar_datos()

opcion = 9
while opcion > 0:
  opcion = menu_principal()
  if opcion == 1:
    opc_cliente = 9
    while opc_cliente > 0:
      opc_cliente = menu_clientes()
      if opc_cliente == 1:
        cliente = editar_cliente("Agregar", None)
        datos.add_cliente(cliente)
        datos.guardar_clientes()
        print("Cliente agregado correctamente")
        continuar()
      elif opc_cliente == 2:
        cliente = encontrar_cliente(datos.clientes)
        if cliente is not None:
          datos.del_cliente(cliente)
          datos.guardar_clientes()
          print("Cliente eliminado correctamente")
          continuar()
      elif opc_cliente == 3:
        cliente = encontrar_cliente(datos.clientes)
        if cliente is not None:
          original_cliente = cliente
          cliente = editar_cliente("Editar", original_cliente)
          datos.update_cliente(cliente, original_cliente)
          datos.guardar_clientes()
          print("Cliente actualizado correctamente")
          continuar()
      elif opc_cliente == 4:
        listar_clientes(datos.clientes)
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
  elif opcion == 5:
    imprimir_ventas(datos.ventas)