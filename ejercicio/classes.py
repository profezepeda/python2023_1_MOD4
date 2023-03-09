from random import randint


class Persona():
  rut: str
  nombre: str
  apellido: str

  def __init__(self, rut, nombre, apellido):
    self.rut = rut
    self.nombre = nombre
    self.apellido = apellido

class Cliente(Persona):
  _saldo: int

  def __init__(self, **kwargs):
    if 'rut' in kwargs:
      self.rut = kwargs['rut']
    if 'nombre' in kwargs:
      self.nombre = kwargs['nombre']
    if 'apellido' in kwargs:
      self.apellido = kwargs['apellido']
    # super().__init__(rut, nombre, apellido)
    self._saldo = randint(100000, 300000)

  def __str__(self):
    return f'{self.nombre} {self.apellido} {self.rut} -- Saldo: {self._saldo}'

  def consumir_saldo(self, monto):
    self._saldo -= monto

  def get_saldo(self):
    return self._saldo

  def buscar(self, rut, clientes):
    for cliente in clientes:
      if cliente.rut == rut:
        return cliente
    return None

class Vendedor(Persona):
  _comision: int
  _valor_comision: float = 0.005

  def __init__(self, rut, nombre, apellido):
    super().__init__(rut, nombre, apellido)
    self._comision = 0

  def __str__(self):
    return f'{self.nombre} {self.apellido} {self.rut} -- Comision: {self.get_comision()}'

  def set_comision(self, comision):
    self._comision = comision

  def get_comision(self):
    return self._comision
  
  def add_comision(self, valor):
    self._comision += valor * self._valor_comision

  def vender(self, detalle) -> dict:
    if detalle.cantidad > detalle.producto.stock:
      return {
        'resultado': False,
        'mensaje': 'Stock insuficiente'
      }
    if (detalle.unitario * detalle.cantidad) > detalle.cliente.get_saldo():
      return {
        'resultado': False,
        'mensaje': 'Saldo insuficiente'
      }
    detalle.cliente.consumir_saldo(detalle.unitario * detalle.cantidad)
    detalle.vendedor.add_comision(detalle.unitario * detalle.cantidad)
    return {
      'resultado': True,
      'mensaje': 'Venta realizada'
    }

class Producto():
  sku: str
  nombre: str
  stock: int
  precio: int

  def __init__(self, sku, nombre, stock, precio):
    self.sku = sku
    self.nombre = nombre
    self.stock = stock
    self.precio = precio

  def __str__(self):
    return f'{self.sku} {self.nombre} {self.precio} -- {self.stock}'

class DetalleVenta():
  cliente: Cliente
  vendedor: Vendedor
  producto: Producto
  cantidad: int
  unitario: int
  comision: int

  def __init__(self, cliente, vendedor, producto, cantidad, unitario):
    self.cliente = cliente
    self.vendedor = vendedor
    self.producto = producto
    self.cantidad = cantidad
    self.unitario = unitario

  def __str__(self):
    return f'{self.cliente.nombre} {self.vendedor.nombre} {self.producto.nombre} {self.cantidad} {self.unitario}'
