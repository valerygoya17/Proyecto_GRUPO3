from Material import Material
class Revista:
    def __init__(self, revista_id, tipo, contador_revista):
        self.id = revista_id
        self.tipo = tipo
        self.contador_revista = contador_revista
        self.disponible = True

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, new_tipo):
        self.tipo = new_tipo

    def get_contador_revista(self):
        return self.contador_revista

    def set_contador_revista(self, new_contador_revista):
        self.contador_revista = new_contador_revista

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible


revista1 = Revista(1, "Revista A", 10)
print(revista1.get_id())
print(revista1.get_tipo())
print(revista1.get_contador_revista())

revista1.set_id(2)
revista1.set_tipo("Revista B")
revista1.set_contador_revista(5)

print(revista1.get_id())  # Output: 2
print(revista1.get_tipo())  # Output: Revista B
print(revista1.get_contador_revista())  # Output: 5

revista1.actualizar_disponibilidad(False)
print(revista1.disponible)  # Output: False

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')