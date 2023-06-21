
class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = 0
        self.activo = True

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cedula: {self.cedula}"

    @property
    def pedir_libro(self):
        if self.activo:
            self.numero_libros += 1
            return True
        else:
            return False

    @property
    def devolver_libro(self):
        return self.numero_libros > 0
print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')
