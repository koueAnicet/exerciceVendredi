import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.interface import AccountPage


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()

#interface

from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QDialog,QMessageBox
from Widget.renseigmnement_carte_Id import Ui_MainWindow
import sqlite3


class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)