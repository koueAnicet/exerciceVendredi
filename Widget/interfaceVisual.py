from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QFileDialog,QMessageBox,QTableWidgetItem
from Widget.visualisation_carte import Ui_MainWindow
from PyQt5.QtGui import QPixmap
#from email.mime.text import MIMEText
import smtplib
import sqlite3

class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)
        self.btn_voirPhoto.clicked.connect(self.requete) 

    def requete(self):
        #connexion a la base de donnees
        conn =sqlite3.connect("carto.db")

        #positio de du cursor
        c=conn.cursor()
        
        command="""SELECT nom,prenom,date_naissance,lieu_naissance,taille,sexe,nationalite,email,photo FROM carta WHERE nom='koue'"""
        v=c.execute(command)
        for i in v:
            print(i[0])
            
        
        self.setNom.setText(i[0].upper())
        self.setPrenom.setText(i[1].upper())
        self.setLieuNaissance.setText(i[2].upper())
        self.setDateNaissance.setText(i[3])
        self.setTaille.setText(i[4])
        self.setSexe.setText(i[5].upper())
        self.setNationalite.setText(i[6].upper())
        self.setPhotoLabel.setPixmap(QPixmap(i[8]))
