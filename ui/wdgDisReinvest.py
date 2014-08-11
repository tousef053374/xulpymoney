from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_wdgDisReinvest import *
from libxulpymoney import *
from decimal import *

class wdgDisReinvest(QWidget, Ui_wdgDisReinvest):
    def __init__(self, mem, inversion,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.inversion=inversion
                
        if len(self.inversion.op_actual.arr)==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("Actualmente no hay acciones disponibles en esta Inversión"))
            m.exec_()     
            return
#        
#        self.tblInvestmentsActualDespues.settings("wdgDisReinvest",  self.mem)
#        self.tblInvestmentsActualAntes.settings("wdgDisReinvest",  self.mem)
#        self.tblOperaciones.settings("wdgDisReinvest",  self.mem)        
#        self.tblInvestmentsHistoricas.settings("wdgDisReinvest",  self.mem)         
        
 
        self.operinversiones=self.inversion.op.clone()#No hacer clone_from_datetime porque falla por haber borrado un actual por venta de balance operación

        self.txtValorAccion.setText(str(self.inversion.product.result.basic.last.quote))
        self.tabResultados.setCurrentIndex(1)
        self.on_radDes_clicked()

    def acciones(self):
        """Debe calcularse las acciones"""
        resultado=0
        perdida=Decimal(self.txtSimulacion.text())       #Va disminuyendo con las distintas operaciones
       
        if self.radDes.isChecked():#DESINVERSION
            (operinversionesactual, operinversioneshistoricas)=self.operinversiones.calcular()
            q=Quote(self.mem).init__create(self.inversion.product, datetime.datetime.now(pytz.timezone(self.mem.localzone.name)), self.txtValorAccion.decimal())
            for rec in operinversionesactual.arr:
                pendiente=rec.pendiente(q)
                if perdida+pendiente==0:
                    resultado=resultado+Decimal(str(rec.acciones))
                    break
                elif perdida+pendiente>0:
                    resultado=resultado+Decimal(str(rec.acciones))
                    perdida=perdida+pendiente
                elif perdida+pendiente<0:
                    # Si de tantas acciones queda pendiente "pendiente"
                    # X                                queda la perdida
#                    balance=abs(perdida*rec.invertido()/pendiente)
                    acciones=abs(int(perdida*rec.acciones/pendiente))
                    resultado=resultado+Decimal(acciones)#Se resta porque se debe calcular antes de quitarse el pendiente
                    break
        else:#REINVERSION
            resultado=Decimal(int(self.txtSimulacion.decimal()/self.txtValorAccion.decimal()))
        return resultado
            
    @QtCore.pyqtSlot() 
    def on_radDes_clicked(self):
        self.lblTitulo.setText(self.trUtf8("Estudio de desinversión de {0}".format(self.inversion.name)))
        self.lblSimulacion.setText(self.trUtf8("Pérdida aproximada a asumir en la desinversión"))
        self.lblValor.setText(self.trUtf8("Valor de venta"))
        
    @QtCore.pyqtSlot() 
    def on_radRe_clicked(self):
        self.lblTitulo.setText(self.trUtf8("Estudio de reinversión de {0}".format(self.inversion.name)))
        self.lblSimulacion.setText(self.trUtf8("Importe a reinvertir"))
        self.lblValor.setText(self.trUtf8("Valor de compra"))
   
    def on_cmd_released(self):
        if self.txtSimulacion.decimal()<=Decimal('0'):
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("El valor de la simulación debe ser positivo"))
            m.exec_()    
            return
        valor_accion=self.txtValorAccion.decimal()
        impuestos=0
        comision=self.txtComision.decimal()
        if valor_accion==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("El valor de la acción no puede ser 0"))
            m.exec_()    
            return
        acciones=self.acciones()
        importe=valor_accion*acciones
        self.txtAcciones.setText(str(acciones))
        self.txtImporte.setText(str(importe))
        (operinversionesactualantes, operinversioneshistoricasantes)=self.operinversiones.calcular_new()

        #Creamos un nuevo operinversiones 
        operaciones=self.operinversiones.clone()
        d=InvestmentOperation(self.mem)
        id_operinversiones=self.operinversiones.arr[len(self.operinversiones.arr)-1].id+1 ##Para simular un id_operinversiones real, le asignamos uno
        if self.radDes.isChecked():#DESINVERSION
            d.init__create(self.mem.tiposoperaciones.find(5), datetime.datetime.now(pytz.timezone(self.mem.localzone.name)), self.inversion, -acciones, importe, impuestos, comision, valor_accion, "", id_operinversiones)
        else:#REINVERSION
            d.init__create(self.mem.tiposoperaciones.find(4), datetime.datetime.now(pytz.timezone(self.mem.localzone.name)), self.inversion, acciones, importe, impuestos, comision, valor_accion, "",  id_operinversiones)
            d.init__create(self.mem.tiposoperaciones.find(4), datetime.datetime.now(pytz.timezone(self.mem.localzone.name)), self.inversion, acciones, importe, impuestos, comision, valor_accion, "",  id_operinversiones)
        operaciones.arr.append(d)


        (operinversionesactual, operinversioneshistoricas)=operaciones.calcular_new()
        operaciones.myqtablewidget(self.tblOperaciones, "wdgDisReinvest")
        self.inversion.op_actual.myqtablewidget(self.tblInvestmentsActualAntes, "wdgDisReinvest")
        operinversionesactual.myqtablewidget(self.tblInvestmentsActualDespues, "wdgDisReinvest")
        operinversioneshistoricas.myqtablewidget(self.tblInvestmentsHistoricas, "wdgDisReinvest")