from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel
from Widget.renseigmnement_carte_Id import Ui_MainWindow
import sqlite3

class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)

        self.btn_valider1.clicked.connect(self.valider)
        
        self.btn_photo.clicked.connect(self.photo)
        self.btn_annuler.clicked.connect(self.annuler)
        #self.buttonErase.clicked.connect(self.deleteLater)
    def valider(self):
        connexion=sqlite3.connect("carto.db")
        dicto={
        "nom": self.nom.text(),
        "prenom": self.prenom.text(),
        "lieu_naissance": self.lieu.text(),
        "date_naissance": self.comboBox_jours.currentText(),
        "taille": self.taille.text(),
        "nationalite": self.nationalite.text(),
        "sexe":self.comboBoxSexe.currentText(),
        
        }
               
        c = connexion.cursor()
        
        #--------------creation de la table dans la base de donnees---------
        c.execute("""CREATE TABLE IF NOT EXISTS carta(
            nom text,
            prenom text,
            lieu_naissance text,
            date_naissance text,
            taille text,
            sexe text

        )""")


        #--------enregistrement des element dans la base de donnees---------- 
        c.execute("INSERT INTO carta VALUES(:nom, :prenom, :lieu_naissance, :date_naissance, :taille, :sexe)", dicto)
        
        #---------ajout dans la base de donnees-----
        connexion.commit()
        connexion.close()
        return dicto
        
       
    def photo(self):
        pass
    def annuler(self):
        self.nom.deleteLater()
        self.prenom.deleteLater()
        self.lieu.deleteLater()
        self.taille.deleteLater()
        self.comboBox_jours.deleteLater()
        self.comboBox_mois.deleteLater()
        self.comboBox_annees.deleteLater()
        self.taille.deleteLater()
        self.nationalite.deleteLater()
        self.validite.deleteLater()
    def RecupDonnees(self):
        pass
    def RecupDonnees(self):
        pass