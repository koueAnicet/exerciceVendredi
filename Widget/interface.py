from email import message
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QFileDialog,QMessageBox,QTableWidgetItem
from Widget.renseigmnement_carte_Id import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from email.mime.text import MIMEText
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
    def RecupDonnees(self):
        pass


    def Get_photo(self):
        global photo_var
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac-05/Desktop')
        photo_var=file_name[0]
        self.labPhoto.setPixmap(QPixmap(file_name[0]))
        #self.affichLienPhoto.setText(file_name[0])
        return photo_var

    
        

    def valider(self):
        
       
        
        if self.nom.text()=="" or self.prenom.text()=="" or self.lieu.text()=="" or self.taille.text()=="":
            QMessageBox.about(self, "champs", "Remplissez les champs!")
        elif self.taille.text().isalpha():
            QMessageBox.about(self, "Taille", " Taille en numerique!")
        
        else:

            connexion_validate=sqlite3.connect("carto.db")

            dicto={
            "nom": self.nom.text(),
            "prenom": self.prenom.text(),
            "date_naissance": self.dateNaissance.text(),
            "lieu_naissance": self.lieu.text(),
            "taille": self.taille.text(),
            "sexe":self.comboBoxSexe.currentText(),
            "nationalite": self.nationalite.text(),
            "validite": self.Validite.text(),
            "photo": photo_var
        
            }
                
            c = connexion_validate.cursor()
        
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
            connexion_validate.commit()
            connexion_validate.close()

        title="Python"
        msg_content='<h2>{title}<font color="blue">ok</font>\n'.format(title=title)
        message= MIMEText(msg_content,'html')

        message['From']='Koue Anicet<anicetkoue@gmail.com>'
        message['To']='anick <anicetkoue1@mgail.com>'
        message['Subjet']='any Subject'

        msg_full= message.as_string()
        server =smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('anicetkoue@gmail.com','bgnnfnggf')
        server.sendmail('anicetkoue@gmail.com',
                        [self.email.text()],
                        msg_full)
        server.quit()

        #suppresion des champs de saisies
        self.nom.clear()
        self.prenom.clear()
        self.dateNaissance.clear()
        self.lieu.clear()
        self.taille.clear()
        self.nationalite.clear()
        self.Validite.clear()
        self.labPhoto.clear()
    
   
    def annuler(self):
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
        search_name=self.name_search.text()
        
        command='''SELECT * FROM carta WHERE nom=?'''
        resultat=c.execute(command,[search_name])
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(resultat):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        
        
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
   