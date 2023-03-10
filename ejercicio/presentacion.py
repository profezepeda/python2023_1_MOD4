import os

from classes import Cliente

def continuar():
  print("")
  input("Presione ENTER para continuar...")

def menu_principal():
  os.system("clear")
  print("MENÚ PRINCIPAL - SISTEMA DE VENTAS")
  print("1. Menú de clientes")
  print("2. Menú de vendedores")
  print("3. Menú de productos")
  print("4. Registrar venta")
  print("5. Listar ventas")
  print("0. Salir")
  while True:
    try:
      opcion = int(input("Ingrese una opción: "))
      if opcion >= 0 and opcion <= 5:
        break
      else:
        print("Ingrese una opción válida.")
    except:
      print("Ingrese una opción válida")
  return opcion

def menu_clientes():
  os.system("clear")
  print("MENÚ CLIENTES")
  print("1. Agregar cliente")
  print("2. Eliminar cliente")
  print("3. Modificar cliente")
  print("4. Listar clientes")
  print("0. Volver")
  while True:
    try:
      opcion = int(input("Ingrese una opción: "))
      if opcion >= 0 and opcion <= 4:
        break
      else:
        print("Ingrese una opción válida.")
    except:
      print("Ingrese una opción válida")
  return opcion

def imprimir_ventas(ventas):
  os.system("clear")
  print("=============================================")
  print("Listado de ventas")
  print("=============================================")
  for venta in ventas:
    print(venta.cliente)
    print(venta.vendedor)
    print(venta.producto)
    print(venta.cantidad, venta.unitario, venta.cantidad * venta.unitario)
    print("---------------------------------------------")
  print()
  print("=============================================")
  print()
  continuar()

def listar_clientes(clientes):
  os.system("clear")
  print("=============================================")
  print("Listado de clientes")
  print("=============================================")
  for cliente in clientes:
    print(cliente)
  print()
  print("=============================================")
  print()
  continuar()

def editar_cliente(accion: str, cliente: Cliente) -> Cliente:
  os.system("clear")
  print("=============================================")
  print(accion.upper(), "CLIENTE")
  print("=============================================")
  registro = { "rut": "", "nombre": "", "apellido": "" }
  if cliente is not None:
    registro["rut"] = cliente.rut
    registro["nombre"] = cliente.nombre
    registro["apellido"] = cliente.apellido
  rut = input("RUT [" + registro["rut"] + "]: ")
  nombre = input("Nombre [" + registro["nombre"] + "]: ")
  apellido = input("Apellido [" + registro["apellido"] + "]: ")
  if rut != "":
    registro["rut"] = rut
  if nombre != "":
    registro["nombre"] = nombre
  if apellido != "":
    registro["apellido"] = apellido
  return Cliente(rut=registro["rut"], nombre=registro["nombre"], apellido=registro["apellido"])

def encontrar_cliente(clientes):
  os.system("clear")
  print("=============================================")
  print("BUSCAR CLIENTE")
  print("=============================================")
  while True:
    condicion = input("Ingrese el RUT del cliente (vacío si quiere retornar): ")
    if condicion == "":
      return None
    else:
      cliente = Cliente().buscar(condicion, clientes)
      if cliente == None:
        print("Cliente no encontrado, inténtelo nuevamente.")
      else:
        return cliente