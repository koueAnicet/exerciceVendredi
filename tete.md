def browser_files(self):
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac_33/Desktop/PHOTO')
        self.label_photo1.setPixmap(QPixmap(file_name[0]))
        self.label_photo2.setPixmap(QPixmap(file_name[0])) 
        self.entry_browser.setText(file_name[0])
        print(file_name) 