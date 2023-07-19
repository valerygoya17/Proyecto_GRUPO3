from PySide6.QtWidgets import QMainWindow

from IU.untitled import Ui_vt_principal


class Persona_principal(QMainWindow):

    def __int__(self):
        super(Persona_principal, self).__init__()
        self.iu = Ui_vt_principal()
        self.iu.setupUi(self)