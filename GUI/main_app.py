# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import errno
sys.path.append('../')
from default_settings import *
from order_and_set import *
from _codecs import decode
from aux_functions import checkos

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_Dialog(object):
    pathname=''
    
    def validation(self,_string):
        if 'My Clippings.txt' in _string:
            if open(_string, 'r').read().split(separator) >= 1: #is there at least one note??
                self.pushButton_2.setEnabled(True)
                return True
        else:
            return False

    def file_open(self):
        name=QtGui.QFileDialog.getOpenFileName(None,'Abra o Arquivo')
        nameforslash = decode(str(name),'utf-8')
        folders=nameforslash.split('/')
        pathwindows=''
        for folder in folders:
            pathwindows+=decode(folder, 'utf-8')+"\\"
        if checkos():
            self.pathname=pathwindows[:-1]
        else:
            self.pathname=name
        if self.validation(name):
            self.textBrowser.setText('Seu arquivo foi validado, selecione na escolha ao lado o lugar para suas notas (Uma nova pasta com todos os titulos dos livros vai aparecer no caminho indicado)') #It is a kindle format, now you can proceed
        else:
            self.textBrowser.setText('Desculpe, o arquivo possui formato diferente do Kindle')
    
    def file_save(self):
        name=decode(str(QtGui.QFileDialog.getExistingDirectory(None,'Escolha o lugar para salvar as notas')),'utf-8')
        if checkos():#windows path
            complement = '\Book_Notes'
            destiny_path=decode(str(os.path.join(*name.split('/'))) + complement, 'utf-8')
        else:
            complement = '/Book_Notes'
            destiny_path = '/' + decode(str(os.path.join(*name.split('/'))) + complement, 'utf-8')
        if not os.path.exists(name+complement):#if doesn't exists, create
            os.mkdir(name+complement)

        reading=read(self.pathname)#o caminho de leitura ta ok
        lo=create_instances(reading)
        order_dict_1=order_by_title(lo)
        order_dict_2=order_by_category(order_dict_1.copy())
        print_time(order_dict_2, order_dict_1, destiny_path)
        self.textBrowser.setText('Suas notas foram geradas na pasta \"Book_Notes\" em '+ name )

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(401, 291)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 401, 291))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(50, 190, 111, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 54, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 151, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 80, 111, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Sobre = QtGui.QWidget()
        self.Sobre.setObjectName(_fromUtf8("Sobre"))
        self.label_2 = QtGui.QLabel(self.Sobre)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.Sobre)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 351, 192))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabWidget.addTab(self.Sobre, _fromUtf8(""))
        self.pushButton_2.setDisabled(True)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.file_open)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.file_save)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Easy Notes Kindle", None))
        self.pushButton.setText(_translate("Dialog", "Achar arquivo", None))
        self.label_3.setText(_translate("Dialog", "Status", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Entre com seu arquivo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> My Clippings.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">usando o botão abaixo.</p></body></html>", None))
        self.pushButton_2.setText(_translate("Dialog", "Gerar Notas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home", None))
        self.label_2.setText(_translate("Dialog", "Olá Mundo!", None))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sou Vagner Nörnberg, estudante de engenharia .</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decidi fazer esse projeto pessoal em python para me familiarizar com a linguagem.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adoro ler e programar no meu tempo livre, então nada melhor do que misturar as duas coisas em</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">um ideia.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Caso queira entrar em contato segue o e-mail: vsaller@yahoo.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Boas anotações e leitura!</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sobre), _translate("Dialog", "Sobre", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

