from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_wdgSource import *
from libsources import *
from myqtablewidget import *

class Sources:
    WorkerYahoo=1
    WorkerYahooHistorical=2
    WorkerMercadoContinuo=3

#class TWorker(QThread):
#    """Hilo que actualiza las products, solo el getBasic, cualquier cambio no de last, deberá ser desarrollado por código"""
#    def __init__(self, mem, sources):
#        QThread.__init__(self)
#        self.mem=mem                
#        if sources==Sources.WorkerYahoo:
#            cur=mem.con.cursor()
#            cur.execute("select count(*) from products where active=true and priority[1]=1")
#            num=cur.fetchone()[0]
#            step=150
#            for i in range (0, int(num/step)+1):
#                self.worker=WorkerYahoo(mem, "select * from products where active=true and priority[1]=1 order by ticker limit {} offset {};".format(step, step*i))
#            cur.close()           
#        elif sources==Sources.WorkerYahooHistorical:
#            self.worker=WorkerYahooHistorical(mem, 1)
#        elif sources==Sources.WorkerMercadoContinuo:                
#            self.worker=WorkerMercadoContinuo(mem)
#            
#    def run(self):
#        print ("TWorker started")
#        self.worker.run()
#        
            
class wdgSource(QWidget, Ui_wdgSource):
    def __init__(self, mem, sources,  parent = None, name = None):
        QWidget.__init__(self,  parent)
        self.setupUi(self)
        self.mem=mem
        self.agrupation=[]#used to iterate workers 
        self.totals=Source(self.mem)# Used to show totals of agrupation
        if sources==Sources.WorkerYahoo:
            cur=mem.con.cursor()
            cur.execute("select count(*) from products where active=true and priority[1]=1")
            num=cur.fetchone()[0]
            step=150
            for i in range (0, int(num/step)+1):
                self.worker=WorkerYahoo(mem, "select * from products where active=true and priority[1]=1 order by ticker limit {} offset {};".format(step, step*i))
                self.agrupation.append(self.worker)
            cur.close()           
        elif sources==Sources.WorkerYahooHistorical:
            self.worker=WorkerYahooHistorical(mem, 0)
            self.agrupation.append(self.worker)
        elif sources==Sources.WorkerMercadoContinuo:                
            self.worker=WorkerMercadoContinuo(mem)
            self.agrupation.append(self.worker)

        self.lbl.setText(self.worker.__class__.__name__)
        
        

    def on_cmdRun_released(self):
        for worker in self.agrupation:
            QTimer.singleShot(200, worker, SLOT(worker.run()))
            worker.inserted.addTo(self.totals.inserted)
            worker.modified.addTo(self.totals.modified)
            worker.ignored.addTo(self.totals.ignored)
            worker.bad.addTo(self.totals.bad)
            worker.quotes.addTo(self.totals.quotes)
            self.totals.errors=worker.errors+self.totals.errors
            QCoreApplication.sendPostedEvents();   
        
        self.cmdRun.setEnabled(False)     
        self.grp.setTitle(self.tr("{} quotes got from the source").format(self.totals.quotes.length()))
        self.cmdInserted.setText(self.tr("{} Inserted").format(self.totals.inserted.length()))
        self.cmdEdited.setText(self.tr("{} Edited").format(self.totals.modified.length()))
        self.cmdIgnored.setText(self.tr("{} Ignored").format(self.totals.ignored.length()))
        self.cmdErrors.setText(self.tr("{} errors parsing the source").format(len(self.totals.errors)))
        self.cmdBad.setText(self.tr("{} bad").format(self.totals.bad.length()))
        self.cmdInserted.setEnabled(True)
        self.cmdIgnored.setEnabled(True)
        self.cmdEdited.setEnabled(True)
        self.cmdErrors.setEnabled(True)
        self.cmdBad.setEnabled(True)        

#        
#    def agrupation_isfinished(self):
#        """Returns a boolean if all workers in agrupation are finished"""
#        for worker in self.agrupation:
#            if worker.finished==False:
#                return False
#        return True


    def on_cmdInserted_released(self):
        d=QDialog(self)        
        d.setFixedSize(900, 670)
        d.setWindowTitle(self.trUtf8("Inserted quotes"))
        t=myQTableWidget(d)
        self.totals.inserted.myqtablewidget(t, "wdgSource")
        lay = QVBoxLayout(d)
        lay.addWidget(t)
        d.show()
        
    def on_cmdEdited_released(self):
        d=QDialog(self)        
        d.setFixedSize(900, 670)
        d.setWindowTitle(self.trUtf8("Edited quotes"))
        t=myQTableWidget(d)
        self.totals.modified.myqtablewidget(t, "wdgSource")
        lay = QVBoxLayout(d)
        lay.addWidget(t)
        d.show()
        
    def on_cmdIgnored_released(self):
        d=QDialog(self)        
        d.setFixedSize(900, 670)
        d.setWindowTitle(self.trUtf8("Ignored quotes"))
        t=myQTableWidget(d)
        self.totals.ignored.myqtablewidget(t, "wdgSource")
        lay = QVBoxLayout(d)
        lay.addWidget(t)
        d.show()
        
    def on_cmdErrors_released(self):
        d=QDialog(self)        
        d.setFixedSize(900, 670)
        d.setWindowTitle(self.trUtf8("Error procesing the source"))
        terrors=myQTableWidget(d)
        self.totals.myqtablewidget_errors(terrors, "wdgSource")
        lay = QVBoxLayout(d)
        lay.addWidget(terrors)
        d.show()

    def on_cmdBad_released(self):
        d=QDialog(self)        
        d.setFixedSize(900, 670)
        d.setWindowTitle(self.trUtf8("Error procesing the source"))
        t=myQTableWidget(d)
        self.totals.bad.myqtablewidget(t, "wdgSource")
        lay = QVBoxLayout(d)
        lay.addWidget(t)
        d.show()

