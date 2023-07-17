from PyQt5 import QtCore, QtGui, QtWidgets
from vidstream import *
import tkinter as tk
import socket,threading,requests


import sys
from PyQt5.QtWidgets import QAbstractItemView,  QMainWindow, QPushButton, QLabel, QStyleFactory, QTableView, QVBoxLayout, QTableWidgetItem, QMessageBox, QWidget, QShortcut, QLabel, QApplication
server = StreamingServer('localhost',9999)
t1 = threading.Thread(target=server.start_server)
t1.start()
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(750, 735)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 440, 261, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.text_ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_ip.sizePolicy().hasHeightForWidth())
        self.text_ip.setSizePolicy(sizePolicy)
        self.text_ip.setObjectName("text_ip")
        self.gridLayout.addWidget(self.text_ip, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(430, 440, 161, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.port_ip = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_ip.sizePolicy().hasHeightForWidth())
        self.port_ip.setSizePolicy(sizePolicy)
        self.port_ip.setObjectName("port_ip")
        self.gridLayout_2.addWidget(self.port_ip, 0, 1, 1, 1)
        self.open = QtWidgets.QPushButton(self)
        self.open.setGeometry(QtCore.QRect(160, 540, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.open.setFont(font)
        self.open.setObjectName("open")
        
        self.share = QtWidgets.QPushButton(self)
        self.share.setGeometry(QtCore.QRect(390, 540, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.share.setFont(font)
        self.share.setObjectName("share")

        self.show_table = QtWidgets.QTextEdit(self)
        self.show_table.setGeometry(QtCore.QRect(160, 40, 431, 271))
        self.show_table.setObjectName("show_table")
 

        self.gonder = QtWidgets.QPushButton(self)
        self.gonder.setGeometry(QtCore.QRect(460, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gonder.setFont(font)
        self.gonder.setObjectName("gonder")

        self.write_text = QtWidgets.QLineEdit(self)
        self.write_text.setGeometry(QtCore.QRect(160, 330, 431, 41))
        self.write_text.setObjectName("lineEdit")



        
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "IP ADRESS:"))
        self.label_2.setText(_translate("MainWindow", "PORT:"))
        self.open.setText(_translate("MainWindow", "Kameramı Aç"))
        self.share.setText(_translate("MainWindow", "Ekranımı Paylaş"))
        self.gonder.setText(_translate("MainWindow", "Gönder"))
        self.open.clicked.connect(self.start_camera_stream)
        self.share.clicked.connect(self.start_screen_sharing)
        import socket, time
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client_socket.connect(('4.tcp.eu.ngrok.io',10322))
                
        
        print(self.write_text.text())

        
      
        self.gonder.clicked.connect(self.yolla)
    def yolla(self):
                    def a():
                        self.show_table.append('Ben: ' +self.write_text.text() +'\n')
                        self.client_socket.send(str.encode(str(self.write_text.text()+' ')))
                        self.show_table.append('My Friend: ' + str(self.client_socket.recv(2048).decode())+'\n')
                    t22 = threading.Thread(target=a)
                    t22.start()
                    

    def start_camera_stream(self):
            camera_client = CameraClient(self.text_ip.text() ,int(self.port_ip.text()))
            t3 = threading.Thread(target=camera_client.start_stream)
            t3.start()

    def start_screen_sharing(self):
            screen_client = ScreenShareClient(self.text_ip.text(),int(self.port_ip.text()))
            t4 = threading.Thread(target=screen_client.start_stream)
            t4.start()
    
def window():
    app = QApplication(sys.argv) # bir app oluşturup sistemdeki arg leri attık # zetcode da bak
    win = MyWindow()
    
    win.show() # pencereyi başlattık
    sys.exit(app.exec_()) # pencereyi kapatabilmek için x tuşunu aktif hale getirdik

window()
