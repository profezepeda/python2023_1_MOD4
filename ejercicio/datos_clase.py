
import json

from classes import Cliente


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

  def guardar_clientes(self):
    with open('clientes.json', 'w') as archivo:
      archivo.write(json.dumps(self.clientes, default=lambda o: o.__dict__, indent=4))
  
  def recuperar_clientes(self):
    with open('clientes.json', 'r') as archivo:
      self.clientes = json.loads(archivo.read(), object_hook=lambda d: Cliente(**d))