from datos.conexion import Conexion
from dominio.Estudiante import Estudiante


class EstudianteDao:
    _INSERTAR = "INSERT INTO Estudiantes (cedula,nombre,apellido,email,carrera,activo) VALUES ('0955824530','Ares','Hidalgo','ARESHIDALGO@GMAIL.COM','GIG',1)"

    @classmethod
    def insertar_estudiante(cls,estudiante):

        #cursor=Conexion.obtenerCursor()
        try:
            with Conexion.obtenerCursor()as cursor:
                datos = (estudiante.nombre, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera, estudiante.activo)

            cursor.execute(cls._INSERTAR, datos)
        except IntegrityError as e:
            print('la cedula que intenta ingresar ya existe')
            print(e)
        except ProgrammingError as e:
            print('los datos ingresados no son del tamaño permitido ')
        except Exception as e:
            print(e)

if __name__=='__main__':
    e1 = Estudiante()
    e1.cedula = '0214586321'
    e1.nombre = 'APOLO'
    e1.apellido = 'Cruz'
    e1.email = 'apoloruz@gmail.com'
    e1.carrera = 'admi'
    e1.activo = True
    EstudianteDao.insertar_estudiante(e1)
