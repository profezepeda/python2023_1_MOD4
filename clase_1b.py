from classes.classes_cl1 import Monitor, CPU, Computador
from classes.classes_cl1 import Persona, Superheroe, Hiperheroe

computadores = [
    Computador(
      Monitor(27.2, "SONY", "SN001"),
      CPU("i5", 16, 500)
    )
]
computadores.append(
    Computador(
      monitor = Monitor(27.2, "Samsung", "SN001"),
      cpu = CPU("i7", 16, 500)
    )
)

for computador in computadores:
    print("COMPUTADOR")
    print(computador.cpu.procesador, computador.monitor.marca)


pantalla:Monitor = None
pantalla:Monitor = Monitor(27.2, "SONY", "SN001")


persona:Persona = Persona("1-9", "Juan", "Perez", 20)
print(persona.nombre, persona.apellido)

superman:Superheroe = Superheroe("1-9", "Clark", "Kent", 20, "Volar")
hiperheroe:Hiperheroe = Hiperheroe("1-9", "Profe", "Zepeda", 21, "Volar", "Teletransportarse")


print(superman.nombre, superman.apellido, superman.poder)
print(hiperheroe.nombre, hiperheroe.apellido, hiperheroe.poder, hiperheroe.poder2)


superman.apellido = "KENT"
print(superman.nombre, superman.apellido, superman.poder)
