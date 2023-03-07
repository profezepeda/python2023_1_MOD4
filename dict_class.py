
from classes.classDB import Datos


datos = Datos()
personas = datos.listarPersonas()

datos.personas[0].name = "Juan"

datos.guardar()

for persona in datos.personas:
  print(persona.name, persona.age, persona.city)