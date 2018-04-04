# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ussd_ui.ui'
#
# Created by: Ismael GraHms
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import urllib
import json
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(778, 731)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(760, 713))
        self.tabWidget.setMaximumSize(QtCore.QSize(760, 713))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setAutoFillBackground(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.call_btn = QtGui.QPushButton(self.tab)
        self.call_btn.setGeometry(QtCore.QRect(130, 533, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.call_btn.setFont(font)
        self.call_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.call_btn.setStyleSheet(_fromUtf8("QPushButton { color: white;\n"
"                        background: green \n"
"                        \n"
"                        }\n"
"QPushButton::menu-indicator {\n"
"subcontrol-origin: content;\n"
"subcontrol-position: right center;\n"
"position: absolute;\n"
"width: 20px;\n"
"top: 5px; right: 2px; bottom: 5px;\n"
"}\n"
"\n"
""))
        self.call_btn.setAutoDefault(False)
        self.call_btn.setDefault(False)
        self.call_btn.setFlat(False)
        self.call_btn.setObjectName(_fromUtf8("call_btn"))
        self.number_6 = QtGui.QPushButton(self.tab)
        self.number_6.setEnabled(True)
        self.number_6.setGeometry(QtCore.QRect(210, 350, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_6.setFont(font)
        self.number_6.setObjectName(_fromUtf8("number_6"))
        self.star_btn = QtGui.QPushButton(self.tab)
        self.star_btn.setGeometry(QtCore.QRect(50, 470, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.star_btn.setFont(font)
        self.star_btn.setObjectName(_fromUtf8("star_btn"))
        self.ussd_opt = QtGui.QLineEdit(self.tab)
        self.ussd_opt.setGeometry(QtCore.QRect(50, 260, 241, 31))
        self.ussd_opt.setFrame(False)
        self.ussd_opt.setObjectName(_fromUtf8("ussd_opt"))
        self.ussd_opt.setDisabled(True)
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(340, 200, 411, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 70, 281, 581))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(str(os.getcwd())+"/pictures/3e12c6f13043eaf1b03face4ebe3b9e6.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.cardinal = QtGui.QPushButton(self.tab)
        self.cardinal.setGeometry(QtCore.QRect(210, 470, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cardinal.setFont(font)
        self.cardinal.setObjectName(_fromUtf8("cardinal"))
        self.phone_number = QtGui.QLineEdit(self.tab)
        self.phone_number.setGeometry(QtCore.QRect(430, 180, 261, 20))
        self.phone_number.setEchoMode(QtGui.QLineEdit.Normal)
        self.phone_number.setDragEnabled(False)
        self.phone_number.setObjectName(_fromUtf8("phone_number"))
        self.number_3 = QtGui.QPushButton(self.tab)
        self.number_3.setGeometry(QtCore.QRect(210, 290, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_3.setFont(font)
        self.number_3.setObjectName(_fromUtf8("number_3"))
        self.number_1 = QtGui.QPushButton(self.tab)
        self.number_1.setGeometry(QtCore.QRect(50, 290, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_1.setFont(font)
        self.number_1.setStyleSheet(_fromUtf8("QPushButton{\n"
"\n"
"\n"
"}"))
        self.number_1.setObjectName(_fromUtf8("number_1"))
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(350, 180, 81, 16))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.ussd_io = QtGui.QLineEdit(self.tab)
        self.ussd_io.setGeometry(QtCore.QRect(50, 140, 241, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ussd_io.setFont(font)
        self.ussd_io.setText(_fromUtf8(""))
        self.ussd_io.setFrame(True)
        self.ussd_io.setAlignment(QtCore.Qt.AlignCenter)
        self.ussd_io.setReadOnly(False)
        self.ussd_io.setObjectName(_fromUtf8("ussd_io"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(450, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("QLabel{\n"
"\n"
"color: blue;\n"
"qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))\n"
"\n"
"}"))
        self.label_2.setTextFormat(QtCore.Qt.LogText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.number_8 = QtGui.QPushButton(self.tab)
        self.number_8.setGeometry(QtCore.QRect(130, 410, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_8.setFont(font)
        self.number_8.setObjectName(_fromUtf8("number_8"))
        self.number_7 = QtGui.QPushButton(self.tab)
        self.number_7.setGeometry(QtCore.QRect(50, 410, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_7.setFont(font)
        self.number_7.setObjectName(_fromUtf8("number_7"))
        self.numero_0 = QtGui.QPushButton(self.tab)
        self.numero_0.setGeometry(QtCore.QRect(130, 470, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numero_0.setFont(font)
        self.numero_0.setObjectName(_fromUtf8("numero_0"))
        self.number_2 = QtGui.QPushButton(self.tab)
        self.number_2.setGeometry(QtCore.QRect(130, 290, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_2.setFont(font)
        self.number_2.setObjectName(_fromUtf8("number_2"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(340, 80, 351, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("QLabel{\n"
"background: rgb(38, 255, 230)\n"
"qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 228, 209, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))\n"
"}"))
        self.label_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_15.setFrameShadow(QtGui.QFrame.Plain)
        self.label_15.setMidLineWidth(0)
        self.label_15.setTextFormat(QtCore.Qt.LogText)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(450, 230, 241, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox{\n"
"\n"
"background: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))\n"
"\n"
"\n"
"}"))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lac_line = QtGui.QLineEdit(self.groupBox)
        self.lac_line.setGeometry(QtCore.QRect(10, 70, 221, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lac_line.setFont(font)
        self.lac_line.setInputMask(_fromUtf8(""))
        self.lac_line.setText(_fromUtf8(""))
        self.lac_line.setFrame(True)
        self.lac_line.setDragEnabled(False)
        self.lac_line.setReadOnly(False)
        self.lac_line.setObjectName(_fromUtf8("lac_line"))
        self.cid_line = QtGui.QLineEdit(self.groupBox)
        self.cid_line.setGeometry(QtCore.QRect(10, 130, 221, 20))
        self.cid_line.setObjectName(_fromUtf8("cid_line"))
        self.mcc_line = QtGui.QLineEdit(self.groupBox)
        self.mcc_line.setGeometry(QtCore.QRect(10, 190, 221, 20))
        self.mcc_line.setObjectName(_fromUtf8("mcc_line"))
        self.msisdn_line = QtGui.QLineEdit(self.groupBox)
        self.msisdn_line.setGeometry(QtCore.QRect(10, 250, 221, 20))
        self.msisdn_line.setObjectName(_fromUtf8("msisdn_line"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 230, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 290, 81, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ussd_line = QtGui.QLineEdit(self.groupBox)
        self.ussd_line.setGeometry(QtCore.QRect(10, 320, 221, 20))
        self.ussd_line.setObjectName(_fromUtf8("ussd_line"))
        self.ussd_line.setDisabled(True)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 300, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic Light"))
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(490, 140, 161, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.call_btn_2 = QtGui.QPushButton(self.tab)
        self.call_btn_2.setGeometry(QtCore.QRect(210, 533, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.call_btn_2.setFont(font)
        self.call_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.call_btn_2.setStyleSheet(_fromUtf8("QPushButton { color: white;\n"
"                        background: red\n"
"                        \n"
"                        }\n"
"\n"
"\n"
""))
        self.call_btn_2.setAutoDefault(False)
        self.call_btn_2.setDefault(False)
        self.call_btn_2.setFlat(False)
        self.call_btn_2.clicked.connect(self.reset)
        self.call_btn_2.setObjectName(_fromUtf8("call_btn_2"))
        self.number_5 = QtGui.QPushButton(self.tab)
        self.number_5.setGeometry(QtCore.QRect(130, 350, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_5.setFont(font)
        self.number_5.setObjectName(_fromUtf8("number_5"))
        self.number_9 = QtGui.QPushButton(self.tab)
        self.number_9.setGeometry(QtCore.QRect(210, 410, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_9.setFont(font)
        self.number_9.setObjectName(_fromUtf8("number_9"))
        self.number_4 = QtGui.QPushButton(self.tab)
        self.number_4.setGeometry(QtCore.QRect(50, 350, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_4.setFont(font)
        self.number_4.setObjectName(_fromUtf8("number_4"))
        self.label.raise_()
        self.call_btn.raise_()
        self.number_6.raise_()
        self.star_btn.raise_()
        self.ussd_opt.raise_()
        self.line.raise_()
        self.cardinal.raise_()
        self.phone_number.raise_()
        self.number_3.raise_()
        self.number_1.raise_()
        self.label_17.raise_()
        self.ussd_io.raise_()
        self.label_2.raise_()
        self.number_8.raise_()
        self.number_7.raise_()
        self.numero_0.raise_()
        self.number_2.raise_()
        self.label_15.raise_()
        self.groupBox.raise_()
        self.label_16.raise_()
        self.call_btn_2.raise_()
        self.number_5.raise_()
        self.number_9.raise_()
        self.number_4.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 120, 751, 571))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.resquest_json_code = QtGui.QTextEdit(self.tab_3)
        self.resquest_json_code.setGeometry(QtCore.QRect(10, 10, 731, 521))
        self.resquest_json_code.setFrameShape(QtGui.QFrame.StyledPanel)
        self.resquest_json_code.setFrameShadow(QtGui.QFrame.Plain)
        self.resquest_json_code.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.resquest_json_code.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.resquest_json_code.setObjectName(_fromUtf8("resquest_XML_code"))

        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.comboBox = QtGui.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(630, 10, 111, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.line_2 = QtGui.QFrame(self.tab_4)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 731, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.code_generator_form = QtGui.QPlainTextEdit(self.tab_4)
        self.code_generator_form.setGeometry(QtCore.QRect(10, 80, 731, 461))
        self.code_generator_form.setAutoFillBackground(False)
        self.code_generator_form.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.code_generator_form.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.code_generator_form.setDocumentTitle(_fromUtf8(""))
        self.code_generator_form.setReadOnly(True)
        self.code_generator_form.setOverwriteMode(False)
        self.code_generator_form.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.code_generator_form.setObjectName(_fromUtf8("code_generator_form"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(450, 40, 301, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("QLabel{\n"
"background: rgb(38, 255, 230)\n"
"qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 228, 209, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))\n"
"}"))
        self.label_18.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_18.setFrameShadow(QtGui.QFrame.Plain)
        self.label_18.setMidLineWidth(0)
        self.label_18.setTextFormat(QtCore.Qt.LogText)
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(650, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("QLabel{\n"
"\n"
"color: blue;\n"
"qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))\n"
"\n"
"}"))
        self.label_19.setTextFormat(QtCore.Qt.LogText)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Larva USSD Simulator 1.0.1 Beta Editon", None))
        self.call_btn.setText(_translate("Form", "CALL", None))
        self.number_6.setText(_translate("Form", "6", None))
        self.star_btn.setText(_translate("Form", "*", None))
        self.cardinal.setText(_translate("Form", "#", None))
        self.number_3.setText(_translate("Form", "3", None))
        self.number_1.setText(_translate("Form", "1", None))
        self.label_17.setText(_translate("Form", "Phone Number", None))
        self.label_2.setText(_translate("Form", "LARVA ", None))
        self.number_8.setText(_translate("Form", "8", None))
        self.number_7.setText(_translate("Form", "7", None))
        self.numero_0.setText(_translate("Form", "0", None))
        self.number_2.setText(_translate("Form", "2", None))
        self.label_15.setText(_translate("Form", "USSD SIMULATOR", None))
        self.groupBox.setTitle(_translate("Form", "USSD REQEST DATA", None))
        self.label_3.setText(_translate("Form", "LAC", None))
        self.label_4.setText(_translate("Form", "CID", None))
        self.label_5.setText(_translate("Form", "MCC", None))
        self.label_6.setText(_translate("Form", "MSISDN", None))
        self.label_7.setText(_translate("Form", "Local area code", None))
        self.label_8.setText(_translate("Form", "Cell id", None))
        self.label_9.setText(_translate("Form", "Cell id", None))
        self.label_10.setText(_translate("Form", "Cell id", None))
        self.label_11.setText(_translate("Form", "Mobile country id", None))
        self.label_12.setText(_translate("Form", "Mobile subscriber ISDN", None))
        self.label_13.setText(_translate("Form", "INPUT USSD", None))
        self.label_14.setText(_translate("Form", " USSD code to be Executed", None))
        self.label_16.setText(_translate("Form", "DEVELOPED BY ISMAEL GRAHMS", None))
        self.call_btn_2.setText(_translate("Form", "Reset", None))
        self.number_5.setText(_translate("Form", "5", None))
        self.number_9.setText(_translate("Form", "9", None))
        self.number_4.setText(_translate("Form", "4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "USSD Test Flow", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Request Json Code", None))
        self.comboBox.setItemText(0, _translate("Form", "Choose Language ", None))
        self.comboBox.setItemText(1, _translate("Form", "PHP", None))
        self.comboBox.setItemText(2, _translate("Form", "Java", None))
        self.comboBox.setItemText(3, _translate("Form", "Python 2.7", None))
        self.comboBox.setItemText(4, _translate("Form", "C#", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Http Response Code", None))
        self.label_18.setText(_translate("Form", "USSD SIMULATOR", None))
        self.label_19.setText(_translate("Form", "LARVA ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "USSD Json Code", None))
        self.optionView = QtGui.QListView(self.tab)
        self.optionView.setGeometry(QtCore.QRect(50, 140, 241, 121))
        self.optionView.setObjectName(_fromUtf8("optionView"))
        self.optionView.close()

        # 1 ########################################

        self.number_1.clicked.connect(self.btnClicked1)
        self.number_2.clicked.connect(self.btnClicked2)
        self.number_3.clicked.connect(self.btnClicked3)
        self.number_4.clicked.connect(self.btnClicked4)
        self.number_5.clicked.connect(self.btnClicked5)
        self.number_6.clicked.connect(self.btnClicked6)
        self.number_7.clicked.connect(self.btnClicked7)
        self.number_8.clicked.connect(self.btnClicked8)
        self.number_9.clicked.connect(self.btnClicked9)
        self.numero_0.clicked.connect(self.btnClicked0)
        self.cardinal.clicked.connect(self.btnClickedCardinal)
        self.star_btn.clicked.connect(self.btnClickedStar)
        self.call_btn.clicked.connect(self.callBtn)

    def callBtn(self):
            if len(self.ussd_line.displayText())<=4:
                    if len(self.ussd_io.displayText()) > 0:
                            self.ussd_line.setText(str(self.ussd_io.displayText()))
                            self.ussd_line.setDisabled(True)
                            self.ussd_io.setDisabled(True)
                            self.ussd_opt.setDisabled(False)
                            self.display_ussd = True
                            if len(self.phone_number.displayText())<=0:
                                    self.ussd_io.setText('WASP')
                                    self.ussd_opt.setText('You forgot to type phone number, press reset')
                                    self.ussd_opt.setDisabled(True)

                            else:
                                    self.get_ussd_opt()
                                    self.ussd_opt.setText('')





    def btnClicked1(self):
            number = str(self.number_1.text())
            if len(self.ussd_line.displayText())>0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)




    def btnClicked2(self):
            number = str(self.number_2.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked3(self):
            number = str(self.number_3.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked4(self):
            number = str(self.number_4.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked5(self):
            number = str(self.number_5.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked6(self):
            number = str(self.number_6.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked7(self):
            number = str(self.number_7.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked8(self):
            number = str(self.number_8.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked9(self):
            number = str(self.number_9.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClicked0(self):
            number = str(self.numero_0.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClickedStar(self):
            number = str(self.star_btn.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)

    def btnClickedCardinal(self):
            number = str(self.cardinal.text())
            if len(self.ussd_line.displayText()) > 0:
                    self.ussd_opt.insert(str(number))
            else:
                    self.ussd_io.insert(number)
    def reset(self):
            self.ussd_line.setText('')
            self.ussd_io.setDisabled(False)
            self.ussd_opt.setDisabled(True)
            self.ussd_io.setText('')
            self.optionView.close()
            self.ussd_opt.setText('')






        # THIS IS WAY THE MAGIC HAPPENS



    def get_ussd_opt(self):

            # Create a ListView

            ########

            # Creating a model for the list



            # Activating the listview

            if str(self.ussd_line.displayText())=='*911#':
                    self.ussd_io.setText('')
                    self.ussd_io.setDisabled(True)
                    self.optionView.setDisabled(False)

                    self.optionView.raise_()
                    ############### Models ################################
                    model = QtGui.QStandardItemModel(self.optionView)
                    #item = QtGui.QStandardItem()
                    numero_cell = self.phone_number.displayText()
                    session = 'main'
                    input = self.ussd_opt.displayText()
                    url = 'http://localhost/larvaussd/ussd_response.php?sessionId=' + session + '&msisdn=' + numero_cell + '&input='+input+''
                    response = urllib.urlopen(url)
                    data = json.loads(response.read())
                    print data
                    items = data['Menu-Inicial' ]



                    options = len(items)
                    x = 1
                    #self.stgs = 1
                    #items = self.options(y)
                    for item in items:
                            QtGui.QStandardItem(item)
                            model.appendRow(QtGui.QStandardItem(str(x)+' '+item))


                            x += 1
                    self.optionView.setModel(model)
                    self.optionView.show()
                    self.stage = 1


            else:
                    self.ussd_opt.setText('incorrect USSD code, press reset')
                    self.ussd_io.setText('WASP')

                    self.ussd_opt.setDisabled(True)


   # '''
    def option(self,request, chosen, stage):
            options = [[' Consultar recarga',  # Must be store-bought
                        ' Consultar Numero',  # Must be homemade
                        ' Ligar pra namorada',  # Must be saucy
                        ' Falar com Guebuza',  # Must be spicy
                        ' Explodir o pais'],
                       # Fisrt Options
                       ['848255237', 'Go Back'],
                       # second options
                       ['1 Numero de amor'], ['voltar']]
            if  stage == '1':
                    return ( options[int(request)-1], chosen)
            if stage == '2':
                    return (options[chosen][int(request)-1])
            if stage == '3':
                    return (options[0][chosen][int(request)-1],chosen)








#'''
##################################################################################


#import myres_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

