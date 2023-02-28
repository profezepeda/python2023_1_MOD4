from classes.classes_cl1 import Persona, Monitor
from classes.classes_cl1 import CPU, Computador

juan:Persona = Persona("1-9", "Juan", "Perez", 20)
# juan.caminar()

monitor:Monitor = Monitor(15.6, "Samsung", "S24F350FHE")
cpu:CPU = CPU("Intel Core i5", 8, 500)

# print(monitor.marca, monitor.modelo)
# print(cpu.procesador, cpu.ram, cpu.disco_duro)

# print(monitor.encendido)
# monitor.encender()
# print(monitor.encendido)
# monitor.encender()
# print(monitor.encendido)
# monitor.apagar()
# print(monitor.encendido)

# print(cpu.encendido)
# cpu.encender()
# print(cpu.encendido)


computador:Computador = Computador(monitor, cpu)

print("Monitor: ", computador.monitor.modelo)
print("CPU: ", computador.cpu.procesador)
print(computador.monitor.encendido, computador.cpu.encendido)
computador.encender()
print(computador.monitor.encendido, computador.cpu.encendido)
computador.encender()
print(computador.monitor.encendido, computador.cpu.encendido)
computador.apagar()
print(computador.monitor.encendido, computador.cpu.encendido)
