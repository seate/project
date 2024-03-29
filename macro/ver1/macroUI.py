# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'macroUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import macroAction

import sys
from time import sleep
from os import getcwd, listdir, remove, path
from shutil import move
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets

CONFIG = {
'file_path' : 'file_path',
'encoding_set' : 'utf-8',
'StyleSheet' : """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: rgb(37, 37, 38);
    color: rgb(255,255,255);  
    border-radius: 5px;
}
QMenuBar::item:selected {    
    background-color: rgb(100,100,100);
}
QMenuBar::item:pressed {
    background: rgb(100,100,100);
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

QMenu {
    background-color: rgb(100,100,100);   
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
    color: rgb(255,255,255);
}
QMenu::item:selected { 
    background-color: rgb(100,100,100);
    color: rgb(255,255,255);
}
"""
}

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, Mainwindow):
        self.mainwindow = Mainwindow
        self.mainwindow.setObjectName("self.mainwindow")
        self.mainwindow.resize(560, 581)
        self.mainwindow.setStyleSheet("background-color: rgb(37, 37, 38);")

        self.centralwidget = QtWidgets.QWidget(self.mainwindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")

        self.ExecuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExecuteButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ExecuteButton.setStyleSheet("background-color: rgb(51, 51, 51);\n""color: rgb(255, 255, 255);")
        self.ExecuteButton.setObjectName("ExecuteButton")
        self.ButtonLayout.addWidget(self.ExecuteButton)

        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AddButton.setStyleSheet("background-color: rgb(51, 51, 51);\n""color: rgb(255, 255, 255);")
        self.AddButton.setObjectName("AddButton")
        self.ButtonLayout.addWidget(self.AddButton)
        

        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.DeleteButton.setStyleSheet("background-color: rgb(51, 51, 51);\n""color: rgb(255, 255, 255);")
        self.DeleteButton.setObjectName("DeleteButton")
        self.ButtonLayout.addWidget(self.DeleteButton)

        self.gridLayout.addLayout(self.ButtonLayout, 1, 0, 1, 1)

        self.ExecutionList = QtWidgets.QListWidget(self.centralwidget)
        self.ExecutionList.setStyleSheet("background-color: rgb(51, 51, 51);\n""color: rgb(255, 255, 255);")
        self.ExecutionList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ExecutionList.setLineWidth(0)
        self.ExecutionList.setMidLineWidth(0)
        self.ExecutionList.setObjectName("ExecutionList")

        #item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        #item.setBackground(brush)
        #self.ExecutionList.addItem(item)
        self.gridLayout.addWidget(self.ExecutionList, 0, 0, 1, 1)
        self.mainwindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self.mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.mainwindow.setMenuBar(self.menubar)

        self.actionSet_File_Path = QtWidgets.QAction(self.mainwindow)
        self.actionSet_File_Path.setObjectName("actionSet_File_Path")
        self.actionAdd_file = QtWidgets.QAction(self.mainwindow)
        self.actionAdd_file.setObjectName("actionAdd_file")
        self.menuSettings.addAction(self.actionAdd_file)
        self.menuSettings.addAction(self.actionSet_File_Path)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(self.mainwindow)
        self.ActionConnects()
        self.ListInitializing()
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        self.mainwindow.setWindowTitle(_translate("self.mainwindow", "self.mainwindow"))
        self.ExecuteButton.setText(_translate("self.mainwindow", "Execute"))
        self.AddButton.setText(_translate("self.mainwindow", "Add"))
        self.DeleteButton.setText(_translate("self.mainwindow", "Delete"))
        self.ExecutionList.setSortingEnabled(False)
        __sortingEnabled = self.ExecutionList.isSortingEnabled()
        self.ExecutionList.setSortingEnabled(False)
        #item = self.ExecutionList.item(0)
        #item.setText(_translate("self.mainwindow", "test"))
        self.ExecutionList.setSortingEnabled(__sortingEnabled)
        self.menuSettings.setTitle(_translate("self.mainwindow", "File"))
        self.actionSet_File_Path.setText(_translate("self.mainwindow", "Set File Path"))
        self.actionAdd_file.setText(_translate("self.mainwindow", "Add File"))
        self.actionAdd_file.setShortcut(_translate("self.mainwindow", "Ctrl+A"))
    
    #========================functions====================================================================
    
    def ActionConnects(self):
        self.actionAdd_file.triggered.connect(self.AddFileAction)
        self.actionSet_File_Path.triggered.connect(self.FilePathSet)

        self.ExecuteButton.clicked.connect(self.ExecuteButtonAction)
        self.AddButton.clicked.connect(self.AddButtonAction)
        self.DeleteButton.clicked.connect(self.DeleteButtonAction)

    def ListInitializing(self):
        self.ExecutionList.addItems([file for file in listdir(CONFIG['file_path']) if file[-4:] == ".bin"])

    def FilePathSet(self):
        Folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open folder', directory= CONFIG['file_path'])
        if Folder:
            CONFIG['file_path'] = Folder
            with open("setting.txt", 'w') as setting:
                setting.write(CONFIG['file_path'])
                setting.write(CONFIG["setup_path"])
            #리스트에 열려 있는 파일들 갱신
            self.ExecutionList.clear()
            self.ExecutionList.addItems([file for file in listdir(CONFIG['file_path']) if file[-4:] == ".bin"])

    
    def AddFileAction(self):
        Files = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', filter= 'Files(*.bin, *.*)', directory= CONFIG['file_path'])
        print("File:",Files)
        if Files[0]:
            for file in Files[0]:
                move(file, CONFIG['file_path'])


    def ExecuteButtonAction(self):
        msgbox = QtWidgets.QMessageBox(self)
        msgbox.setText("Action will be start in 3 seconds")
        msgbox.exec_()
        sleep(3)
        msgbox.hide()
        self.mainwindow.showMinimized()
        
        for selectedItem in self.ExecutionList.selectedItems():
            macroAction.Control(CONFIG["file_path"] + "/" + selectedItem.text())
    
    def AddButtonAction(self):
        file_name, ext = QtWidgets.QFileDialog.getSaveFileName(filter="Files(*.bin)", directory= CONFIG['file_path'])
        if file_name:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("Action will be start in 3 seconds")
            msgbox.exec_()
            sleep(3)
            msgbox.hide()
            self.mainwindow.showMinimized()

            macroAction.Listening(file_name)
            file_name = path.basename(file_name)
            if file_name in {self.ExecutionList.item(x).text() for x in range(self.ExecutionList.count())}: return
            self.ExecutionList.addItem(path.basename(file_name))
        
    def DeleteButtonAction(self):
        if self.ExecutionList.currentItem():
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setText("Do you really want to delete?")
            msgbox.addButton(QtWidgets.QPushButton('Yes'), QtWidgets.QMessageBox.YesRole)
            msgbox.addButton(QtWidgets.QPushButton('No'), QtWidgets.QMessageBox.NoRole)

            if not msgbox.exec_():
                for selectedItem in self.ExecutionList.selectedItems():
                    print("selecteds: ", selectedItem)
                    #file delete
                    remove(CONFIG['file_path'] + "/" + selectedItem.text())
                    self.ExecutionList.takeItem(self.ExecutionList.row(selectedItem))


def init():
    #first installed
    if not path.isfile("setting.txt"): 
        with open("setting.txt", 'w') as setting:
            setting.write(getcwd() + "\n") #file_path
            setting.write(getcwd()) #setup_path
        CONFIG["file_path"] = getcwd()
    else:
        with open("setting.txt", 'r') as setting:
            CONFIG["file_path"] = setting.readline()
        
def UImain():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(CONFIG['StyleSheet'])
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())

if "__main__" == __name__:
    init()
    UImain()