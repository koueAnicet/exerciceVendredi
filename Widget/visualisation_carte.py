# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/visualisation_carte.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 971, 581))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:lightgrey;}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(250, 90, 561, 311))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:lightyellow;\n"
"border:2px solid;\n"
"border-radius:15px;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.setPhotoLabel = QtWidgets.QLabel(self.frame_2)
        self.setPhotoLabel.setGeometry(QtCore.QRect(20, 80, 121, 141))
        self.setPhotoLabel.setStyleSheet("QLabel{\n"
"border-radius:0px;\n"
"border:1px solid black;\n"
"}")
        self.setPhotoLabel.setText("")
        self.setPhotoLabel.setPixmap(QtGui.QPixmap(":/img/Côte_d\'Ivoire.svg.png"))
        self.setPhotoLabel.setScaledContents(True)
        self.setPhotoLabel.setObjectName("setPhotoLabel")
        self.setNom = QtWidgets.QLabel(self.frame_2)
        self.setNom.setGeometry(QtCore.QRect(190, 70, 201, 21))
        self.setNom.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setNom.setObjectName("setNom")
        self.setPrenom = QtWidgets.QLabel(self.frame_2)
        self.setPrenom.setGeometry(QtCore.QRect(190, 110, 131, 20))
        self.setPrenom.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setPrenom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setPrenom.setObjectName("setPrenom")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(190, 210, 51, 16))
        self.label_5.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(270, 210, 41, 16))
        self.label_6.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(190, 170, 201, 20))
        self.label_7.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 280, 81, 20))
        self.label_8.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(190, 260, 121, 21))
        self.label_9.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(380, 240, 60, 16))
        self.label_12.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(190, 10, 311, 31))
        self.label_13.setStyleSheet("QLabel{\n"
"border-radius:0px;\n"
"border:none;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(220, 40, 231, 31))
        self.label_14.setStyleSheet("QLabel{\n"
"border-radius:0px;\n"
"border:none;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(190, 90, 60, 16))
        self.label_10.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(190, 130, 201, 16))
        self.label_11.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setObjectName("label_11")
        self.setSexe = QtWidgets.QLabel(self.frame_2)
        self.setSexe.setGeometry(QtCore.QRect(190, 190, 60, 16))
        self.setSexe.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setSexe.setObjectName("setSexe")
        self.setTaille = QtWidgets.QLabel(self.frame_2)
        self.setTaille.setGeometry(QtCore.QRect(270, 190, 51, 20))
        self.setTaille.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setTaille.setObjectName("setTaille")
        self.setDateNaissance = QtWidgets.QLabel(self.frame_2)
        self.setDateNaissance.setGeometry(QtCore.QRect(190, 150, 201, 16))
        self.setDateNaissance.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setDateNaissance.setObjectName("setDateNaissance")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(320, 70, 121, 20))
        self.label_18.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.setNationalite = QtWidgets.QLabel(self.frame_2)
        self.setNationalite.setGeometry(QtCore.QRect(40, 260, 81, 20))
        self.setNationalite.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setNationalite.setObjectName("setNationalite")
        self.setValidite = QtWidgets.QLabel(self.frame_2)
        self.setValidite.setGeometry(QtCore.QRect(450, 240, 91, 16))
        self.setValidite.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setValidite.setObjectName("setValidite")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(440, 70, 111, 20))
        self.label_21.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(300, 70, 221, 201))
        self.label_22.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/img/images__3_-removebg-preview.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(340, 110, 121, 101))
        self.label_23.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/img/Côte_d\'Ivoire.svg.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.setLieuNaissance = QtWidgets.QLabel(self.frame_2)
        self.setLieuNaissance.setGeometry(QtCore.QRect(190, 240, 141, 16))
        self.setLieuNaissance.setStyleSheet("QLabel{\n"
"border:none;\n"
"}")
        self.setLieuNaissance.setObjectName("setLieuNaissance")
        self.label_22.raise_()
        self.setPhotoLabel.raise_()
        self.setNom.raise_()
        self.setPrenom.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.setSexe.raise_()
        self.setTaille.raise_()
        self.setDateNaissance.raise_()
        self.label_18.raise_()
        self.setNationalite.raise_()
        self.setValidite.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.setLieuNaissance.raise_()
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 20, 541, 31))
        self.label.setObjectName("label")
        self.btn_voirPhoto = QtWidgets.QPushButton(self.frame)
        self.btn_voirPhoto.setGeometry(QtCore.QRect(530, 470, 61, 61))
        self.btn_voirPhoto.setStyleSheet("QPushButton{\n"
"background-color:black;\n"
"color:white;\n"
"font:Italic 16 bold;\n"
"border-radius:20px\n"
"}")
        self.btn_voirPhoto.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/imgCapture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voirPhoto.setIcon(icon)
        self.btn_voirPhoto.setIconSize(QtCore.QSize(100, 100))
        self.btn_voirPhoto.setObjectName("btn_voirPhoto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setNom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">KOUE</span></p></body></html>"))
        self.setPrenom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ANICET</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Sexe</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Taille</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date de naissance</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nationalité</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Lieu de naissance"))
        self.label_12.setText(_translate("MainWindow", "Validité:"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">REBLIQUE DE CÔTE D\'IVORE</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CARTE NATIONALE D\'IDENTITE</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nom</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Prenom</span></p></body></html>"))
        self.setSexe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">M</span></p></body></html>"))
        self.setTaille.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">1,66</span></p></body></html>"))
        self.setDateNaissance.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">16/12/1995</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Immmatriculation: "))
        self.setNationalite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">IVOIRIENNE</span></p></body></html>"))
        self.setValidite.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">03/02/2026</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "C 0012 6948 29"))
        self.setLieuNaissance.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">DEOULE</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">PREVISUALISTION DE LA CARTE D\'IDENTITE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
