import self as self
from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow


from IU.untitled import Ui_TIPO
from datos.estudiante_dao import EstudianteDao
from dominio.Estudiante import Estudiante
from dominio.Docente import Docente

class Persona_principal(QMainWindow):

    def __init__(self):
        super(Persona_principal, self).__init__()
        self.iu = Ui_TIPO()
        self.iu.setupUi(self)
        self.iu.stb_estado.showMessage('Bienvenido', 2000)
        self.iu.stb_estado.showMessage("Saludos")
        self.iu.GRABAR.clicked.connect(self.GRABAR)

        self.iu.txt_cedula.setValidator(QtGui.QIntValidator())


        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.iu.txt_email.setValidator(validator)

    def GRABAR(self):
        tipo_persona = self.iu.cb_tipo_persona.currentText()
        if self.iu.txt_NOMBRE.text() == '' or self.iu.txt_APELLIDO.text() == '' \
                or len(self.iu.txt_cedula.text()) < 10 or self.iu.txt_email.text() == '':
            # Mostrar un mensaje de advertencia o mostrar un cuadro de diálogo
            pass
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.nombre = self.iu.txt_NOMBRE.text()
                persona.apellido = self.iu.txt_APELLIDO.text()
                persona.cedula = self.iu.txt_cedula.text()
                persona.email = self.iu.txt_email.text()
            else:
                persona = Estudiante()
                persona.nombre = self.iu.txt_NOMBRE.text()
                persona.apellido = self.iu.txt_APELLIDO.text()
                persona.cedula = self.iu.txt_cedula.text()
                persona.email = self.iu.txt_email.text()

                EstudianteDao.insertar_estudiante(persona)

            self.iu.txt_NOMBRE.setText('')
            self.iu.txt_APELLIDO.setText('')
            self.iu.txt_cedula.setText('')
            self.iu.txt_email.setText('')
            self.iu.stb_estado.showMessage('Grabado con éxito.', 2000)

            def buscar_x_cedula(self):
                cedula = self.ui.txt_cedula.text()
                e = Estudiante(cedula=cedula)
                e = EstudianteDao.seleccionar_por_cedula(e)
                print(e)
                self.ui.txt_nombre.setText(e.nombre)
                self.ui.txt_apellido.setText(e.apellido)
                self.ui.txt_correo.setText(e.correo)
                self.ui.cb_tipo_persona.setCurrentText('Estudiante')


