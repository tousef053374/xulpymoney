# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmSellingPoint.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmSellingPoint(object):
    def setupUi(self, frmSellingPoint):
        frmSellingPoint.setObjectName("frmSellingPoint")
        frmSellingPoint.setWindowModality(QtCore.Qt.WindowModal)
        frmSellingPoint.resize(790, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSellingPoint.setWindowIcon(icon)
        frmSellingPoint.setSizeGripEnabled(True)
        frmSellingPoint.setModal(True)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(frmSellingPoint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTitulo = QtWidgets.QLabel(frmSellingPoint)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_3.addWidget(self.lblTitulo)
        self.groupBox = QtWidgets.QGroupBox(frmSellingPoint)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radTPC = QtWidgets.QRadioButton(self.groupBox)
        self.radTPC.setChecked(True)
        self.radTPC.setObjectName("radTPC")
        self.horizontalLayout_2.addWidget(self.radTPC)
        self.cmbTPC = QtWidgets.QComboBox(self.groupBox)
        self.cmbTPC.setObjectName("cmbTPC")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.cmbTPC.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbTPC)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radGain = QtWidgets.QRadioButton(self.groupBox)
        self.radGain.setObjectName("radGain")
        self.horizontalLayout.addWidget(self.radGain)
        self.txtGanancia = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtGanancia.sizePolicy().hasHeightForWidth())
        self.txtGanancia.setSizePolicy(sizePolicy)
        self.txtGanancia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtGanancia.setObjectName("txtGanancia")
        self.horizontalLayout.addWidget(self.txtGanancia)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radPrice = QtWidgets.QRadioButton(self.groupBox)
        self.radPrice.setObjectName("radPrice")
        self.horizontalLayout_8.addWidget(self.radPrice)
        self.txtPrice = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPrice.sizePolicy().hasHeightForWidth())
        self.txtPrice.setSizePolicy(sizePolicy)
        self.txtPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtPrice.setObjectName("txtPrice")
        self.horizontalLayout_8.addWidget(self.txtPrice)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(frmSellingPoint)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chkGainsTime = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkGainsTime.setObjectName("chkGainsTime")
        self.verticalLayout_2.addWidget(self.chkGainsTime)
        self.chkPonderanAll = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkPonderanAll.setObjectName("chkPonderanAll")
        self.verticalLayout_2.addWidget(self.chkPonderanAll)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.tab = QtWidgets.QTabWidget(frmSellingPoint)
        self.tab.setObjectName("tab")
        self.tab_current = QtWidgets.QWidget()
        self.tab_current.setObjectName("tab_current")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_current)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table = myQTableWidget(self.tab_current)
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.table.verticalHeader().setVisible(False)
        self.horizontalLayout_5.addWidget(self.table)
        self.tab.addTab(self.tab_current, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableSP = myQTableWidget(self.tab_2)
        self.tableSP.setObjectName("tableSP")
        self.tableSP.setColumnCount(7)
        self.tableSP.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSP.setHorizontalHeaderItem(6, item)
        self.tableSP.verticalHeader().setVisible(False)
        self.horizontalLayout_6.addWidget(self.tableSP)
        self.tab.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tab)
        self.cmd = QtWidgets.QPushButton(frmSellingPoint)
        self.cmd.setObjectName("cmd")
        self.verticalLayout_3.addWidget(self.cmd)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.retranslateUi(frmSellingPoint)
        self.cmbTPC.setCurrentIndex(2)
        self.tab.setCurrentIndex(0)
        self.txtGanancia.textEdited['QString'].connect(self.radGain.toggle)
        self.cmbTPC.currentIndexChanged['QString'].connect(self.radTPC.toggle)
        QtCore.QMetaObject.connectSlotsByName(frmSellingPoint)

    def retranslateUi(self, frmSellingPoint):
        _translate = QtCore.QCoreApplication.translate
        frmSellingPoint.setWindowTitle(_translate("frmSellingPoint", "Selling point calculation"))
        self.lblTitulo.setText(_translate("frmSellingPoint", "Selling point calculation"))
        self.groupBox.setTitle(_translate("frmSellingPoint", "Select your gain"))
        self.radTPC.setText(_translate("frmSellingPoint", "Select a &gain percentage"))
        self.cmbTPC.setItemText(0, _translate("frmSellingPoint", "2.5 %"))
        self.cmbTPC.setItemText(1, _translate("frmSellingPoint", "5 %"))
        self.cmbTPC.setItemText(2, _translate("frmSellingPoint", "7.5 %"))
        self.cmbTPC.setItemText(3, _translate("frmSellingPoint", "10 %"))
        self.cmbTPC.setItemText(4, _translate("frmSellingPoint", "15 %"))
        self.cmbTPC.setItemText(5, _translate("frmSellingPoint", "20 %"))
        self.cmbTPC.setItemText(6, _translate("frmSellingPoint", "25 %"))
        self.radGain.setText(_translate("frmSellingPoint", "Se&lect a gain amount"))
        self.txtGanancia.setToolTip(_translate("frmSellingPoint", "Select a gain amount"))
        self.txtGanancia.setText(_translate("frmSellingPoint", "1000"))
        self.radPrice.setText(_translate("frmSellingPoint", "Selec&t a price"))
        self.txtPrice.setText(_translate("frmSellingPoint", "10"))
        self.groupBox_2.setTitle(_translate("frmSellingPoint", "Selling point calculation options"))
        self.chkGainsTime.setText(_translate("frmSellingPoint", "Remove operations less than a year"))
        self.chkPonderanAll.setText(_translate("frmSellingPoint", "Include shares of the same product from different investments"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("frmSellingPoint", "Date"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("frmSellingPoint", "Investment (Bank)"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("frmSellingPoint", "Operation type"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("frmSellingPoint", "Shares"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("frmSellingPoint", "Bought price"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("frmSellingPoint", "Invested"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("frmSellingPoint", "Pending"))
        self.tab.setTabText(self.tab.indexOf(self.tab_current), _translate("frmSellingPoint", "Current state"))
        item = self.tableSP.horizontalHeaderItem(0)
        item.setText(_translate("frmSellingPoint", "Date"))
        item = self.tableSP.horizontalHeaderItem(1)
        item.setText(_translate("frmSellingPoint", "Investment (Bank)"))
        item = self.tableSP.horizontalHeaderItem(2)
        item.setText(_translate("frmSellingPoint", "Operation type"))
        item = self.tableSP.horizontalHeaderItem(3)
        item.setText(_translate("frmSellingPoint", "Shares"))
        item = self.tableSP.horizontalHeaderItem(4)
        item.setText(_translate("frmSellingPoint", "Price"))
        item = self.tableSP.horizontalHeaderItem(5)
        item.setText(_translate("frmSellingPoint", "Invested"))
        item = self.tableSP.horizontalHeaderItem(6)
        item.setText(_translate("frmSellingPoint", "Pending"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("frmSellingPoint", "Selling point state"))
        self.cmd.setText(_translate("frmSellingPoint", "Set the selling point"))

from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.myqtablewidget import myQTableWidget
import xulpymoney.images.xulpymoney_rc
