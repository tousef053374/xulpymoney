import datetime
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_frmSellingPoint import Ui_frmSellingPoint
from libxulpymoney import Money,  Quote, SetInvestmentOperationsCurrentHomogeneus, qmessagebox
from decimal import Decimal

class frmSellingPoint(QDialog, Ui_frmSellingPoint):
    def __init__(self, mem,  inversion ,   parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.showMaximized()
        self.mem=mem
        self.inversion=inversion
        
        if self.inversion.id==None:
            qmessagebox(self.tr("You can't set a selling price to a unsaved investment"))
            return
        if len(self.inversion.op_actual.arr)==0:
            qmessagebox(self.tr("You don't have shares to sale in this investment"))
            return
        
        self.puntoventa=Decimal(0)#Guarda el resultado de los cálculos
        self.operinversiones=None 

        if self.mem.gainsyear==True:
            self.chkGainsTime.setCheckState(Qt.Checked)
        else:
            self.chkGainsTime.setEnabled(False)

        self.table.settings(self.mem, "frmSellingPoint")
        self.tableSP.settings(self.mem, "frmSellingPoint")
        
        self.cmbTPC.setCurrentText("{} %".format(self.mem.settingsdb.value("frmSellingPoint/lastgainpercentage",  5)))
        
    def __calcular(self):           
        type=2
        if self.chkPonderanAll.checkState()==Qt.Checked:#Results are in self.mem.localcurrency
            self.operinversiones=self.mem.data.investments_active().investment_merging_current_operations_with_same_product(self.inversion.product).op_actual
            self.operinversiones.myqtablewidget(self.table)
            suminvertido=self.operinversiones.invertido()
        else:#Results in account currency
            self.operinversiones=SetInvestmentOperationsCurrentHomogeneus(self.mem, self.inversion)
            if self.chkGainsTime.checkState()==Qt.Checked:
                self.operinversiones=self.inversion.op_actual.copy_until_datetime(self.mem.localzone.now()-datetime.timedelta(days=365))
            else:
                self.operinversiones=self.inversion.op_actual.copy_until_datetime(None)
            self.operinversiones.myqtablewidget(self.table, self.inversion.product.result.basic.last,  type)
            suminvertido=self.operinversiones.invertido(type)
        sumacciones=self.operinversiones.acciones()
        
        if sumacciones==Decimal(0):
            self.puntoventa=Money(self.mem, 0, self.inversion.account.currency)
        else:
            if self.radTPC.isChecked()==True:
                tpc=Decimal(self.cmbTPC.currentText().replace(" %", ""))
                self.puntoventa=Money(self.mem, suminvertido.amount*(1+tpc/100)/sumacciones, self.inversion.account.currency)
            elif self.radPrice.isChecked()==True:
                if self.txtPrice.isValid():#Si hay un numero bien
                    self.puntoventa=Money(self.mem,  self.txtPrice.decimal(),  self.inversion.account.currency)
                    self.cmd.setEnabled(True)
                else:
                    self.puntoventa=Money(self.mem, 0, self.inversion.account.currency)
                    self.cmd.setEnabled(False)
            elif self.radGain.isChecked()==True:
                if self.txtGanancia.isValid():#Si hay un numero bien
                    self.puntoventa=Money(self.mem, (self.txtGanancia.decimal()+suminvertido.amount)/sumacciones, self.inversion.account.currency)
                    self.cmd.setEnabled(True)
                else:
                    self.puntoventa=Money(self.mem, 0, self.inversion.account.currency)
                    self.cmd.setEnabled(False)

        if self.inversion.hasSameAccountCurrency()==False:
            #punto de venta tiene el currency de la acount luego hay que pasarlo al currency de la inversi´on_chkGainsTime_stateChanged
            self.puntoventa=self.puntoventa.convert(self.inversion.product.currency, self.mem.localzone.now())


        quote=Quote(self.mem).init__create(self.inversion.product, self.mem.localzone.now(), self.puntoventa.amount)
        self.tab.setTabText(1, self.tr("Selling point: {0}".format(self.puntoventa)))
        self.tab.setTabText(0, self.tr("Current state: {0}".format(self.inversion.product.currency.string(self.inversion.product.result.basic.last.quote))) )
        self.operinversiones.myqtablewidget(self.tableSP, quote, type) 
        
        if self.chkPonderanAll.checkState()==Qt.Checked:
            self.cmd.setText(self.tr("Set selling price to all investments  of {0} to gain {1}").format(self.puntoventa, self.operinversiones.pendiente(quote, type)))
        else:
            self.cmd.setText(self.tr("Set {0} shares selling price to {1} to gain {2}").format(sumacciones, self.puntoventa, self.operinversiones.pendiente(quote, type)))

    def on_radTPC_clicked(self):
        self.__calcular()
        
    def on_radPrice_clicked(self):
        self.__calcular()
        
    def on_radGain_clicked(self):
        self.__calcular()
        
    @pyqtSlot(str) 
    def on_cmbTPC_currentIndexChanged(self, cur):
        self.__calcular()
        
    def on_txtGanancia_textChanged(self):
        self.__calcular()
        
    def on_txtPrice_textChanged(self):
        self.__calcular()
        
    def on_chkPonderanAll_stateChanged(self, state):
        self.__calcular()
        
    def on_chkGainsTime_stateChanged(self, state):
        self.__calcular()

    @pyqtSlot() 
    def on_cmd_released(self):
        if self.chkPonderanAll.checkState()==Qt.Checked:
            for inv in self.mem.data.investments_active().arr:
                if inv.product.id==self.inversion.product.id:
                    inv.venta=self.puntoventa.amount
                    inv.save()
            self.mem.con.commit()
        
        #Save in settings the last selling percentage, if that's the case
        if self.radTPC.isChecked():
            percentage=Decimal(self.cmbTPC.currentText().replace(" %", ""))
            self.mem.settingsdb.setValue("frmSellingPoint/lastgainpercentage", percentage)
        self.done(0)
