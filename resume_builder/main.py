#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi

from fpdf import FPDF
import webbrowser

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('/home/didik/FGA-final-project/resume_builder/ui.ui', self)
        self.setWindowTitle('FGA Resume Builder')
        self.save_btn.clicked.connect(self.save_action)
        self.foto_btn.clicked.connect(self.foto_action)

        self.pdf = FPDF(format='A4', unit='mm')
        self.PATH = '/home/didik/FGA-final-project/resume_builder/hasil/'
    
    def save_action(self):
        self.pdf.add_page()
        self.create_header()
        self.create_body()
        self.create_footer()
        filename = self.PATH + str(self.line_nama.text()) + '.pdf'
        self.pdf.output(filename)
        webbrowser.open_new(filename)

    def foto_action(self, foto_dir = None):
        if not foto_dir:
            foto_dir, _ = QFileDialog.getOpenFileName(self, 'Pilih foto', '/home/didik/FGA-final-project/resume_builder/', 'Images (*.png *.jpg *jpeg', options=QFileDialog.DontUseNativeDialog)
            if not foto_dir:
                return
        self.foto_dir = foto_dir

    def create_header(self):
        self.pdf.image('/home/didik/FGA-final-project/resume_builder/fga.png', h=25, x=60)
        self.pdf.set_y(45)
        self.pdf.set_font('helvetica', 'B', 26)
        epw = self.pdf.w - 2 * self.pdf.l_margin
        self.pdf.cell(epw, 0.0, 'RESUME', align='C')
    
    def create_body(self):
        epw = self.pdf.w - 2*self.pdf.l_margin + 100
        self.pdf.set_font('helvetica', '', 16)
        
        def cell(x,y,string):
            self.pdf.set_y(y)
            self.pdf.set_x(x)
            self.pdf.cell(epw, 0.0, string)
        #foto
        self.pdf.image(self.foto_dir, h = 25, x=90, y = 50)
        #nama
        cell(40,90,'Nama'); cell(80,90,f' : {self.line_nama.text()}')
        #alamat
        cell(40,100,'Alamat'); cell(80,100,f' : {self.line_alamat.text()}')
        #email
        cell(40,110,'Email');cell(80,110,f' : {self.line_email.text()}')
        #pendidikan
        cell(40,120,'Pendidikan');cell(80,120,f' : {self.line_pendidikan.text()}')
        #ipk
        cell(40,130,'GPA / IPK ');cell(80,130,f' : {self.line_ipk.text()}')
        #prestasi 1
        cell(40,140,'Prestasi 1');cell(80,140,f' : {self.line_prestasi1.text()}')
        #prestasi 2
        cell(40,150,'Prestasi 2');cell(80,150,f' : {self.line_prestasi2.text()}')
        #prestasi 3
        cell(40,160,'Prestasi 3');cell(80,160,f' : {self.line_prestasi3.text()}')
    
    def create_footer(self):
         # Page numbers in the footerself.WIDTH
        self.pdf.set_y(-15)
        self.pdf.set_font('times', 'I', 10)
        self.pdf.set_text_color(128)
        #self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C') #set page
        self.pdf.content = 'Produced by FGA Developer'
        self.pdf.cell(0,-15, self.pdf.content , 0, 0, 'C')

app = QApplication(sys.argv)
window = MainUI()
window.setFixedWidth(280)
window.setFixedHeight(400)
window.show()
app.exec_()