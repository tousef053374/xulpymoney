# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmDPSAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmDPSAdd(object):
    def setupUi(self, frmDPSAdd):
        frmDPSAdd.setObjectName("frmDPSAdd")
        frmDPSAdd.setWindowModality(QtCore.Qt.ApplicationModal)
        frmDPSAdd.resize(740, 406)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/dividends.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmDPSAdd.setWindowIcon(icon)
        frmDPSAdd.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(frmDPSAdd)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(frmDPSAdd)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color: rgb(0, 192, 0);")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(frmDPSAdd)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.calendar = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout_4.addWidget(self.calendar)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(frmDPSAdd)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.calendarPay = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarPay.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarPay.setObjectName("calendarPay")
        self.horizontalLayout_5.addWidget(self.calendarPay)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(frmDPSAdd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtGross = myQLineEdit(frmDPSAdd)
        self.txtGross.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtGross.setObjectName("txtGross")
        self.horizontalLayout_2.addWidget(self.txtGross)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cmd = QtWidgets.QPushButton(frmDPSAdd)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon1)
        self.cmd.setObjectName("cmd")
        self.verticalLayout.addWidget(self.cmd)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(frmDPSAdd)
        QtCore.QMetaObject.connectSlotsByName(frmDPSAdd)
        frmDPSAdd.setTabOrder(self.txtGross, self.cmd)

    def retranslateUi(self, frmDPSAdd):
        _translate = QtCore.QCoreApplication.translate
        frmDPSAdd.setWindowTitle(_translate("frmDPSAdd", "New DPS"))
        self.groupBox.setTitle(_translate("frmDPSAdd", "Dividend date"))
        self.groupBox_2.setTitle(_translate("frmDPSAdd", "Dividend pay date"))
        self.label_2.setText(_translate("frmDPSAdd", "DPS gross"))
        self.txtGross.setText(_translate("frmDPSAdd", "0"))
        self.cmd.setText(_translate("frmDPSAdd", "Save DPS"))
from xulpymoney.ui.myqlineedit import myQLineEdit
import xulpymoney.images.xulpymoney_rc
