class Material:
    def __init__(self, codigo, autor, titulo, año, editorial, disponible, cantidad_disponible):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.año = año
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible

    def obtener_tipo(self):
        pass

    def __str__(self):
        return f"Código: {self.codigo}\n" \
               f"Autor: {self.autor}\n" \
               f"Título: {self.titulo}\n" \
               f"Año: {self.año}\n" \
               f"Editorial: {self.editorial}\n" \
               f"Disponible: {self.disponible}\n" \
               f"Cantidad Disponible: {self.cantidad_disponible}"


class Libro(Material):
    def obtener_tipo(self):
        return "Libro"


class Revista(Material):
    def obtener_tipo(self):
        return "Revista"


class Periodico(Material):
    def obtener_tipo(self):
        return "Periódico"


# Demostración de ejecución de todas las clases
libro = Libro("L001", "John Doe", "Python Programming", 2022, "Tech Books", True, 5)
revista = Revista("R001", "Jane Smith", "Science Weekly", 2023, "Scientific Publishing", False, 0)
periodico = Periodico("P001", "David Johnson", "Daily News", 2023, "Media Corp", True, 10)

print("=== Información del Libro ===")
print(libro)
print("Tipo:", libro.obtener_tipo())
print()

print("=== Información de la Revista ===")
print(revista)
print("Tipo:", revista.obtener_tipo())
print()

print("=== Información del Periódico ===")
print(periodico)
print("Tipo:", periodico.obtener_tipo())

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')