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
        

    def requete(self):
        #connexion a la base de donnees
        conn =sqlite3.connect("carto.db")

        #positio de du cursor
        c=conn.cursor()

        command="""SELECT nom,prenom,date_naissance,lieu_naissance,taille,sexe,nationalite,validite FROM carta"""
        resultat = c.execute(command)
    

        self.setNom.setT()

