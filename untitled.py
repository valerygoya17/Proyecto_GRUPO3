# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vt_principal(object):
    def setupUi(self, vt_principal):
        if not vt_principal.objectName():
            vt_principal.setObjectName(u"vt_principal")
        vt_principal.resize(414, 278)
        self.centralwidget = QWidget(vt_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_NOMBRE = QLineEdit(self.centralwidget)
        self.txt_NOMBRE.setObjectName(u"txt_NOMBRE")
        self.txt_NOMBRE.setGeometry(QRect(150, 70, 113, 20))
        self.txt_APELLIDO = QLineEdit(self.centralwidget)
        self.txt_APELLIDO.setObjectName(u"txt_APELLIDO")
        self.txt_APELLIDO.setGeometry(QRect(150, 100, 113, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 70, 47, 13))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 100, 47, 13))
        self.GRABAR = QPushButton(self.centralwidget)
        self.GRABAR.setObjectName(u"GRABAR")
        self.GRABAR.setGeometry(QRect(180, 150, 75, 23))
        vt_principal.setCentralWidget(self.centralwidget)
        self.mnb_menuprincipal = QMenuBar(vt_principal)
        self.mnb_menuprincipal.setObjectName(u"mnb_menuprincipal")
        self.mnb_menuprincipal.setGeometry(QRect(0, 0, 414, 21))
        vt_principal.setMenuBar(self.mnb_menuprincipal)
        self.stb_estado = QStatusBar(vt_principal)
        self.stb_estado.setObjectName(u"stb_estado")
        vt_principal.setStatusBar(self.stb_estado)

        self.retranslateUi(vt_principal)

        QMetaObject.connectSlotsByName(vt_principal)
    # setupUi

    def retranslateUi(self, vt_principal):
        vt_principal.setWindowTitle(QCoreApplication.translate("vt_principal", u"Ventana Principal", None))
        self.label.setText(QCoreApplication.translate("vt_principal", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("vt_principal", u"Apellido:", None))
        self.GRABAR.setText(QCoreApplication.translate("vt_principal", u"GRABAR", None))
    # retranslateUi

