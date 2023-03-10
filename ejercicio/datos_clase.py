
import json

from classes import Cliente, Producto, Vendedor, DetalleVenta

class Datos():
  vendedores = []
  productos = []
  clientes = []
  ventas = []

  def add_cliente(self, cliente):
    self.clientes.append(cliente)

  def add_vendedor(self, vendedor):
    self.vendedores.append(vendedor)

  def add_producto(self, producto):
    self.productos.append(producto)

  def del_cliente(self, cliente):
    self.clientes.remove(cliente)

  def del_vendedor(self, vendedor):
    self.vendedores.remove(vendedor)

  def del_producto(self, producto):
    self.productos.remove(producto)

  def update_cliente(self, cliente, original):
    self.clientes[self.clientes.index(original)] = cliente

  def guardar_clientes(self):
    with open('clientes.json', 'w') as archivo:
      archivo.write(json.dumps(self.clientes, default=lambda o: o.__dict__, indent=4))

  def recuperar_clientes(self):
    try:
      with open('clientes.json', 'r') as archivo:
        self.clientes = json.loads(archivo.read(), object_hook=lambda d: Cliente(**d))
    except:
      self.clientes = []

  def guardar_vendedores(self):
    with open('vendedores.json', 'w') as archivo:
      archivo.write(json.dumps(self.vendedores, default=lambda o: o.__dict__, indent=4))

  def recuperar_vendedores(self):
    try:
      with open('vendedores.json', 'r') as archivo:
        self.vendedores = json.loads(archivo.read(), object_hook=lambda d: Vendedor(**d))
    except:
      self.vendedores = []

  def guardar_productos(self):
    with open('productos.json', 'w') as archivo:
      archivo.write(json.dumps(self.productos, default=lambda o: o.__dict__, indent=4))

  def recuperar_productos(self):
    try:
      with open('productos.json', 'r') as archivo:
        self.productos = json.loads(archivo.read(), object_hook=lambda d: Producto(**d))
    except:
      self.productos = []

  def guardar_ventas(self):
    with open('ventas.json', 'w') as archivo:
      archivo.write(json.dumps(self.ventas, default=lambda o: o.__dict__, indent=4))

  def recuperar_ventas(self):
    try:
      with open('ventas.json', 'r') as archivo:
        self.ventas = json.loads(archivo.read(), object_hook=lambda d: DetalleVenta(**d))
    except:
      self.ventas = []

  def recuperar_datos(self):
    self.recuperar_clientes()
    self.recuperar_vendedores()
    self.recuperar_productos()
    self.recuperar_ventas()