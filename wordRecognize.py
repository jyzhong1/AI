# author: Jingyi Zhong
# date: 2021.6.1
# -*- coding: utf-8 -*-


from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QMessageBox

from PyQt5 import QtGui

import cv2
import docx
import sys
import time

from MyOcr import Ui_MyOcrMainWindow

# 图片文字识别相关模块
from PIL import Image
import pytesseract

class MyOcrWinclass (QMainWindow, Ui_MyOcrMainWindow):

    def __init__(self, fontsize):
        super(MyOcrWinclass, self).__init__()

        #layout = QVBoxLayout()
        self.setupUi(self)

        self.fileOpened = False
        self.fileOcred = False
        self.imagePasted = False

        self.OcredTextEdit.setText('')
        self.OcredTextEdit.setFont(QtGui.QFont('SansSerif', fontsize))

        self.lang = 'eng'

#        self.OcrCheckBox.stateChanged.connect(self.on_action_OcrCheckBox_stateChanged(self.OcrCheckBox.checkState()))
        # 获取显示器分辨率大小
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
#        print('w {},h {} '.format(self.height,self.width))
        
        if self.width > 100:
            #self.location = QtCore.QRect(1, 58, self.screenRect.width(), self.screenRect.height() - 80)
            self.location = QtCore.QRect(1, 30, self.screenRect.width(), self.screenRect.height() - 40)
            self.setGeometry(self.location)
            #self.resize(self.screenRect.width(), self.screenRect.height())
            # 控件布局、显示设置
            x, y, y0, w, h, margin = 6, 10, 20, self.width/2, self.height - 20, 104
            self.OcrCheckBox.setGeometry(QtCore.QRect(x, y, w, y0))
            self.gridLayoutWidget.setGeometry(QtCore.QRect(x, y + y0 + 4, w + 10, h - margin - y))
            self.OcredTextEdit.setGeometry(QtCore.QRect(x + w + 26, y + y0 + 4, w - 50, h - margin - y))

        else:
            self.location = QtCore.QRect(1, 30, self.screenRect.width(), self.screenRect.height() - 10)
            self.setGeometry(self.location)
            #self.resize(self.screenRect.width(), self.screenRect.height())
            # 控件布局、显示设置
            self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, self.width/2 + 40, self.height - 110))
            self.OcredTextEdit.setGeometry(QtCore.QRect(self.width/2 + 60, 10,  self.width/2 - 75, self.height - 110))

        self.item = QGraphicsPixmapItem()  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)  # 将像素图元加入场景
        ret = self.OcrGraphicsView.setScene(self.scene)  # 将场景添加至视图

        self.tmpImageFile = './tmp01.png'
        self.logsText = '\n'
        self.logsFileName = './OcredText.log'

    def getCfgFilePath(self):
        '''
        filePath = './ocrcfg.ini'

        with open(filePath, 'r') as fo:
            pyocrCfgFile = fo.read()
            pytesseract.pytesseract.tesseract_cmd = pyocrCfgFile
        '''
        pass

    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        #print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == 86):
            print('从剪贴板获取图像：')
            self.on_actionPaste_triggered()

        # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
        """
        if (event.key() == Qt.Key_P):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + p")
            else:
                print("p")
        
        if (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
            print("shift + o")
        """

    #def mousePressEvent(self, event):
    #    if event.button() == Qt.LeftButton:
    #        print("鼠标左键点击")
    #    elif event.button() == Qt.RightButton:
    #        print("鼠标右键点击")
    #        self.on_actionPaste_triggered()
    #    elif event.button() == Qt.MidButton:
    #        print("鼠标中键点击")

    @QtCore.pyqtSlot()
    def on_action_Clear_triggered(self):
        self.fileOcred = False
        self.imagePasted = False
        self.OcredTextEdit.setPlainText('')
        self.OcrGraphicsView.setScene(None)  # 将场景清空
        print('clear all')


    def setscene(self, item):
        self.scene.clear()
        self.scene.addItem(item)  # 将像素图元加入场景
        ret = self.OcrGraphicsView.setScene(self.scene)  # 将场景添加至视图
                
        
    @QtCore.pyqtSlot()
    def on_actionPaste_triggered(self):
        ret = 0
        clipboard = QApplication.clipboard()
        if clipboard.mimeData().hasImage():
            #clipboard.mimeData().hasFormat()
            #self.imageLabel.setPixmap(clipboard.pixmap())
            pix = clipboard.pixmap()

            item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.setscene(item) # 将像素图元加入场景
            
            time.sleep(0.03)

            try:
                ret = pix.save(self.tmpImageFile)
                img = Image.open(self.tmpImageFile)

                #'''pix.fromImage()
                if self.OcrCheckBox.isChecked():
                    self.lang = 'chi_sim'
                else:
                    self.lang = 'eng'

                self.imagePasted = False

                txt = pytesseract.image_to_string(img, self.lang)

                self.imagePasted = True
                self.logsText = self.logsText + '\nOcred text from clipboard.'

                # 插入识别的文字
                self.OcredTextEdit.insertPlainText('\n' + txt)

                self.setWindowTitle(self.mWinTitle)

            except Exception as e:
                print('exception:', e)
                self.logsText = self.logsText + '\nfail to img in Paste'

        elif clipboard.mimeData().hasText():
            self.imagePasted = True
            txt = clipboard.mimeData().text()
            ret = self.OcredTextEdit.insertPlainText('\n' + txt)

            self.setWindowTitle(self.mWinTitle)

        else:
            print('paste null')

        print('language:{}, state checked?-{}'.format(self.lang, self.OcrCheckBox.isChecked()))

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.ocrFileName, ret = QFileDialog.getOpenFileName(self,
                                                    "选取图像文件",
                                                    ".",
                                                    "Png Files (*.png);;Jpg Files (*.jpg)")

        try:
            import numpy as np

            ## 读取图像，解决imread不能读取中文路径的问题
            def cv_imread(filePath):
                
                 cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
                 ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
                 ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
                 return cv_img

            # 读取图像
            img = cv_imread(self.ocrFileName)
            #img  = cv2.imread(self.ocrFileName)

            img0 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道

            self.setWindowTitle(self.mWinTitle + ' - ' + self.ocrFileName)

        except:
            print('cv2.imread is error')
            return

        col = img0.shape[1]  # 获取图像大小
        row = img0.shape[0]
        bw = img0.shape[2]

        #self.zoomscale = 1  # 图片放缩尺度

        if bw == 3:
            frame = QtGui.QImage(img0, col, row, col * bw,  # bytesPerLine = 3 * width 非对齐
                                 QtGui.QImage.Format_RGB888)
        elif bw == 1:
            frame = QtGui.QImage(img0, col, row, col * bw,
                                 QtGui.QImage.Format_Indexed8)
        else:
            frame = QtGui.QImage(img0, col, row, col, QtGui.QImage.Format_RGB888)

        pix = QtGui.QPixmap.fromImage(frame)

        item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.setscene(item) # 将像素图元加入场景
        time.sleep(0.03)
        self.fileOpened = True
        self.fileOcred = False

        # 开始识别
        print('begin to ocr...')
        self.on_action_Ocr_triggered()

    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        if self.fileOcred or self.imagePasted:
            outFileName = QFileDialog.getSaveFileName(self, "保存文件", ".", "Docx Files (*.docx);;")
            if outFileName[0] != '':
                ind = outFileName[0].rindex('.') + 1
                if outFileName[0][ind:] != 'docx':
                    outFileName[0] += '.docx'
                my_doc = docx.Document()
                my_doc.add_paragraph(self.OcredTextEdit.toPlainText())
                ret = my_doc.save(outFileName[0])
                print('File {0} is saved successfully.'.format(outFileName[0]))

        else:
            print("file Ocred error")

    @QtCore.pyqtSlot()
    def on_action_OcrCheckBox_stateChanged(self, state):
        print('checkbox changed is {0},{1}'.format(self.OcrCheckBox.state, state))

    @QtCore.pyqtSlot()
    def on_action_Ocr_triggered(self):

        if self.OcrCheckBox.isChecked():
            self.lang = 'chi_sim'
        else:
            self.lang = 'eng'

        if self.fileOpened is True and self.ocrFileName != '': # or self.imagePasted is True:
            self.logsText = self.logsText + 'Ocr_triggered, file <{0}> Opened\n'.format(self.ocrFileName)

            try:
                img = Image.open(self.ocrFileName)
                txt = pytesseract.image_to_string(img, self.lang)
                self.OcredTextEdit.insertPlainText('\n' + txt)
                self.fileOcred = True

            except:
                print('failed to ocr ')
        else:
            QMessageBox.about(self, '识别文件', '没有要识别的文件')

    def outLogs(self):
        with open(self.logsFileName, 'w+') as fo:
            fo.write(self.logsText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myOcr = MyOcrWinclass(20)
    myOcr.show()
    ret = app.exec_()
    myOcr.outLogs()
    sys.exit(ret)
