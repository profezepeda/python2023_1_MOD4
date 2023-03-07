import json


class Persona():
  name: str
  age: int
  city: str

  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city



class Datos():
  personas: list[Persona] = []
  def __init__(self) -> None:
    # self.migrarDatos()
    pass

  def migrarDatos(self) -> None:
    registros = []
    with open('data.json', 'r') as filehandle:
      lista = json.load(filehandle)
    for elemento in lista:
      registros.append(Persona(elemento['name'], elemento['age'], elemento.get("city", "-")))
    with open('data.json', 'w') as filehandle:
      json.dump(registros, filehandle, indent=2, default=lambda o: o.__dict__)

  def listarPersonas(self) -> list[Persona]:
    with open('data.json', 'r') as filehandle:
      lista = json.load(filehandle)

    self.personas = []
    for elemento in lista:
      self.personas.append(Persona(elemento['name'], elemento['age'], elemento['city']))
    return self.personas
  
  def guardar(self) -> None:
    with open('data.json', 'w') as filehandle:
      json.dump(self.personas, filehandle, indent=2, default=lambda o: o.__dict__)