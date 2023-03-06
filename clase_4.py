class PersonalUniversitario():
    rut: str
    nombre: str
    apellido: str

    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Personal: {self.nombre} {self.apellido}"

    def hablar(self):
        print("Hola, soy el método Padre")

class Profesor(PersonalUniversitario):
    asignatura: str
    sueldo: int

    def __init__(self, rut, nombre, apellido, asignatura, sueldo):
        super().__init__(rut, nombre, apellido)
        self.asignatura = asignatura
        self.sueldo = sueldo

    # def __str__(self):
    #     return f"Profesor: {self.nombre} {self.apellido} - {self.asignatura}"

    def hablar(self):
        super().hablar()
        print("Hola, soy el profesor")

class Alumno(PersonalUniversitario):
    carrera: str
    semestre: int

    def __init__(self, rut, nombre, apellido, carrera, semestre):
        super().__init__(rut, nombre, apellido)
        self.carrera = carrera
        self.semestre = semestre

    # def __str__(self):
    #     return f"Alumno: {self.nombre} {self.apellido} - {self.carrera} - {self.semestre}"

class ProfesorAyudante(Profesor, Alumno):

    def __init__(self, rut, nombre, apellido, asignatura, sueldo, carrera, semestre):
      self.rut = rut
      self.nombre = nombre
      self.apellido = apellido
      self.asignatura = asignatura
      self.sueldo = sueldo
      self.carrera = carrera
      self.semestre = semestre

    def __str__(self):
        return f"Profesor Ayudante: {self.nombre} {self.apellido} - {self.asignatura} - {self.carrera} - {self.semestre}"


profesor: Profesor = Profesor("1-9", "Juan", "Perez", "Matematicas", 500000)
alumno: Alumno = Alumno("2-7", "María", "González", "Informática", 3)

print(profesor)
print(alumno)

ayudante = ProfesorAyudante("3-5", "Juanita", "Tapia", "Matemáticas", 50000, "Tecnologías", 3)
print(ayudante)


profesor.hablar()

print(isinstance(profesor, PersonalUniversitario))
print(alumno)