# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/frmInvestmentReport.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmInvestmentReport(object):
    def setupUi(self, frmInvestmentReport):
        frmInvestmentReport.setObjectName("frmInvestmentReport")
        frmInvestmentReport.setWindowModality(QtCore.Qt.WindowModal)
        frmInvestmentReport.resize(860, 539)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/report2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmInvestmentReport.setWindowIcon(icon)
        frmInvestmentReport.setModal(True)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(frmInvestmentReport)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lblTitulo = QtWidgets.QLabel(frmInvestmentReport)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 128, 0);")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout_9.addWidget(self.lblTitulo)
        self.tab = QtWidgets.QTabWidget(frmInvestmentReport)
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cmbAccount = QtWidgets.QComboBox(self.groupBox)
        self.cmbAccount.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cmbAccount.setObjectName("cmbAccount")
        self.horizontalLayout_2.addWidget(self.cmbAccount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txtInvestment = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInvestment.sizePolicy().hasHeightForWidth())
        self.txtInvestment.setSizePolicy(sizePolicy)
        self.txtInvestment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtInvestment.setObjectName("txtInvestment")
        self.horizontalLayout_3.addWidget(self.txtInvestment)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ise = wdgProductSelector(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ise.sizePolicy().hasHeightForWidth())
        self.ise.setSizePolicy(sizePolicy)
        self.ise.setObjectName("ise")
        self.horizontalLayout_8.addWidget(self.ise)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.txtVenta = myQLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtVenta.sizePolicy().hasHeightForWidth())
        self.txtVenta.setSizePolicy(sizePolicy)
        self.txtVenta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtVenta.setObjectName("txtVenta")
        self.horizontalLayout_5.addWidget(self.txtVenta)
        self.cmdPuntoVenta = QtWidgets.QToolButton(self.groupBox)
        self.cmdPuntoVenta.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdPuntoVenta.setIcon(icon1)
        self.cmdPuntoVenta.setObjectName("cmdPuntoVenta")
        self.horizontalLayout_5.addWidget(self.cmdPuntoVenta)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.chkExpiration = QtWidgets.QCheckBox(self.groupBox)
        self.chkExpiration.setChecked(True)
        self.chkExpiration.setObjectName("chkExpiration")
        self.horizontalLayout_10.addWidget(self.chkExpiration)
        self.cmdToday = QtWidgets.QToolButton(self.groupBox)
        self.cmdToday.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/today.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdToday.setIcon(icon2)
        self.cmdToday.setIconSize(QtCore.QSize(32, 32))
        self.cmdToday.setObjectName("cmdToday")
        self.horizontalLayout_10.addWidget(self.cmdToday)
        self.calExpiration = QtWidgets.QCalendarWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calExpiration.sizePolicy().hasHeightForWidth())
        self.calExpiration.setSizePolicy(sizePolicy)
        self.calExpiration.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calExpiration.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calExpiration.setObjectName("calExpiration")
        self.horizontalLayout_10.addWidget(self.calExpiration)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.cmdInvestment = QtWidgets.QPushButton(self.groupBox)
        self.cmdInvestment.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdInvestment.setIcon(icon3)
        self.cmdInvestment.setObjectName("cmdInvestment")
        self.verticalLayout.addWidget(self.cmdInvestment)
        self.horizontalLayout_14.addLayout(self.verticalLayout)
        self.horizontalLayout_12.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/xulpymoney/bundle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_12, icon4, "")
        self.tabInvestmentCurrent = QtWidgets.QWidget()
        self.tabInvestmentCurrent.setObjectName("tabInvestmentCurrent")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabInvestmentCurrent)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.grpCurrentInvestmentCurrency = QtWidgets.QGroupBox(self.tabInvestmentCurrent)
        self.grpCurrentInvestmentCurrency.setObjectName("grpCurrentInvestmentCurrency")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.grpCurrentInvestmentCurrency)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tblInvestmentCurrent = myQTableWidget(self.grpCurrentInvestmentCurrency)
        self.tblInvestmentCurrent.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentCurrent.setAlternatingRowColors(True)
        self.tblInvestmentCurrent.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInvestmentCurrent.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblInvestmentCurrent.setObjectName("tblInvestmentCurrent")
        self.tblInvestmentCurrent.setColumnCount(0)
        self.tblInvestmentCurrent.setRowCount(0)
        self.tblInvestmentCurrent.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tblInvestmentCurrent)
        self.verticalLayout_11.addWidget(self.grpCurrentInvestmentCurrency)
        self.grpCurrentAccountCurrency = QtWidgets.QGroupBox(self.tabInvestmentCurrent)
        self.grpCurrentAccountCurrency.setObjectName("grpCurrentAccountCurrency")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.grpCurrentAccountCurrency)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tblInvestmentCurrentAccountCurrency = myQTableWidget(self.grpCurrentAccountCurrency)
        self.tblInvestmentCurrentAccountCurrency.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentCurrentAccountCurrency.setAlternatingRowColors(True)
        self.tblInvestmentCurrentAccountCurrency.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblInvestmentCurrentAccountCurrency.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblInvestmentCurrentAccountCurrency.setObjectName("tblInvestmentCurrentAccountCurrency")
        self.tblInvestmentCurrentAccountCurrency.setColumnCount(0)
        self.tblInvestmentCurrentAccountCurrency.setRowCount(0)
        self.tblInvestmentCurrentAccountCurrency.verticalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.tblInvestmentCurrentAccountCurrency)
        self.verticalLayout_11.addWidget(self.grpCurrentAccountCurrency)
        self.lblAge = QtWidgets.QLabel(self.tabInvestmentCurrent)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblAge.setFont(font)
        self.lblAge.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAge.setObjectName("lblAge")
        self.verticalLayout_11.addWidget(self.lblAge)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/xulpymoney/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabInvestmentCurrent, icon5, "")
        self.tabOperacionesHistoricas = QtWidgets.QWidget()
        self.tabOperacionesHistoricas.setObjectName("tabOperacionesHistoricas")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tabOperacionesHistoricas)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chkOperaciones = QtWidgets.QCheckBox(self.tabOperacionesHistoricas)
        self.chkOperaciones.setObjectName("chkOperaciones")
        self.verticalLayout_7.addWidget(self.chkOperaciones)
        self.grpOperationsInvestmentCurrency = QtWidgets.QGroupBox(self.tabOperacionesHistoricas)
        self.grpOperationsInvestmentCurrency.setObjectName("grpOperationsInvestmentCurrency")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.grpOperationsInvestmentCurrency)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tblOperations = myQTableWidget(self.grpOperationsInvestmentCurrency)
        self.tblOperations.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblOperations.setAlternatingRowColors(True)
        self.tblOperations.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblOperations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblOperations.setObjectName("tblOperations")
        self.tblOperations.setColumnCount(0)
        self.tblOperations.setRowCount(0)
        self.tblOperations.verticalHeader().setVisible(False)
        self.horizontalLayout_9.addWidget(self.tblOperations)
        self.verticalLayout_7.addWidget(self.grpOperationsInvestmentCurrency)
        self.grpOperationsAccountCurrency = QtWidgets.QGroupBox(self.tabOperacionesHistoricas)
        self.grpOperationsAccountCurrency.setObjectName("grpOperationsAccountCurrency")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.grpOperationsAccountCurrency)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tblOperationsAccountCurrency = myQTableWidget(self.grpOperationsAccountCurrency)
        self.tblOperationsAccountCurrency.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblOperationsAccountCurrency.setAlternatingRowColors(True)
        self.tblOperationsAccountCurrency.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblOperationsAccountCurrency.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblOperationsAccountCurrency.setObjectName("tblOperationsAccountCurrency")
        self.tblOperationsAccountCurrency.setColumnCount(0)
        self.tblOperationsAccountCurrency.setRowCount(0)
        self.tblOperationsAccountCurrency.verticalHeader().setVisible(False)
        self.horizontalLayout_16.addWidget(self.tblOperationsAccountCurrency)
        self.verticalLayout_7.addWidget(self.grpOperationsAccountCurrency)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.tab.addTab(self.tabOperacionesHistoricas, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.grpHistoricalInvestmentCurrency = QtWidgets.QGroupBox(self.tab_2)
        self.grpHistoricalInvestmentCurrency.setObjectName("grpHistoricalInvestmentCurrency")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.grpHistoricalInvestmentCurrency)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tblInvestmentHistorical = myQTableWidget(self.grpHistoricalInvestmentCurrency)
        self.tblInvestmentHistorical.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentHistorical.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInvestmentHistorical.setAlternatingRowColors(True)
        self.tblInvestmentHistorical.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentHistorical.setObjectName("tblInvestmentHistorical")
        self.tblInvestmentHistorical.setColumnCount(0)
        self.tblInvestmentHistorical.setRowCount(0)
        self.tblInvestmentHistorical.verticalHeader().setVisible(False)
        self.verticalLayout_12.addWidget(self.tblInvestmentHistorical)
        self.verticalLayout_14.addWidget(self.grpHistoricalInvestmentCurrency)
        self.grpHistoricalAccountCurrency = QtWidgets.QGroupBox(self.tab_2)
        self.grpHistoricalAccountCurrency.setObjectName("grpHistoricalAccountCurrency")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.grpHistoricalAccountCurrency)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tblInvestmentHistoricalAccountCurrency = myQTableWidget(self.grpHistoricalAccountCurrency)
        self.tblInvestmentHistoricalAccountCurrency.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblInvestmentHistoricalAccountCurrency.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblInvestmentHistoricalAccountCurrency.setAlternatingRowColors(True)
        self.tblInvestmentHistoricalAccountCurrency.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tblInvestmentHistoricalAccountCurrency.setObjectName("tblInvestmentHistoricalAccountCurrency")
        self.tblInvestmentHistoricalAccountCurrency.setColumnCount(0)
        self.tblInvestmentHistoricalAccountCurrency.setRowCount(0)
        self.tblInvestmentHistoricalAccountCurrency.verticalHeader().setVisible(False)
        self.verticalLayout_13.addWidget(self.tblInvestmentHistoricalAccountCurrency)
        self.verticalLayout_14.addWidget(self.grpHistoricalAccountCurrency)
        self.horizontalLayout_4.addLayout(self.verticalLayout_14)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/xulpymoney/history2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_2, icon6, "")
        self.tabDividends = QtWidgets.QWidget()
        self.tabDividends.setObjectName("tabDividends")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tabDividends)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.chkHistoricalDividends = QtWidgets.QCheckBox(self.tabDividends)
        self.chkHistoricalDividends.setObjectName("chkHistoricalDividends")
        self.verticalLayout_16.addWidget(self.chkHistoricalDividends)
        self.grpDividendsInvestmentCurrency = QtWidgets.QGroupBox(self.tabDividends)
        self.grpDividendsInvestmentCurrency.setObjectName("grpDividendsInvestmentCurrency")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grpDividendsInvestmentCurrency)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tblDividends = myQTableWidget(self.grpDividendsInvestmentCurrency)
        self.tblDividends.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblDividends.setAlternatingRowColors(True)
        self.tblDividends.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblDividends.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblDividends.setObjectName("tblDividends")
        self.tblDividends.setColumnCount(0)
        self.tblDividends.setRowCount(0)
        self.tblDividends.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tblDividends)
        self.verticalLayout_16.addWidget(self.grpDividendsInvestmentCurrency)
        self.grpDividendsAccountCurrency = QtWidgets.QGroupBox(self.tabDividends)
        self.grpDividendsAccountCurrency.setObjectName("grpDividendsAccountCurrency")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.grpDividendsAccountCurrency)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tblDividendsAccountCurrency = myQTableWidget(self.grpDividendsAccountCurrency)
        self.tblDividendsAccountCurrency.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblDividendsAccountCurrency.setAlternatingRowColors(True)
        self.tblDividendsAccountCurrency.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblDividendsAccountCurrency.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblDividendsAccountCurrency.setObjectName("tblDividendsAccountCurrency")
        self.tblDividendsAccountCurrency.setColumnCount(0)
        self.tblDividendsAccountCurrency.setRowCount(0)
        self.tblDividendsAccountCurrency.verticalHeader().setVisible(False)
        self.verticalLayout_15.addWidget(self.tblDividendsAccountCurrency)
        self.verticalLayout_16.addWidget(self.grpDividendsAccountCurrency)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.grpDividendsEstimation = QtWidgets.QGroupBox(self.tabDividends)
        self.grpDividendsEstimation.setObjectName("grpDividendsEstimation")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.grpDividendsEstimation)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblDivAnualEstimado = QtWidgets.QLabel(self.grpDividendsEstimation)
        self.lblDivAnualEstimado.setObjectName("lblDivAnualEstimado")
        self.verticalLayout_2.addWidget(self.lblDivAnualEstimado)
        self.lblDivFechaRevision = QtWidgets.QLabel(self.grpDividendsEstimation)
        self.lblDivFechaRevision.setObjectName("lblDivFechaRevision")
        self.verticalLayout_2.addWidget(self.lblDivFechaRevision)
        self.lblDivSaldoEstimado = QtWidgets.QLabel(self.grpDividendsEstimation)
        self.lblDivSaldoEstimado.setObjectName("lblDivSaldoEstimado")
        self.verticalLayout_2.addWidget(self.lblDivSaldoEstimado)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.grpDividendsEstimation)
        self.grpDividendsEfectivos = QtWidgets.QGroupBox(self.tabDividends)
        self.grpDividendsEfectivos.setObjectName("grpDividendsEfectivos")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.grpDividendsEfectivos)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblDivTPC = QtWidgets.QLabel(self.grpDividendsEfectivos)
        self.lblDivTPC.setObjectName("lblDivTPC")
        self.verticalLayout_3.addWidget(self.lblDivTPC)
        self.lblDivTAE = QtWidgets.QLabel(self.grpDividendsEfectivos)
        self.lblDivTAE.setObjectName("lblDivTAE")
        self.verticalLayout_3.addWidget(self.lblDivTAE)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addWidget(self.grpDividendsEfectivos)
        self.verticalLayout_16.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_16)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/dividends.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabDividends, icon7, "")
        self.tabContracts = QtWidgets.QWidget()
        self.tabContracts.setObjectName("tabContracts")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tabContracts)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.chkHistoricalContracts = QtWidgets.QCheckBox(self.tabContracts)
        self.chkHistoricalContracts.setObjectName("chkHistoricalContracts")
        self.verticalLayout_17.addWidget(self.chkHistoricalContracts)
        self.grpHlContracts = QtWidgets.QGroupBox(self.tabContracts)
        self.grpHlContracts.setObjectName("grpHlContracts")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.grpHlContracts)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tblHlContracts = myQTableWidget(self.grpHlContracts)
        self.tblHlContracts.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblHlContracts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblHlContracts.setAlternatingRowColors(True)
        self.tblHlContracts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblHlContracts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblHlContracts.setObjectName("tblHlContracts")
        self.tblHlContracts.setColumnCount(0)
        self.tblHlContracts.setRowCount(0)
        self.tblHlContracts.verticalHeader().setVisible(False)
        self.horizontalLayout_18.addWidget(self.tblHlContracts)
        self.verticalLayout_17.addWidget(self.grpHlContracts)
        self.horizontalLayout_19.addLayout(self.verticalLayout_17)
        self.tab.addTab(self.tabContracts, icon6, "")
        self.verticalLayout_9.addWidget(self.tab)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.actionOperationAdd = QtWidgets.QAction(frmInvestmentReport)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/xulpymoney/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOperationAdd.setIcon(icon8)
        self.actionOperationAdd.setObjectName("actionOperationAdd")
        self.actionOperationDelete = QtWidgets.QAction(frmInvestmentReport)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/xulpymoney/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOperationDelete.setIcon(icon9)
        self.actionOperationDelete.setObjectName("actionOperationDelete")
        self.actionDividendAdd = QtWidgets.QAction(frmInvestmentReport)
        self.actionDividendAdd.setIcon(icon8)
        self.actionDividendAdd.setObjectName("actionDividendAdd")
        self.actionDividendRemove = QtWidgets.QAction(frmInvestmentReport)
        self.actionDividendRemove.setIcon(icon9)
        self.actionDividendRemove.setObjectName("actionDividendRemove")
        self.actionOperationEdit = QtWidgets.QAction(frmInvestmentReport)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOperationEdit.setIcon(icon10)
        self.actionOperationEdit.setObjectName("actionOperationEdit")
        self.actionDisReinvest = QtWidgets.QAction(frmInvestmentReport)
        self.actionDisReinvest.setIcon(icon6)
        self.actionDisReinvest.setObjectName("actionDisReinvest")
        self.actionSellingPoint = QtWidgets.QAction(frmInvestmentReport)
        self.actionSellingPoint.setIcon(icon1)
        self.actionSellingPoint.setObjectName("actionSellingPoint")
        self.actionDividendEdit = QtWidgets.QAction(frmInvestmentReport)
        self.actionDividendEdit.setIcon(icon10)
        self.actionDividendEdit.setObjectName("actionDividendEdit")
        self.actionSharesTransferUndo = QtWidgets.QAction(frmInvestmentReport)
        self.actionSharesTransferUndo.setIcon(icon9)
        self.actionSharesTransferUndo.setObjectName("actionSharesTransferUndo")
        self.actionSharesTransfer = QtWidgets.QAction(frmInvestmentReport)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/xulpymoney/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSharesTransfer.setIcon(icon11)
        self.actionSharesTransfer.setObjectName("actionSharesTransfer")
        self.actionSplit = QtWidgets.QAction(frmInvestmentReport)
        self.actionSplit.setIcon(icon10)
        self.actionSplit.setObjectName("actionSplit")
        self.actionChangeBenchmarkPrice = QtWidgets.QAction(frmInvestmentReport)
        self.actionChangeBenchmarkPrice.setIcon(icon10)
        self.actionChangeBenchmarkPrice.setObjectName("actionChangeBenchmarkPrice")
        self.actionRangeReport = QtWidgets.QAction(frmInvestmentReport)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/xulpymoney/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRangeReport.setIcon(icon12)
        self.actionRangeReport.setObjectName("actionRangeReport")
        self.actionDisReinvestProduct = QtWidgets.QAction(frmInvestmentReport)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/xulpymoney/study.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisReinvestProduct.setIcon(icon13)
        self.actionDisReinvestProduct.setObjectName("actionDisReinvestProduct")
        self.actionContractAdd = QtWidgets.QAction(frmInvestmentReport)
        self.actionContractAdd.setIcon(icon8)
        self.actionContractAdd.setObjectName("actionContractAdd")
        self.actionContractDelete = QtWidgets.QAction(frmInvestmentReport)
        self.actionContractDelete.setIcon(icon9)
        self.actionContractDelete.setObjectName("actionContractDelete")
        self.actionContractEdit = QtWidgets.QAction(frmInvestmentReport)
        self.actionContractEdit.setIcon(icon10)
        self.actionContractEdit.setObjectName("actionContractEdit")

        self.retranslateUi(frmInvestmentReport)
        self.tab.setCurrentIndex(5)
        self.chkExpiration.toggled['bool'].connect(self.calExpiration.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(frmInvestmentReport)

    def retranslateUi(self, frmInvestmentReport):
        _translate = QtCore.QCoreApplication.translate
        frmInvestmentReport.setWindowTitle(_translate("frmInvestmentReport", "Investment report"))
        self.label.setText(_translate("frmInvestmentReport", "Associated account"))
        self.label_2.setText(_translate("frmInvestmentReport", "Investment name"))
        self.txtInvestment.setText(_translate("frmInvestmentReport", "New investment"))
        self.label_4.setText(_translate("frmInvestmentReport", "Selling price"))
        self.txtVenta.setText(_translate("frmInvestmentReport", "0"))
        self.chkExpiration.setText(_translate("frmInvestmentReport", "Add selling order expiration"))
        self.cmdToday.setToolTip(_translate("frmInvestmentReport", "Change calendar date to today"))
        self.cmdInvestment.setText(_translate("frmInvestmentReport", "Update investment"))
        self.tab.setTabText(self.tab.indexOf(self.tab_12), _translate("frmInvestmentReport", "Investment data"))
        self.grpCurrentInvestmentCurrency.setTitle(_translate("frmInvestmentReport", "Current status in investment currency"))
        self.grpCurrentAccountCurrency.setTitle(_translate("frmInvestmentReport", "Current status in account currency"))
        self.tab.setTabText(self.tab.indexOf(self.tabInvestmentCurrent), _translate("frmInvestmentReport", "Current status"))
        self.chkOperaciones.setText(_translate("frmInvestmentReport", "Show all operations"))
        self.grpOperationsInvestmentCurrency.setTitle(_translate("frmInvestmentReport", "Operations in investment currency"))
        self.grpOperationsAccountCurrency.setTitle(_translate("frmInvestmentReport", "Operations in account currency"))
        self.tab.setTabText(self.tab.indexOf(self.tabOperacionesHistoricas), _translate("frmInvestmentReport", "Operations"))
        self.grpHistoricalInvestmentCurrency.setTitle(_translate("frmInvestmentReport", "Historical operations in investment currency"))
        self.grpHistoricalAccountCurrency.setTitle(_translate("frmInvestmentReport", "Historical operations in account currency"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("frmInvestmentReport", "Historical operations"))
        self.chkHistoricalDividends.setText(_translate("frmInvestmentReport", "Show historical dividends"))
        self.grpDividendsInvestmentCurrency.setTitle(_translate("frmInvestmentReport", "Dividends in investment currency"))
        self.grpDividendsAccountCurrency.setTitle(_translate("frmInvestmentReport", "Dividends in account currency"))
        self.grpDividendsEstimation.setTitle(_translate("frmInvestmentReport", "Estimation"))
        self.lblDivAnualEstimado.setText(_translate("frmInvestmentReport", "APR"))
        self.lblDivFechaRevision.setText(_translate("frmInvestmentReport", "Review date"))
        self.lblDivSaldoEstimado.setText(_translate("frmInvestmentReport", "Estimated balance"))
        self.grpDividendsEfectivos.setTitle(_translate("frmInvestmentReport", "Collected dividends"))
        self.lblDivTPC.setText(_translate("frmInvestmentReport", "% Invested"))
        self.lblDivTAE.setText(_translate("frmInvestmentReport", "% APR"))
        self.tab.setTabText(self.tab.indexOf(self.tabDividends), _translate("frmInvestmentReport", "Dividends"))
        self.chkHistoricalContracts.setText(_translate("frmInvestmentReport", "Show historical High-Low daily contracts"))
        self.grpHlContracts.setTitle(_translate("frmInvestmentReport", "High-Low operations daily contracts"))
        self.tab.setTabText(self.tab.indexOf(self.tabContracts), _translate("frmInvestmentReport", "Contracts"))
        self.actionOperationAdd.setText(_translate("frmInvestmentReport", "New operation"))
        self.actionOperationAdd.setToolTip(_translate("frmInvestmentReport", "New operation"))
        self.actionOperationDelete.setText(_translate("frmInvestmentReport", "Delete operation"))
        self.actionOperationDelete.setToolTip(_translate("frmInvestmentReport", "Delete operation"))
        self.actionDividendAdd.setText(_translate("frmInvestmentReport", "Add new dividend"))
        self.actionDividendAdd.setToolTip(_translate("frmInvestmentReport", "Add new dividend"))
        self.actionDividendRemove.setText(_translate("frmInvestmentReport", "Delete dividend"))
        self.actionDividendRemove.setToolTip(_translate("frmInvestmentReport", "Delete dividend"))
        self.actionOperationEdit.setText(_translate("frmInvestmentReport", "Edit operation"))
        self.actionOperationEdit.setToolTip(_translate("frmInvestmentReport", "Edit operation"))
        self.actionDisReinvest.setText(_translate("frmInvestmentReport", "Disinvest / Reinvest report"))
        self.actionDisReinvest.setToolTip(_translate("frmInvestmentReport", "Disinvest / Reinvest report"))
        self.actionSellingPoint.setText(_translate("frmInvestmentReport", "Selling point calculation"))
        self.actionSellingPoint.setToolTip(_translate("frmInvestmentReport", "Selling point calculation"))
        self.actionDividendEdit.setText(_translate("frmInvestmentReport", "Edit dividend"))
        self.actionDividendEdit.setToolTip(_translate("frmInvestmentReport", "Edit dividend"))
        self.actionSharesTransferUndo.setText(_translate("frmInvestmentReport", "Undo shares transfer to another bank"))
        self.actionSharesTransferUndo.setToolTip(_translate("frmInvestmentReport", "Undo shares transfer to another bank"))
        self.actionSharesTransfer.setText(_translate("frmInvestmentReport", "Transfer shares to another bank"))
        self.actionSharesTransfer.setToolTip(_translate("frmInvestmentReport", "Transfer shares to another bank"))
        self.actionSplit.setText(_translate("frmInvestmentReport", "Make Split / Contrasplit"))
        self.actionSplit.setToolTip(_translate("frmInvestmentReport", "make Split / Contrasplit"))
        self.actionChangeBenchmarkPrice.setText(_translate("frmInvestmentReport", "Change benchmark price"))
        self.actionChangeBenchmarkPrice.setToolTip(_translate("frmInvestmentReport", "Change benchmark price"))
        self.actionRangeReport.setText(_translate("frmInvestmentReport", "Hide in range report"))
        self.actionRangeReport.setToolTip(_translate("frmInvestmentReport", "Hide in range report"))
        self.actionDisReinvestProduct.setText(_translate("frmInvestmentReport", "Disinvest / Reinvest all product"))
        self.actionDisReinvestProduct.setToolTip(_translate("frmInvestmentReport", "Disinvest / Reinvest all product"))
        self.actionContractAdd.setText(_translate("frmInvestmentReport", "New High-Low contract"))
        self.actionContractAdd.setToolTip(_translate("frmInvestmentReport", "New High-Low contract"))
        self.actionContractDelete.setText(_translate("frmInvestmentReport", "Delete contract"))
        self.actionContractDelete.setToolTip(_translate("frmInvestmentReport", "Delete contract"))
        self.actionContractEdit.setText(_translate("frmInvestmentReport", "Edit contract"))
        self.actionContractEdit.setToolTip(_translate("frmInvestmentReport", "Edit contract"))


from xulpymoney.ui.myqlineedit import myQLineEdit
from xulpymoney.ui.myqtablewidget import myQTableWidget
from xulpymoney.ui.wdgProductSelector import wdgProductSelector
import xulpymoney.images.xulpymoney_rc
