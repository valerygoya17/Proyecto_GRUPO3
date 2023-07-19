import sys

from PySide6.QtWidgets import QApplication

from servicio.persona_principal import Persona_principal

app = QApplication()
untitled = Persona_principal()
untitled.show()
sys.exit(app.exec())