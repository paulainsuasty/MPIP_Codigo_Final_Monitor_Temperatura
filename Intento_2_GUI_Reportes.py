# -*- coding: utf-8 -*-
import mplwidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import subprocess
import statistics
from PIL import Image
import csv

#global valores_temperatura
#imagen = "logocbmt.jpg"
#image = Image.open("logocbmt.jpg")
#new_image = image.resize((200, 200))
#new_image.save('logo_cb_ajustado.jpg')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(742, 451)
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo_cb = QtWidgets.QFrame(self.centralwidget)
        self.logo_cb.resize(400, 200)
        self.logo_cb.setGeometry(QtCore.QRect(350, 50, 200, 200))
        self.logo_cb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_cb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_cb.setObjectName("logo_cb")
        # self.logo_cb.setStyleSheet("backgroung-image: url(C:\Users\LENOVO\OneDrive - Universidad del rosario\Escritorio\Final_Final_DABM_Monitor_Temperatura\logocbmt.jpg);")
        #self.logo_cb.setStyleSheet("background-image: url(logocbmt.jpg);")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.grafica_prueba = MplWidget(self.centralwidget)
        # self.grafica_prueba.setGeometry(QtCore.QRect(410, 60, 301, 161))
        # self.grafica_prueba.setObjectName("grafica_prueba")
        # self.tabla_reporte = QtWidgets.QTableWidget(self.centralwidget)
        # self.tabla_reporte.setGeometry(QtCore.QRect(410, 240, 301, 141))
        # self.tabla_reporte.setObjectName("tabla_reporte")
        # self.tabla_reporte.setColumnCount(2)
        # self.tabla_reporte.setRowCount(3)
        # item = QtWidgets.QTableWidgetItem()
        # self.tabla_reporte.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tabla_reporte.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tabla_reporte.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tabla_reporte.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tabla_reporte.setHorizontalHeaderItem(1, item)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 291, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 280, 300, 15))
        self.label_3.setObjectName("label_3")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 320, 300, 15))
        self.label_5.setObjectName("label_5")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 360, 300, 15))
        self.label_4.setObjectName("label_4")

        self.seleccionar_prueba = QtWidgets.QComboBox(self.centralwidget)
        self.seleccionar_prueba.setGeometry(QtCore.QRect(50, 180, 270, 30))
        self.seleccionar_prueba.setObjectName("seleccionar_prueba")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.boton_aceptar = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.seleccionando_prueba())
        self.boton_aceptar.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.boton_aceptar.setObjectName("boton_aceptar")

        self.boton_volver = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.volver_principal())
        self.boton_volver.setGeometry(QtCore.QRect(200, 300, 75, 23))
        self.boton_volver.setObjectName("boton_volver")

        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        f = open("opciones.csv", "r")
        opciones = f.readlines()
        for op in opciones:
            self.seleccionar_prueba.addItem(op)
        f.close()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Reportes"))
        # item = self.tabla_reporte.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Valor Máximo"))
        # item = self.tabla_reporte.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Valor mínimo"))
        # item = self.tabla_reporte.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Promedio"))
        # item = self.tabla_reporte.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Parámetro"))
        # item = self.tabla_reporte.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Valor"))
        self.label_2.setText(_translate("MainWindow", "Selecciona la prueba de la que deseas obtener el reporte"))
        self.label_3.setText(_translate("MainWindow", "Valor maximo es:"))
        self.label_4.setText(_translate("MainWindow", " Valor Promedio es:"))
        self.label_5.setText(_translate("MainWindow", " Valor minimo es: "))
        self.boton_aceptar.setText(_translate("MainWindow", "Obtener"))
        self.boton_volver.setText(_translate("MainWindow", "Volver"))

    def seleccionando_prueba(self):
        global valores_temperatura
        content = self.seleccionar_prueba.currentText()
        # showing content on the screen though label
        print("Archivo deseado es: " + content)
        #nuevo_cont = "'"+content+"'"
        #print(nuevo_cont)
        ####
        content= content.replace('"','')
        print(content)
        #a = open(content, "r")
        #a = open("'"+content+"'", "r")
        a = open("2022-10-2320_9_42.csv", "r")
        lineas = a.readlines()
        print(lineas)
        valores_temperatura = []
        #print("llegue")
        #datos.append(lineas)
        for l in (lineas):
            # print(l)
           l = l.replace("\n", "")
           l = l.replace("", "")
           l = l.split(";")
           valores_temperatura.append(l)
        #print("llegue a 1")

        for i in range(len(lineas)):
            print("ultimas 4 lineas son:")
            print(valores_temperatura[len(lineas)-1][0])
            print(valores_temperatura[len(lineas) - 2])
            print(valores_temperatura[len(lineas) - 3])

        #max = (valores_temperatura[len(lineas) - 1])
        #self.label_5.setText(((str(max(valores_temperatura)))))
        #self.label_4.setText("hola_4")
        #self.label_3.setText("hola_3")
        #valores_temperatura[len(lineas) - 1]
        #self.label_4.setText(valores_temperatura[len(lineas) - 2])
        #self.label_3.setText(valores_temperatura[len(lineas) - 3])


        imagen = "2022-10-2320_9_1.jpg"
        image = Image.open(imagen)
        new_image = image.resize((200, 200))
        new_image.save('myimage_500.jpg')

        #self.logo_cb.setStyleSheet("background-image: url(logo_ur.jpg);")
        self.logo_cb.setStyleSheet("background-image: url(myimage_500.jpg);")
        #img_prueba = "2022-10-2320_9_1.jpg"
        #self.graphWidget.canvas.ax.plot(img_prueba)
        #self.graphWidget.canvas.draw()


            #(valores_temperatura[len(lineas) - 3]))
        #self.label_4.setText(("MainWindow", "soy"))

        #print("Valores de temperatura son: ", valores_temperatura)
        #print(str(max(valores_temperatura)))
        #val_max_temp = str(max(valores_temperatura))
        #print(str(min(valores_temperatura)))
        #val_min_temp = str(min(valores_temperatura))
        #print("v max es: ", val_max_temp)

        self.label_5.setText(str(valores_temperatura[len(lineas) - 3][0]))
        self.label_4.setText(str(valores_temperatura[len(lineas) - 2][0]))
        self.label_3.setText(str(valores_temperatura[len(lineas) - 1][0]))

        #self.label_3.setText("MainWindow", (max(valores_temperatura)))

        #print(str(statistics.mean(valores_temperatura)))
        #self.
        #inx = 0  # indice
        #for prueba in len():
            #usuario = usuario.replace("\n", "")
            #nombre, password = usuario.split(";")  # sepaarandolo por ;
        #self.tableWidget.insertRow(inx)
        #self.tableWidget.setItem(0, 1, QTableWidgetItem(str(max(valores_temperatura))))
        #self.tableWidget.setItem(1, 1, QTableWidgetItem(str(min(valores_temperatura))))

        #inx = inx + 1
        #print(str(max(valores_temperatura)))
        #print(str(min(valores_temperatura)))
        #print("La fecha en la cual fueron tomados estos datos fue: (AAAA-MM-DD)", nombre_archivo_revisar[:10])
        #nombre_imagen_presentar =  "2022-10-2312_18_34.jpg"
        #im = Image.open(nombre_imagen_presentar)
        #im.show()
        #mplwidget.Figure()
        #mplwidget.Canvas.print_jpg(nombre_imagen_presentar)
        print("fin")
        #escribiendo_resultados()

    # def escribiendo_resultados(self):
    #     global valores_temperatura
    #     self.label_3.setText("MainWindow", (max(valores_temperatura)))

    def volver_principal(self):
        subprocess.call(['python36', "interfaz_principal.py"])

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())