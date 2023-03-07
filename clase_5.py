class Persona():
  lista = []
  
  def agregar(self, nombre):
    if not isinstance(nombre, str):
      raise TypeError("Sólo utilizar strings")
    self.lista.append(nombre)

personas: Persona = Persona()
try:
  personas.agregar("Juan")
  personas.agregar("123")
except TypeError:
  print("Sólo ingresar nombres en string")
finally:
  print("Esto se ejecutará siempre")

print(personas.lista)



print()
print("==========")
print()

try:
  valor = "hola " + 90.5
  numero = 15 / 0
  print(numero)
# except (ZeroDivisionError, TypeError):
#   print("Erro inesperado")
except ZeroDivisionError:
  print("División por cero")
except TypeError:
  print("Tipo de datos")

class calculoValido(Exception):
  def __init__(self, saldo, monto):
    if saldo < monto:
      super().__init__("No hay saldo suficiente")
    self.saldo = saldo
    self.monto = monto

  def diferencia(self):
    return self.monto - self.saldo
  
try:
  raise calculoValido(500, 550);
except calculoValido as e:
  print("Lo siento, no puede girar este monto")


print()
print("==========")
print()


class Persona():
  _nombre: str
  _apellido: str

  def __init__(self, nombre, apellido):
    self._nombre = nombre
    self._apellido = apellido

  def __str__(self):
    return self._nombre + " " + self._apellido

  def set_nombre(self, nombre):
    self._nombre = nombre
  def get_nombre(self):
    return self._nombre.upper()
  def set_apellido(self, apellido):
    self._apellido = apellido
  def get_apellido(self):
    return self._apellido.upper()

persona = Persona("Juan", "Perez")
persona.set_nombre("Pedro")
persona.set_apellido("Gomez")

print(persona.get_nombre() + " " + persona.get_apellido())