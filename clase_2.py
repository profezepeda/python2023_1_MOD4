class Persona():
    rut: str
    nombre: str
    apellido: str
    velocidad: int
    hobbies: list = []
    informacion_personal = {}

    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre
        self.a´pellido = apellido

    def caminar(self, **kwargs):
        if not 'velocidad' in kwargs:
            print("No ha indicado velocidad")
            return
        print("La persona camina a una velocidad de: ", kwargs['velocidad'])

    def definir_hobbies(self, *hobbies):
        self.hobbies = hobbies

    def asignar_informacion_personal(self, **kwargs):
        self.informacion_personal = kwargs

    def calculos_salud(self, **kwargs):
        if 'altura' in kwargs:
            if kwargs['altura'] > 1.80:
                print("La persona es alta")
            else:
                print("La persona es baja")
        if 'altura' in kwargs and 'peso' in kwargs:
            imc = kwargs['peso'] / (kwargs['altura'] ** 2)
            print("El IMC es: ", imc)

persona = Persona('1.9', 'Juan', 'Perez')
persona.definir_hobbies("modelismo", "lectura", "programación")
persona.asignar_informacion_personal(
    edad = 20,
    estatura = 1.80,
    peso = 80,
    color_ojos = "azules"
)

persona.caminar()
print(persona.hobbies)
print(persona.informacion_personal)

persona.calculos_salud(peso = 80, altura = 1.80)