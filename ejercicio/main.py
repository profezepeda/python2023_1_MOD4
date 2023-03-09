import random
from classes import Cliente, DetalleVenta, Producto, Vendedor
from presentacion import imprimir_ventas
from datos_clase import Datos

datos = Datos()
# datos.add_cliente(Cliente(rut='1-9', nombre='Juan', apellido='Perez'))
# datos.add_cliente(Cliente(rut='2-9', nombre='Pedro', apellido='Gonzalez'))
# datos.add_cliente(Cliente(rut='3-9', nombre='Maria', apellido='Gonzalez'))
# datos.add_cliente(Cliente(rut='4-9', nombre='Jose', apellido='Perez'))
# datos.add_cliente(Cliente(rut='5-9', nombre='Luis', apellido='Gonzalez'))

datos.recuperar_clientes()

# cliente = Cliente().buscar('2-9', datos.clientes)
# if cliente is not None:
#   datos.del_cliente(cliente)

# datos.guardar_clientes()

datos.add_vendedor(Vendedor('1-9', 'Mario', 'Perez'))
datos.add_vendedor(Vendedor('2-9', 'Mauricio', 'Gonzalez'))
datos.add_vendedor(Vendedor('3-9', 'Josefina', 'Gonzalez'))
datos.add_vendedor(Vendedor('4-9', 'Antonia', 'Perez'))
datos.add_vendedor(Vendedor('5-9', 'Paz', 'Gonzalez'))

datos.add_producto(Producto('1', 'Producto 1', 20, 1000))
datos.add_producto(Producto('2', 'Producto 2', 15, 2000))
datos.add_producto(Producto('3', 'Producto 3', 18, 3000))
datos.add_producto(Producto('4', 'Producto 4', 80, 4000))
datos.add_producto(Producto('5', 'Producto 5', 30, 5000))

cliente = Cliente().buscar('2-9', datos.clientes)
print(cliente)

# cliente, vendedor, producto, cantidad, unitario
ventas = []

for item in range(0, 5):
  idx_cliente = random.randint(0, 4)
  idx_vendedor = random.randint(0, 4)
  idx_producto = random.randint(0, 4)
  rnd_cantidad = random.randint(1, 10)
  venta = DetalleVenta(
    datos.clientes[idx_cliente],
    datos.vendedores[idx_vendedor],
    datos.productos[idx_producto],
    2,
    datos.productos[idx_producto].precio)
  resultado = datos.vendedores[item].vender(venta)
  if resultado['resultado']:
    ventas.append(venta)
  print(resultado['mensaje'])


# venta = DetalleVenta(clientes[0], vendedores[0], productos[0], 2, productos[0].precio)
# resultado = vendedores[0].vender(venta)
# if resultado['resultado']:
#   ventas.append(venta)
# print(resultado['mensaje'])


imprimir_ventas(ventas)
