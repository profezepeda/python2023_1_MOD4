

class Persona():
  rut: str
  nombre: str
  apellido: str
  edad: int

  def __init__(self, rut, nombre, apellido, edad):
    self.rut = rut
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    # self.caminar()

  def caminar(self):
    print("Estoy caminando a 6km/h")
    pass

class Superheroe(Persona):
  poder: str

  def __init__(self, rut, nombre, apellido, edad, poder):
    super().__init__(rut, nombre, apellido, edad)
    self.poder = poder

  def caminar(self):
    print("Estoy volando a 100km/h")


class Hiperheroe(Superheroe):
  poder2: str

  def __init__(self, rut, nombre, apellido, edad, poder, poder2):
    super().__init__(rut, nombre, apellido, edad, poder)
    self.poder2 = poder2

  def caminar(self):
    print("Estoy volando a 1000km/h")


class Monitor():
  tamano: float
  marca: str
  modelo: str
  encendido: bool = False

  def __init__(self, tamano, marca, modelo):
    self.tamano = tamano
    self.marca = marca
    self.modelo = modelo

  def encender(self):
    if self.encendido == False:
      print("Encendiendo monitor ...")
      self.encendido = True
    else:
      print("Monitor ya se encuentra encendido")

  def apagar(self):
    if self.encendido == True:
      print("Apagando monitor ... ")
      self.encendido = False
    else:
      print("Monitor ya se encuentra apagado")

class CPU():
  procesador: str
  ram: int
  disco_duro: int
  encendido: bool = False

  def __init__(self, procesador, ram, disco_duro):
    self.procesador = procesador
    self.ram = ram
    self.disco_duro = disco_duro

  def encender(self):
    if not self.encendido:
      print("Encendiendo CPU ...")
      self.encendido = True
    else:
      print("CPU ya se encuentra encendida")

  def apagar(self):
    if self.encendido:
      print("Apagando CPU ...")
      self.encendido = False
    else:
      print("CPU ya se encuentra apagada!")

class Computador():
  monitor: Monitor
  cpu: CPU

  def __init__(self, monitor, cpu):
    self.monitor = monitor
    self.cpu = cpu

  def encender(self):
    self.monitor.encender()
    self.cpu.encender()

  def apagar(self):
    self.monitor.apagar()
    self.cpu.apagar()




class Automovil():
  ruedas: int
  color: str
  marca: str
  modelo: str
  encendido: bool = False
  motor_cc: int

class AutoCombustion(Automovil):
  combustible: str
  caja_cambios: str

class AutoElectrico(Automovil):
  bateria: int
  carga_bateria: int