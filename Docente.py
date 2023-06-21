from Persona import Persona

class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, area):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion)
        self._area = area
        Docente.contador_docente += 1

    def pedir_libro(self):
        print("Docente pidiendo un libro...")

    def devolver_libro(self):
        print("Docente devolviendo un libro...")

    def obtener_nombre(self):
        return f"{self.nombre} {self.apellido}"

        def get_contador_docente(cls):
            return cls.contador_docente

docente = Docente("987654321", "Carolina", "Nuñez", "carolan@gmail.com", "0919255935", "Norte", "Ciencias")

print("Nombre:", docente.obtener_nombre())
print()

docente.devolver_libro()

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')