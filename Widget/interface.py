from distutils import command
from unicodedata import numeric
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QFileDialog,QMessageBox,QTableWidgetItem
from Widget.renseigmnement_carte_Id import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import sqlite3



class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)

        self.btn_valider1.clicked.connect(self.valider)
        self.btn_photo.clicked.connect(self.photo)
        self.btn_annuler.clicked.connect(self.annuler)
        #self.listeEnregistrement.clicked.connect(self.listers)
        #self.buttonErase.clicked.connect(self.deleteLater)
    # def listers(self):
    #     connexion_db=sqlite3.connect("carto.db")
    #     c = connexion_db.cursor()
    #     command="""SELECT * FROM carto"""
    #     resultat=c.execute(command)
    #     self.tableWidget.setRowCount(0)
    #     for row_number,row_data in enumerate(resultat):
    #         self.tableWidget.insertRow(row_number)
    #         for column_number,data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
    def RecupDonnees(self):
        pass
    def valider(self):
        if self.nom.text()=="" or self.prenom.text()=="" or self.lieu.text()=="" or self.taille.text()=="":
            QMessageBox.about(self, "Title", "Remplissez les champs!")
        elif self.taille.text().isalpha():
            QMessageBox.about(self, "Title", " Taille en numerique!")
        else:
            connexion=sqlite3.connect("carto.db")
            dicto={
            "nom": self.nom.text(),
            "prenom": self.prenom.text(),
            "lieu_naissance": self.lieu.text(),
            "date_naissance": self.dateNaissance.text(),
            "taille": self.taille.text(),
            "nationalite": self.nationalite.text(),
            "sexe":self.comboBoxSexe.currentText(),
            "validite": self.Validite.text()
        
            }
                
            c = connexion.cursor()
        
            #--------------creation de la table dans la base de donnees---------
            c.execute("""CREATE TABLE IF NOT EXISTS carta(
                nom text,
                prenom text,
                lieu_naissance text,
                date_naissance text,
                taille text,
                sexe text,
                validite text
            )""")


            #--------enregistrement des element dans la base de donnees---------- 
            c.execute("INSERT INTO carta VALUES(:nom, :prenom, :lieu_naissance, :date_naissance, :taille, :sexe, :validite)", dicto)
            
            #---------ajout dans la base de donnees-----
            connexion.commit()
            connexion.close()
            
        connexion_db=sqlite3.connect("carto.db")
        c = connexion_db.cursor()
        command="""SELECT * FROM carta"""
        resultat=c.execute(command)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connexion_db.commit()
        connexion_db.close()
   
    def photo(self):
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac-05/Desktop')
        self.label_photo1.setPixmap(QPixmap(file_name[0]))
        self.label_photo2.setPixmap(QPixmap(file_name[0])) 
        self.photo.setText(file_name[0])
        print(file_name) 
    def annuler(self):
        # self.nom.deleteLater()
        # self.prenom.deleteLater()
        # self.lieu.deleteLater()
        # self.taille.deleteLater()
        # self.comboBox_jours.deleteLater()
        # self.comboBox_mois.deleteLater()
        # self.comboBox_annees.deleteLater()
        # self.taille.deleteLater()
        # self.nationalite.deleteLater()
        # self.validite.deleteLater()
        pass
    