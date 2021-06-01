# /user/bin/python37
# author: Jingyi Zhong
# date: 2021.6.1
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyOcrMainWindow(object):
    def setupUi(self, MyOcrMainWindow):
        MyOcrMainWindow.setObjectName("MyOcrMainWindow")
#        MyOcrMainWindow.resize(1440, 800)
        self.centralwidget = QtWidgets.QWidget(MyOcrMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
#        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 831, 691))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.OcrGraphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.OcrGraphicsView.setObjectName("OcrGraphicsView")

        self.gridLayout.addWidget(self.OcrGraphicsView, 0, 1, 1, 1)

        self.OcredTextEdit = QtWidgets.QTextEdit(self.centralwidget)
#       self.OcredTextEdit.setGeometry(QtCore.QRect(860, 60, 561, 691))
        self.OcredTextEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.OcredTextEdit.setObjectName("OcredTextEdit")

        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
#      self.ImageLabel.setGeometry(QtCore.QRect(300, 10, 91, 21))

 #       font = QtGui.QFont()
 #       font.setFamily("微软雅黑")
 #       font.setPointSize(12)
 #       font.setBold(True)
 #       font.setWeight(75)
 #       self.ImageLabel.setFont(font)

        self.ImageLabel.setObjectName("ImageLabel")
        self.OcredLabel = QtWidgets.QLabel(self.centralwidget)
#        self.OcredLabel.setGeometry(QtCore.QRect(1080, 10, 121, 41))

#        font = QtGui.QFont()
#        font.setFamily("微软雅黑")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        self.OcredLabel.setFont(font)

        self.OcredLabel.setObjectName("OcredLabel")

        self.OcrCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.OcrCheckBox.setGeometry(QtCore.QRect(200, 80, 80, 30))
        self.OcrCheckBox.setObjectName("OcrCheckBox")

        self.gridLayoutWidget.raise_()
        self.OcredTextEdit.raise_()
        self.OcredLabel.raise_()
        self.ImageLabel.raise_()
#       self.OcrCheckBox.raise_()
        MyOcrMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyOcrMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_word = QtWidgets.QMenu(self.menubar)
        self.menu_word.setObjectName("menu_word")
        MyOcrMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyOcrMainWindow)
        self.statusbar.setObjectName("statusbar")
        MyOcrMainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MyOcrMainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionPaste = QtWidgets.QAction(MyOcrMainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionSave = QtWidgets.QAction(MyOcrMainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionAbout = QtWidgets.QAction(MyOcrMainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.action_Ocr = QtWidgets.QAction(MyOcrMainWindow)
        self.action_Ocr.setObjectName("action_Ocr")

        
        self.action_Clear = QtWidgets.QAction(MyOcrMainWindow)
        self.action_Clear.setObjectName("action_Clear")


        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionPaste)
        self.menu_File.addAction(self.actionSave)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_word.addAction(self.action_Ocr)

        self.menu_word.addAction(self.action_Clear) #清空
        
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_word.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.mWinTitle = '文字识别软件'
        self.retranslateUi(MyOcrMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MyOcrMainWindow)

    def retranslateUi(self, MyOcrMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MyOcrMainWindow.setWindowTitle(_translate("MyOcrMainWindow", self.mWinTitle))

#        self.ImageLabel.setText(_translate("MyOcrMainWindow", "图  像"))
#        self.OcredLabel.setText(_translate("MyOcrMainWindow", "识别结果"))
        self.OcrCheckBox.setText(_translate("MyOcrMainWindow", "识别中文"))

        self.menu_File.setTitle(_translate("MyOcrMainWindow", "文件"))
        self.menu_Help.setTitle(_translate("MyOcrMainWindow", "帮助"))
        self.menu_word.setTitle(_translate("MyOcrMainWindow", "文字识别"))

        self.actionOpen.setText(_translate("MyOcrMainWindow", "打开文件"))
        self.actionPaste.setText(_translate("MyOcrMainWindow", "粘贴图片"))
        self.actionSave.setText(_translate("MyOcrMainWindow", "保存文本"))

        self.actionAbout.setText(_translate("MyOcrMainWindow", "关于"))
        self.action_Ocr.setText(_translate("MyOcrMainWindow", "文字识别"))

        self.action_Clear.setText(_translate("MyOcrMainWindow", "清空结果"))
