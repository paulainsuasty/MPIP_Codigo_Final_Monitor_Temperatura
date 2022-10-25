# -*- coding: utf-8 -*-

# MPIP
# DABM 2022 - 2
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_interfaz_principal(object):
    def setupUi(self, interfaz_principal):
        interfaz_principal.setObjectName("interfaz_principal")
        interfaz_principal.resize(815, 266)
        self.centralwidget = QtWidgets.QWidget(interfaz_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 100, 331, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 130, 731, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.captura_datos = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.a_captura_datos())
        self.captura_datos.setObjectName("captura_datos")
        self.horizontalLayout.addWidget(self.captura_datos)
        self.configuracion_parametros = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.a_configuracion_parametros())
        self.configuracion_parametros.setObjectName("configuracion_parametros")
        self.horizontalLayout.addWidget(self.configuracion_parametros)
        self.reportes = QtWidgets.QPushButton(self.horizontalLayoutWidget , clicked = lambda: self.a_reportes())
        self.reportes.setObjectName("reportes")
        self.horizontalLayout.addWidget(self.reportes)
        self.salir = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.a_cerrar())
        self.salir.setObjectName("salir")
        self.horizontalLayout.addWidget(self.salir)
        interfaz_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(interfaz_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        interfaz_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(interfaz_principal)
        self.statusbar.setObjectName("statusbar")
        interfaz_principal.setStatusBar(self.statusbar)

        self.retranslateUi(interfaz_principal)
        QtCore.QMetaObject.connectSlotsByName(interfaz_principal)

    def a_salir(self):
        print("Fin de ejecución")
        exit()
    def a_captura_datos(self):
        subprocess.call(['python36', "final_interfaz_captura_datos_mpl.py"])

    def a_configuracion_parametros(self):
        subprocess.call(['python36', "interfaz_parametros_temperatura.py"])

    def a_reportes(self):
        #subprocess.call(['python36', "interfaz_reportes.py"])
        subprocess.call(['python36', "Intento_2_GUI_Reportes.py"])

    def retranslateUi(self, interfaz_principal):
        _translate = QtCore.QCoreApplication.translate
        interfaz_principal.setWindowTitle(_translate("interfaz_principal", "MainWindow"))
        self.label.setText(_translate("interfaz_principal", "MONITOR DE TEMPERATURA"))
        self.label_2.setText(_translate("interfaz_principal", "MPIP - DABM 2022-2"))
        self.label_3.setText(_translate("interfaz_principal", "Por favor selecciona la opción que deseas que el programa realice"))
        self.captura_datos.setText(_translate("interfaz_principal", "Captura de datos"))
        self.configuracion_parametros.setText(_translate("interfaz_principal", "Configuración de parámetros"))
        self.reportes.setText(_translate("interfaz_principal", "Visualizar reportes"))
        self.salir.setText(_translate("interfaz_principal", "Salir del programa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaz_principal = QtWidgets.QMainWindow()
    ui = Ui_interfaz_principal()
    ui.setupUi(interfaz_principal)
    interfaz_principal.show()
    sys.exit(app.exec_())
