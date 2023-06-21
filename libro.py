from Material import Material
class Libro:
    def __init__(self, id, tipo_pasta):
        self._id = id
        self._tipo_pasta = tipo_pasta
        self._contador_libro = 0
        self._disponible = True

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_tipo_pasta(self):
        return self._tipo_pasta

    def set_tipo_pasta(self, new_tipo_pasta):
        self._tipo_pasta = new_tipo_pasta

    def get_contador_libro(self):
        return self._contador_libro

    def set_contador_libro(self, new_contador_libro):
        self._contador_libro = new_contador_libro

    def actualizar_disponibilidad(self, disponible):
        self._disponible = disponible

# Crear objetos de tipo libro
libro1 = Libro(1, "Tapa dura")
libro2 = Libro(2, "Tapa blanda")

# Modificar atributos
libro1.set_id(3)
libro1.set_tipo_pasta("Tapa flexible")
libro1.set_contador_libro(5)
libro1.actualizar_disponibilidad(False)

# Obtener atributos
print(libro1.get_id())  # Output: 3
print(libro1.get_tipo_pasta())  # Output: Tapa flexible
print(libro1.get_contador_libro())  # Output: 5
print(libro1._disponible)  # Output: False

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')