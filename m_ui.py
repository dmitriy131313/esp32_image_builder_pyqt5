# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 211)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_proj_dir = QtWidgets.QPushButton(self.centralwidget)
        self.button_proj_dir.setEnabled(True)
        self.button_proj_dir.setGeometry(QtCore.QRect(20, 20, 121, 61))
        self.button_proj_dir.setObjectName("button_proj_dir")
        self.button_make = QtWidgets.QPushButton(self.centralwidget)
        self.button_make.setEnabled(False)
        self.button_make.setGeometry(QtCore.QRect(20, 90, 121, 61))
        self.button_make.setObjectName("button_make")
        self.label_bl_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_bl_offset.setGeometry(QtCore.QRect(150, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_bl_offset.setFont(font)
        self.label_bl_offset.setObjectName("label_bl_offset")
        self.label_bl_size = QtWidgets.QLabel(self.centralwidget)
        self.label_bl_size.setGeometry(QtCore.QRect(150, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_bl_size.setFont(font)
        self.label_bl_size.setObjectName("label_bl_size")
        self.text_bl_offset = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_bl_offset.setGeometry(QtCore.QRect(330, 20, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_bl_offset.setFont(font)
        self.text_bl_offset.setObjectName("text_bl_offset")
        self.text_bl_size = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_bl_size.setGeometry(QtCore.QRect(330, 60, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_bl_size.setFont(font)
        self.text_bl_size.setObjectName("text_bl_size")
        self.label_pt_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_pt_offset.setGeometry(QtCore.QRect(150, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pt_offset.setFont(font)
        self.label_pt_offset.setObjectName("label_pt_offset")
        self.text_pt_offset = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_pt_offset.setGeometry(QtCore.QRect(330, 100, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_pt_offset.setFont(font)
        self.text_pt_offset.setObjectName("text_pt_offset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_proj_dir.setText(_translate("MainWindow", "Set Project Dir"))
        self.button_make.setText(_translate("MainWindow", "Make binary"))
        self.label_bl_offset.setText(_translate("MainWindow", "Bootloader OFFSET:"))
        self.label_bl_size.setText(_translate("MainWindow", "Bootloader SIZE:"))
        self.text_bl_offset.setPlainText(_translate("MainWindow", "0x1000"))
        self.text_bl_size.setPlainText(_translate("MainWindow", "0x7000"))
        self.label_pt_offset.setText(_translate("MainWindow", "Partition table OFFSET:"))
        self.text_pt_offset.setPlainText(_translate("MainWindow", "0x8000"))