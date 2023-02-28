class Usuario():
  id: int
  nombre: str
  apellido: str
  perfil: str

  # def __init__(self, id, nombre, apellido, perfil):
  #   self.id = id
  #   self.nombre = nombre
  #   self.apellido = apellido
  #   self.perfil = perfil

  def __str__(self):
    return f"{self.nombre} {self.apellido}"

  def guardar(self):
    print("Guardando usuario ...")
    # accion guardar
    pass


class Interfaces():

  def formulario_datos() -> Usuario:
    usuario: Usuario = Usuario()
    # datos = { "id": None, "nombre": None, "apellido": None, "perfil": None}
    usuario.id = input("Ingrese id: ")
    usuario.nombre = input("Ingrese nombre: ")
    usuario.apellido = input("Ingrese apellido: ")
    usuario.perfil = input("Ingrese perfil: ")
    return usuario



# usuario = Usuario(1, "Juan", "Perez", 20)
usuario = Interfaces.formulario_datos()
usuario.guardar()
print(usuario)