# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgOpportunities.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgOpportunities(object):
    def setupUi(self, wdgOpportunities):
        wdgOpportunities.setObjectName("wdgOpportunities")
        wdgOpportunities.resize(656, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/bank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgOpportunities.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(wdgOpportunities)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl = QtWidgets.QLabel(wdgOpportunities)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_2.addWidget(self.lbl)
        self.tabWidget = QtWidgets.QTabWidget(wdgOpportunities)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.wdgYear = wdgYear(self.tab)
        self.wdgYear.setObjectName("wdgYear")
        self.horizontalLayout.addWidget(self.wdgYear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cmbMode = QtWidgets.QComboBox(self.tab)
        self.cmbMode.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbMode.setObjectName("cmbMode")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbMode.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/expired.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbMode.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbMode.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbMode.addItem(icon4, "")
        self.horizontalLayout_2.addWidget(self.cmbMode)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tblOpportunities = myQTableWidget(self.tab)
        self.tblOpportunities.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblOpportunities.setAlternatingRowColors(True)
        self.tblOpportunities.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblOpportunities.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblOpportunities.setObjectName("tblOpportunities")
        self.tblOpportunities.setColumnCount(0)
        self.tblOpportunities.setRowCount(0)
        self.tblOpportunities.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblOpportunities)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.actionOpportunityNew = QtWidgets.QAction(wdgOpportunities)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpportunityNew.setIcon(icon6)
        self.actionOpportunityNew.setObjectName("actionOpportunityNew")
        self.actionOpportunityDelete = QtWidgets.QAction(wdgOpportunities)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpportunityDelete.setIcon(icon7)
        self.actionOpportunityDelete.setObjectName("actionOpportunityDelete")
        self.actionOpportunityEdit = QtWidgets.QAction(wdgOpportunities)
        self.actionOpportunityEdit.setIcon(icon5)
        self.actionOpportunityEdit.setObjectName("actionOpportunityEdit")
        self.actionExecute = QtWidgets.QAction(wdgOpportunities)
        self.actionExecute.setIcon(icon3)
        self.actionExecute.setObjectName("actionExecute")
        self.actionRemove = QtWidgets.QAction(wdgOpportunities)
        self.actionRemove.setIcon(icon2)
        self.actionRemove.setObjectName("actionRemove")
        self.actionShowGraphic = QtWidgets.QAction(wdgOpportunities)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/curiosity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowGraphic.setIcon(icon8)
        self.actionShowGraphic.setObjectName("actionShowGraphic")

        self.retranslateUi(wdgOpportunities)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgOpportunities)

    def retranslateUi(self, wdgOpportunities):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgOpportunities", "Opportunities list"))
        self.cmbMode.setItemText(0, _translate("wdgOpportunities", "Show current opportunities"))
        self.cmbMode.setItemText(1, _translate("wdgOpportunities", "Show removed opportunities"))
        self.cmbMode.setItemText(2, _translate("wdgOpportunities", "Show executed opportunities"))
        self.cmbMode.setItemText(3, _translate("wdgOpportunities", "Show all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("wdgOpportunities", "Opportunity annotations list"))
        self.actionOpportunityNew.setText(_translate("wdgOpportunities", "New purchase opportunity"))
        self.actionOpportunityNew.setToolTip(_translate("wdgOpportunities", "New purchase opportunity"))
        self.actionOpportunityDelete.setText(_translate("wdgOpportunities", "Delete purchase opportunity"))
        self.actionOpportunityDelete.setToolTip(_translate("wdgOpportunities", "Delete purchase opportunity"))
        self.actionOpportunityEdit.setText(_translate("wdgOpportunities", "Edit purchase opportunity"))
        self.actionOpportunityEdit.setToolTip(_translate("wdgOpportunities", "Edit purchase opportunity"))
        self.actionExecute.setText(_translate("wdgOpportunities", "Execute opportunity"))
        self.actionExecute.setToolTip(_translate("wdgOpportunities", "Execute opportunity"))
        self.actionRemove.setText(_translate("wdgOpportunities", "Remove opportunity"))
        self.actionRemove.setToolTip(_translate("wdgOpportunities", "Remove opportunity"))
        self.actionShowGraphic.setText(_translate("wdgOpportunities", "Show Purchase graphic"))
        self.actionShowGraphic.setToolTip(_translate("wdgOpportunities", "Show Purchase graphic"))

from xulpymoney.ui.myqtablewidget import myQTableWidget
from xulpymoney.ui.wdgYear import wdgYear
import xulpymoney.images.xulpymoney_rc
