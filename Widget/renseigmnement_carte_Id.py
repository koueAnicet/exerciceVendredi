# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/renseigmnement_carte_Id.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 641))
        self.tabWidget.setStyleSheet("QTableWidget{\n"
"background-color:greenlight;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 611))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:lightblue;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 100, 401, 31))
        self.label.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 401, 31))
        self.label_2.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 401, 31))
        self.label_3.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 401, 31))
        self.label_4.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 200, 461, 31))
        self.label_5.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(490, 100, 461, 31))
        self.label_6.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(500, 410, 461, 31))
        self.label_9.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(50, 130, 401, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 240, 401, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 440, 401, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(490, 130, 461, 31))
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(500, 440, 461, 31))
        self.lineEdit_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit_9.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 540, 131, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:lightgreen;\n"
"color:white;\n"
"font:Italic 14 bold;\n"
"border:2px solid white;\n"
"border-radius:12px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 540, 131, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:red;\n"
"color:white;\n"
"font:Italic 14 bold;\n"
"border:2px solid white;\n"
"border-radius:12px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 540, 151, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:green;\n"
"color:white;\n"
"font:Italic 14 bold;\n"
"border:2px solid white;\n"
"border-radius:12px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(490, 240, 461, 31))
        self.comboBox.setStyleSheet("QComboBox{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(50, 330, 51, 31))
        self.label_19.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"ackground-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:8px;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(200, 330, 41, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(340, 330, 51, 31))
        self.label_21.setObjectName("label_21")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 330, 81, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 330, 91, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(390, 330, 61, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(490, 300, 461, 31))
        self.label_10.setStyleSheet("QLabel{\n"
"font: italic 13pt \"Georgia\";\n"
"background-color:#5892bf;\n"
"border-bottom-left-radius:13px;\n"
"border-bottom-right-radius:13px;\n"
"padding-left:15px;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 330, 461, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius:12px;\n"
"}")
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(-20, 20, 1001, 51))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.treeView = QtWidgets.QTreeView(self.tab_2)
        self.treeView.setGeometry(QtCore.QRect(20, 70, 971, 511))
        self.treeView.setObjectName("treeView")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 20, 101, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:red;\n"
"color:white;\n"
"font:Italic 16 bold;\n"
"border-radius:9px\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 20, 101, 41))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color:green;\n"
"color:white;\n"
"font:Italic 16 bold;\n"
"border-radius:9px\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Nom</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Prenom</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Date de naissance</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Lieu de naissance</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Sexe</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">     Taille</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Validité</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Entrez le nom"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Entrez le  prenom"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Entrez le lieu de naissance"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Entrez la  taille"))
        self.pushButton.setText(_translate("MainWindow", "Photo"))
        self.pushButton_2.setText(_translate("MainWindow", "Annuler"))
        self.pushButton_3.setText(_translate("MainWindow", "Valider"))
        self.comboBox.setCurrentText(_translate("MainWindow", "-----choisir le sexe-----"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "choisir"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-----choisir le sexe-----"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Masculin"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Feminin"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Autre"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Jour</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Mois</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Année</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "05"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "06"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "07"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "08"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "09"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "21"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "22"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "23"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "24"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "25"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "26"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "27"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "28"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "29"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "30"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "31"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Janvier"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Fevrier"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Mars"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Avril"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Mai"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Juin"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Juillet"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Août"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Septembre"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Octobre"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Novembre"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Decembre"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "2022"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2021"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "2020"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "2019"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "2018"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "2017"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "2016"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "2015"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "2014"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "2013"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "2012"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "2011"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "2010"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "2009"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "20O8"))
        self.comboBox_4.setItemText(15, _translate("MainWindow", "20O7"))
        self.comboBox_4.setItemText(16, _translate("MainWindow", "20O6"))
        self.comboBox_4.setItemText(17, _translate("MainWindow", "20O5"))
        self.comboBox_4.setItemText(18, _translate("MainWindow", "20O4"))
        self.comboBox_4.setItemText(19, _translate("MainWindow", "20O3"))
        self.comboBox_4.setItemText(20, _translate("MainWindow", "20O2"))
        self.comboBox_4.setItemText(21, _translate("MainWindow", "20O1"))
        self.comboBox_4.setItemText(22, _translate("MainWindow", "2000"))
        self.comboBox_4.setItemText(23, _translate("MainWindow", "1999"))
        self.comboBox_4.setItemText(24, _translate("MainWindow", "1998"))
        self.comboBox_4.setItemText(25, _translate("MainWindow", "1997"))
        self.comboBox_4.setItemText(26, _translate("MainWindow", "1996"))
        self.comboBox_4.setItemText(27, _translate("MainWindow", "1995"))
        self.comboBox_4.setItemText(28, _translate("MainWindow", "1994"))
        self.comboBox_4.setItemText(29, _translate("MainWindow", "1980"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">NATIONALITE</span></p><p><br/></p></body></html>"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Entrez la nationalité"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">PRODUCTION DE CARTE NATIONALE D\'IDENTITE</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_4.setText(_translate("MainWindow", "SUPPRIMER"))
        self.pushButton_5.setText(_translate("MainWindow", "MODIFIER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())