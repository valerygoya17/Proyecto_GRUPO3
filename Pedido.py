from Estudiante import Estudiante
from Persona import Persona
from Material import Material
from Docente import Docente
from Revista import Revista
class Pedido:
    contador_pedido = 0

    def __init__(self, id_pedido, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion):
        self.id = id_pedido
        self.solicitante = solicitante
        self.lista_material = lista_material
        self.materia = materia
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        Pedido.contador_pedido += 1

    def obtener_id(self):
        return self.id

    def obtener_solicitante(self):
        return self.solicitante

    def obtener_lista_material(self):
        return self.lista_material

    def obtener_materia(self):
        return self.materia

    def obtener_fecha_prestamo(self):
        return self.fecha_prestamo

    def obtener_fecha_devolucion(self):
        return self.fecha_devolucion

    def modificar_solicitante(self, solicitante):
        self.solicitante = solicitante

    def modificar_lista_material(self, lista_material):
        self.lista_material = lista_material

    def modificar_materia(self, materia):
        self.materia = materia

    def modificar_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def modificar_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion

    @staticmethod
    def pedir_material(lista_material, solicitante, materia):
        fecha_prestamo = date.today()
        fecha_devolucion = fecha_prestamo  # Puedes ajustar la lógica de la fecha de devolución según tus necesidades
        pedido = Pedido(Pedido.contador_pedido + 1, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion)
        return pedido

    def devolver_material(self):
        # Lógica para devolver el material
        pass


# Demostración de ejecución de todas las clases
docente = Docente ("987654321", "Carolina", "Nuñez", "carolan@gmail.com", "0919255935", "Norte", "Ciencias")
estudiante = Estudiante("JaneSmith")

print("=== Información de la Persona ===")
print("Nombre:", docente.obtener_nombre())
print()

print("=== Información de la Persona ===")
print("Nombre:", 'obtener_nombre')
print()

libro = Material("L001", "John Doe", "Python Programming", 2022, "Tech Books", True, 5)
revista = Revista("R001", "Jane Smith", "Science Weekly")





