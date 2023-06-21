from Persona import Persona
class Estudiante:
    contador_estudiante = 0

    def __init__(self, nivel):
        self.id = Estudiante.contador_estudiante + 1
        self.nivel = nivel
        Estudiante.contador_estudiante += 1

    def obtener_id(self):
        return self.id

    def obtener_nivel(self):
        return self.nivel

    def modificar_nivel(self, nivel):
        self.nivel = nivel

    def pedir_libro(self):
        # Lógica para solicitar un libro
        pass

    def devolver_libro(self):
        # Lógica para devolver un libro
        pass

    def obtener_nombre(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def get_contador_estudiante(cls):
        return cls.contador_estudiante


estudiante = ("123456789","Medicina")

print("Nombre:", 'obtener_nombre')
print()

'devolver_libro'

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')