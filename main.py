# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import json

with open("data.json", "r") as file:
    data = json.load(file)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("background-color: rgb(113, 130, 170);\n"
"font: 75 italic 10pt \"Bahnschrift\";\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 31, 181, 41))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 361, 391))
        self.groupBox.setStyleSheet("background-color: rgb(79, 85, 122);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.official_name = QtWidgets.QLabel(self.groupBox)
        self.official_name.setText("")
        self.official_name.setObjectName("official_name")
        self.gridLayout_2.addWidget(self.official_name, 0, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.capital = QtWidgets.QLabel(self.groupBox)
        self.capital.setText("")
        self.capital.setObjectName("capital")
        self.gridLayout_2.addWidget(self.capital, 1, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.region = QtWidgets.QLabel(self.groupBox)
        self.region.setText("")
        self.region.setObjectName("region")
        self.gridLayout_2.addWidget(self.region, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.callingCode = QtWidgets.QLabel(self.groupBox)
        self.callingCode.setText("")
        self.callingCode.setObjectName("callingCode")
        self.gridLayout_2.addWidget(self.callingCode, 3, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 30, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 80, 371, 391))
        self.groupBox_2.setStyleSheet("background-color: rgb(79, 85, 122);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.population = QtWidgets.QLabel(self.groupBox_2)
        self.population.setText("")
        self.population.setObjectName("population")
        self.gridLayout.addWidget(self.population, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.area = QtWidgets.QLabel(self.groupBox_2)
        self.area.setText("")
        self.area.setObjectName("area")
        self.gridLayout.addWidget(self.area, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.timezones = QtWidgets.QLabel(self.groupBox_2)
        self.timezones.setText("")
        self.timezones.setObjectName("timezones")
        self.gridLayout.addWidget(self.timezones, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.gini = QtWidgets.QLabel(self.groupBox_2)
        self.gini.setText("")
        self.gini.setObjectName("gini")
        self.gridLayout.addWidget(self.gini, 3, 1, 1, 1)
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(630, 10, 131, 61))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/newPrefix/flags-img/af.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countries"))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>test 123456789</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Please choose your country:"))
        self.groupBox.setTitle(_translate("MainWindow", "General information"))
        self.label_2.setText(_translate("MainWindow", "Official name:"))
        self.label_5.setText(_translate("MainWindow", "Capital:"))
        self.label_6.setText(_translate("MainWindow", "Continent"))
        self.label_4.setText(_translate("MainWindow", "Country Code:"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Detailed Informations"))
        self.label_7.setText(_translate("MainWindow", "Population (2010):"))
        self.label_8.setText(_translate("MainWindow", "Surface Area"))
        self.label_9.setText(_translate("MainWindow", "Timezone"))
        self.label_10.setText(_translate("MainWindow", "Gini Coeficient"))

        #fill comboBox with the list of name of countries
        for key, country in data.items():
            self.comboBox.addItem(country["name"], key)

        #refreshes result when the button is clicked    
        self.pushButton.clicked.connect(self.clicked)
        
    def clicked(self):
        
        #Acessing the currently selected country name
        self.search_name = str(self.comboBox.currentText())

        #looking for country key to acess the data
        for key, value in data.items():
            if value["name"] == self.search_name:
                self.result_key = key
                break
            
        self.official_name.setText(str(data[self.result_key]["official_name"]))
        self.capital.setText(str(data[self.result_key]["capital"]))
        self.region.setText(str(data[self.result_key]["region"]))
        self.callingCode.setText(str(data[self.result_key]["callingCode"]))
        
        #formatting population so it's easier to read
        self.fpopulation = data[self.result_key]["population"]
        self.fpopulation = f"{self.fpopulation:,}"
        self.fpopulation = self.fpopulation.replace(",", " ")
        self.population.setText(str(self.fpopulation))
        
        #formatting area so it's easier to read
        self.farea = data[self.result_key]["area"]
        self.farea = f"{self.farea:,}"
        self.farea = self.farea.replace(",", " ")
        self.area.setText(str(self.farea) +" km²")
        
        self.timezones.setText(str(data[self.result_key]["timezones"]))
        self.gini.setText(str(data[self.result_key]["gini"]))
        
        #displays the image of the selected country when PushButton is clicked
        self.img_label.setPixmap(QPixmap(f"flags-img/{data[self.result_key]["alpha2Code"]}.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
