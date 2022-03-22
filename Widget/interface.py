from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QFileDialog,QMessageBox,QTableWidgetItem
from Widget.renseigmnement_carte_Id import Ui_MainWindow
from PyQt5.QtGui import QPixmap
#from email.mime.text import MIMEText
import smtplib
import sqlite3



class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)

        self.btn_valider1.clicked.connect(self.valider)
        self.btn_refresh.clicked.connect(self.refresh)
        self.btn_photo.clicked.connect(self.Get_photo)
        self.btn_annuler.clicked.connect(self.annuler)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_update.clicked.connect(self.update)
        self.btn_search.clicked.connect(self.search)

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
    def Get_photo(self):
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac-05/Desktop')
        self.labPhoto.setPixmap(QPixmap(file_name[0]))
        self.affichLienPhoto.setText(file_name[0])
        return file_name[0]
    
    def valider(self):
        
        if self.nom.text()=="" or self.prenom.text()=="" or self.lieu.text()=="" or self.taille.text()=="":
            QMessageBox.about(self, "Title", "Remplissez les champs!")
        elif self.taille.text().isalpha():
            QMessageBox.about(self, "Title", " Taille en numerique!")
        
        else:
            
            print(self.Get_photo())

            connexion=sqlite3.connect("carto.db")
            
            dicto={
            "nom": self.nom.text(),
            "prenom": self.prenom.text(),
            "date_naissance": self.dateNaissance.text(),
            "lieu_naissance": self.lieu.text(),
            "taille": self.taille.text(),
            "sexe":self.comboBoxSexe.currentText(),
            "nationalite": self.nationalite.text(),
            "validite": self.Validite.text(),
            "photo":  self.Get_photo()
        
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
                nationalite text,
                validite text,
                photo file
                
            )""")


            #--------enregistrement des element dans la base de donnees---------- 
            c.execute("INSERT INTO carta VALUES(:nom, :prenom, :date_naissance, :lieu_naissance,  :taille, :sexe, :nationalite, :validite, :photo)", dicto)
            QMessageBox.about(self,"validate","succès d'enregistrement")
            
            #---------ajout dans la base de donnees-----
            connexion.commit()
            connexion.close()
            
       
    
   #    connexion=sqlite3.connect("carto.db")
    #     d={
    #         "photo": file_name.text()

    #     }
                
    #     c = connexion.cursor()

    #     #--------enregistrement des element dans la base de donnees---------- 
    #     c.execute("INSERT INTO carta VALUES(:photo", d)
        
    #     #---------ajout dans la base de donnees-----
    #     connexion.commit()
    #     connexion.close()
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
    def delete(self):
           pass 
            
    def update(self):
        connexion=sqlite3.connect("carto.db") 
        c=connexion.cursor()
        
        nom_=str(self.nom.text())
        prenom_=self.prenom.text()
        date_naissance_=self.dateNaissance.text()
        lieu_naissance_=self.lieu.text()
        taille_=self.taille.text()
        sexe_=self.comboBoxSexe.currentText()
        nationalite_=self.nationalite.text()
        validite_=self.Validite.text()
        
        row=(nom_,prenom_,date_naissance_,lieu_naissance_,taille_,sexe_,nationalite_,validite_)
        command=''' UPDATE carta  SET prenom_=?,date_naissance_=?,lieu_naissance_,taille_=?,sexe=?,nationalite_=?,validite_=? WHERE nom=nom_'''
        c.execute(command,row)
        
        
    def delete(self):
        connexion=sqlite3.connect("carto.db") 
        c=connexion.cursor()
        
        d=self.nom.text()
        
        requete=''' DELETE FROM carta WHERE nom=?'''
        c.execute(requete,d)
        
        connexion.commit()
        
        
    
    #methode de recherche
    def search(self):
        connexion=sqlite3.connect("carto.db") 
        c=connexion.cursor()
        nom_search=str(self.name_search.text())
        
        requete='''SELECT * FROM carta WHERE nom=?'''
        resultat=c.execute(requete,[nom_search])
        for row_number,row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connexion.commit()
        connexion.close()
        
    def refresh(self):
        
        connexion_db=sqlite3.connect("carto.db")
        c = connexion_db.cursor()
        command="""SELECT nom,prenom,date_naissance,lieu_naissance,taille,sexe,nationalite,validite FROM carta"""
        resultat=c.execute(command)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connexion_db.commit()
        connexion_db.close()
   