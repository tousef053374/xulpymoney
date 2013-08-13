from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libxulpymoney import *
from matplotlib.finance import *
from decimal import Decimal
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.dates import *

# Matplotlib Figure object
from matplotlib.figure import Figure


class ChartType:
    lines=0
    ohcl=1
    candles=2


        

class canvasChart(FigureCanvas):
    """
        RECIBE DATOS DE LA FORMA DATETIME,VALUE
    
    Class to represent the FigureCanvas widget
    type 0:lineas
            since: datetime desde el que mostrar datos
            period: forma en que se muestran 0:5 minutos, 1: 15 minutos, 2:1 hora,3:diario,4:semanal,5 mensual
            
            
    Se crea el objeto
    objeto.settings
    objeto.load_data"""
    def __init__(self, parent):
            
        # setup Matplotlib Figure and Axis
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)
        self.original=None#Almacena los datos originales
        self.currentMatrizDataLength=0#Almacena la longitud de los datos dibujados
        self.since=None #Muestra todos los datos
        self.periodo=None
        
#        self.num=540#Numéro de items a dibujar
        
        
        self.type=None
        
        self.ax = self.fig.add_subplot(111)
        
        #Para grabar settings
        self.file=None
        self.section=None
        
          
        
    def settings(self, section):		
        """Esta funcion debe ejecutarse despues de haber creado las columnas"""
        self.section=section

        try:
            self.type=self.cfg.config_ui.getint(section, "type" )
        except:
            self.type=ChartType.lines
            
        try:
            self.actionSMA50.setChecked(self.cfg.config_ui.getboolean(section, "sma50" ))
        except:
            self.actionSMA50.setChecked(False)

        try:
            self.actionSMA200.setChecked(self.cfg.config_ui.getboolean(section, "sma200" ))
        except:
            self.actionSMA200.setChecked(False)
            
    def on_actionLinesIntraday_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type",   self.type)
        (dates, quotes)=zip(*self.data)
        self._draw_lines_from_quotes(dates, quotes)
                

    def on_actionLines1d_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type",   ChartType.lines)
        self.currentMatrizDataLength=len(self.result.ohclDaily.arr)
        
        if len(self.result.ohclDaily.arr)>self.num:              
            self._draw_lines_from_ohcl(self.result.ohclDaily.arr[len(self.result.ohclDaily.arr)-1-self.num:len(self.result.ohclDaily.arr)])      
        else:
            self._draw_lines_from_ohcl(self.result.ohclDaily.arr)     
        self.draw()

      
        
        
    @pyqtSignature("")
    def on_actionSMA50_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "sma50",   self.actionSMA50.isChecked())
#        self._settings_saveprop("sma50", self.actionSMA50.isChecked())
        self.cfg.configs_save()
#        self._draw()
                
        
    @pyqtSignature("")
    def on_actionSMA200_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "sma200",   self.actionSMA200.isChecked())
        self.cfg.configs_save()
#        self._settings_saveprop("sma200", self.actionSMA200.isChecked())
#        self._draw()
        
        
    def _draw_sma50(self,  datime, quotes):
        #Calculamos según
        """
        Calculamos segun
        a=[1,2,3,4]
        sum([0:2])=3
        """
        if self.actionSMA50.isChecked()==False:
            return
        if len(quotes)<50:
            return
        dat=[]
        sma=[]
        for i in range(50, len(quotes)):
            dat.append(datime[i-1])
            sma.append(sum(quotes[i-50:i])/Decimal(50))
        self.ax.plot_date(dat, sma, '-',  color='gray')     
    
    def _draw_sma200(self, datime, quotes):
        if self.actionSMA200.isChecked()==False:
            return
        if len(quotes)<200:
            return
        dat=[]
        sma=[]
        for i in range(200, len(quotes)):
            dat.append(datime[i-1])
            sma.append(sum(quotes[i-200:i])/Decimal(200))
        self.ax.plot_date(dat, sma, '-', color="red")    


#    def _draw_lines_ohcl(self):
#        return
        
        
    def _get_locators(self, first,  last,  count):
        if count==0:
            return
        interval=(last-first).days
#        print ("Interval get locators",  interval)
        if interval==0:
            self.ax.xaxis.set_major_locator(HourLocator(interval=1 , tz=pytz.timezone(self.cfg.localzone.name)))
            self.ax.xaxis.set_minor_locator(HourLocator(interval=1 , tz=pytz.timezone(self.cfg.localzone.name)))
            self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))            
        elif interval<365:
            self.ax.xaxis.set_minor_locator(MonthLocator())
            self.ax.xaxis.set_major_locator(MonthLocator())
            self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d'))   
        elif interval>=365:
            self.ax.xaxis.set_minor_locator(MonthLocator())
            self.ax.xaxis.set_major_locator(YearLocator())   
            self.ax.xaxis.set_major_formatter( DateFormatter('%Y'))        
            self.ax.fmt_xdata=DateFormatter('%Y-%m-%d')
            #[xmin, xmax, ymin, ymax].
#            print (self.ax.axis())
#            self.ax.axis([0.0, 0.5, 0.0, 0.5])
                        
        self.ax.fmt_ydata = self.price  
        self.ax.grid(True)
#        for tick in self.ax.xaxis.get_major_ticks():
#            tick.label.set_fontsize(9) 
#            tick.label.set_rotation('vertical')
#            
    def _draw_lines_from_ohcl(self, data):
        """Aquí  data es un array de OHCL"""
        self.ax.clear()      
        dates=[]
        quotes=[]
        for ohcl in data:
            dates.append(ohcl.datetime())
            
            quotes.append(ohcl.close)
#        for i in range(len(data)):
#            dates[i]=datetime.datetime.combine(dates[i], datetime.time(0, 0))

        self._get_locators(dates[0],  dates[len(dates)-1], len(dates))
        self.ax.plot_date(dates, quotes, '-')
        self._draw_sma50(dates, quotes)
        self._draw_sma200(dates, quotes)
        self.draw()
        
    def _draw_lines_from_quotes(self, data):
        """Deben estar con tz, se recibe data porque puede recortarese según zoom"""
        self.ax.clear()
        (datetimes, quotes)=([], [])
        for q in data:
            datetimes.append(q.datetime)
            quotes.append(q.quote)

        self._get_locators(datetimes[0],  datetimes[len(datetimes)-1], len(datetimes))
        self.ax.plot_date(datetimes, quotes, '-',  tz=pytz.timezone(self.cfg.localzone.name))
        
        self._draw_sma50(datetimes, quotes)
        self._draw_sma200(datetimes, quotes)
        self.draw()

#    @pyqtSignature("")
#    def on_actionOHCL5m_activated(self):
#        print ("Una vez")
#        self.ohcl(datetime.timedelta(minutes=5))
#
#        self.ax.xaxis.set_major_locator(HourLocator(interval=1 , tz=pytz.timezone(self.cfg.localzone.name)))
#        self.ax.xaxis.set_minor_locator(HourLocator(interval=1, tz=pytz.timezone(self.cfg.localzone.name)))
#        self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))      
#        self.ax.autoscale_view()
#        self.ax.fmt_xdata = DateFormatter('%Y-%m-%d')
#        self.draw()
        
    @pyqtSignature("")
    def on_actionOHCL1d_activated(self):
#        self._settings_saveprop("type", ChartType.ohcl)
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type", ChartType.ohcl)
        self.currentMatrizDataLength=len(self.result.ohclDaily.arr)
        
        if len(self.result.ohclDaily.arr)>self.num:            
            self.ohcl(self.result.ohclDaily.arr[len(self.result.ohclDaily.arr)-1-self.num:len(self.result.ohclDaily.arr)], datetime.timedelta(days=1))       
        else:
            self.ohcl(self.result.ohclDaily.arr, datetime.timedelta(days=1))     
     
        self.draw()
                
#    @pyqtSignature("")
#    def on_actionOHCL30d_activated(self):
#        print ("Una vez")
#        self.ohcl(datetime.timedelta(days=30))
#        if len(self.data)<60:
#            self.ax.xaxis.set_minor_locator(DayLocator())
#            self.ax.xaxis.set_major_locator(MonthLocator())
#            self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d'))   
#        else:
#            self.ax.xaxis.set_minor_locator(MonthLocator())
#            self.ax.xaxis.set_major_locator(YearLocator())                    
#        self.ax.autoscale_view()
#        self.ax.fmt_xdata = DateFormatter('%Y-%m-%d')
#        self.draw()
        
    def ohcl(self, ohcldata,  interval):
        self.ax.clear()
            
#        dates, open,  close, high, low, volumen=zip(*ohcldata)
        quotes=[]
        dates=[]
        close=[]
        self._get_locators(ohcldata[0].datetime(),  ohcldata[len(ohcldata)-1].datetime(), len(ohcldata))
        for d in ohcldata:
            quotes.append((d.datetime().toordinal(), d.open, d.close,  d.high, d.low))         #ESTE ES EL CAUSEANTE NO SE VEA MENOR DE DIARIO TOOARDIANL
            dates.append(d.datetime())
            close.append(d.close)

#        self.ax.autoscale_view()
        self.ax.fmt_xdata = DateFormatter('%Y-%m-%d')
        left=ohcldata[0].datetime().toordinal()-interval.days#De margen
        right=ohcldata[len(ohcldata)-1].datetime().toordinal()+interval.days
        self.ax.set_xlim(left, right)
        plot_day_summary(self.ax, quotes,  ticksize=4)
        self._draw_sma50(dates, close)
        self._draw_sma200(dates, close)

    @pyqtSignature("")
    def on_actionCandles1d_activated(self):
        self.candles(datetime.timedelta(days=1))
        if len(self.data)<1000:
            self.ax.xaxis.set_minor_locator(DayLocator())
            self.ax.xaxis.set_major_locator(MonthLocator())
            self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d'))   
        else:
            self.ax.xaxis.set_minor_locator(MonthLocator())
            self.ax.xaxis.set_major_locator(YearLocator())
        self.ax.autoscale_view()
        self.__draw()
        
    def candles(self, interval):
        """Interval 0.05 5minutos
        1 1 dia"""
        self.ax.clear()
        self.data=self.format_data(6, interval)

        quotes=[]
        for d in self.data:
            quotes.append((d[0].toordinal(), d[1], d[2], d[3], d[4]))


        # format the coords message box
        self.ax.fmt_xdata = DateFormatter('%Y-%m-%d')
        self.ax.fmt_ydata = self.price
        self.ax.grid(True)
#                self.fig.autofmt_xdate()
        candlestick(self.ax,quotes,   width=0.6)
        self.ax.xaxis_date()


    def clear(self):
        self.ax.clear()
    

#        
#        
#    def is_intraday(self, data2):
#        first=data2[0][0].day
#        for d in data2:
#            if d[0].day!=first:
#                return False
#        return True        
#    def is_intramonth(self, data2):
#        first=data2[0][0].month
#        for d in data2:
#            if d[0].month!=first:
#                return False
#        return True
#        
#        
#    def quita_ohcl(self, data):
#        resultado=[]
#        for d in self.data:
#            if d[0].microsecond in (1, 2, 3, 4):
#                continue
#            else:
#                resultado.append(d)
#        return resultado
        
#    def dibuja_ohcl(self, data):
#        return
#    
    def common_actions(self):
        self.actionSMA50=QAction(self)
        self.actionSMA50.setText(self.trUtf8("Media móvil simple 50"))
        self.actionSMA50.setCheckable(True)
        self.actionSMA50.setObjectName(self.trUtf8("actionSMA50"))
        self.actionSMA200=QAction(self)
        self.actionSMA200.setText(self.trUtf8("Media móvil simple 200"))
        self.actionSMA200.setCheckable(True)
        self.actionSMA200.setObjectName(self.trUtf8("actionSMA200"))
        
        self.actionLines5m=QAction(self)
        self.actionLines5m.setText(self.trUtf8("5 minutos"))
        self.actionLines5m.setObjectName(self.trUtf8("actionLines5m"))
        self.actionLines5m.setEnabled(False)
        self.actionLines10m=QAction(self)
        self.actionLines10m.setText(self.trUtf8("10 minutos"))
        self.actionLines10m.setObjectName(self.trUtf8("actionLines10m"))
        self.actionLines10m.setEnabled(False)
        self.actionLines30m=QAction(self)
        self.actionLines30m.setText(self.trUtf8("30 minutos"))
        self.actionLines30m.setObjectName(self.trUtf8("actionLines30m"))
        self.actionLines30m.setEnabled(False)
        self.actionLines60m=QAction(self)
        self.actionLines60m.setText(self.trUtf8("1 hora"))
        self.actionLines60m.setObjectName(self.trUtf8("actionLines60m"))
        self.actionLines60m.setEnabled(False)
        
        
        self.actionOHCL5m=QAction(self)
        self.actionOHCL5m.setText(self.trUtf8("5 minutos"))
        self.actionOHCL5m.setObjectName(self.trUtf8("actionOHCL5m"))
        self.actionOHCL5m.setEnabled(False)
        self.actionOHCL10m=QAction(self)
        self.actionOHCL10m.setText(self.trUtf8("10 minutos"))
        self.actionOHCL10m.setEnabled(False)
        self.actionOHCL10m.setObjectName(self.trUtf8("actionOHCL10m"))
        self.actionOHCL30m=QAction(self)
        self.actionOHCL30m.setText(self.trUtf8("30 minutos"))
        self.actionOHCL30m.setEnabled(False)
        self.actionOHCL30m.setObjectName(self.trUtf8("actionOHCL30m"))
        self.actionOHCL60m=QAction(self)
        self.actionOHCL60m.setText(self.trUtf8("1 hora"))
        self.actionOHCL60m.setEnabled(False)
        self.actionOHCL60m.setObjectName(self.trUtf8("actionOHCL60m"))
        
        self.actionCandles5m=QAction(self)
        self.actionCandles5m.setText(self.trUtf8("5 minutos"))
        self.actionCandles5m.setEnabled(False)
        self.actionCandles5m.setObjectName(self.trUtf8("actionCandles5m"))
        self.actionCandles10m=QAction(self)
        self.actionCandles10m.setText(self.trUtf8("10 minutos"))
        self.actionCandles10m.setEnabled(False)
        self.actionCandles10m.setObjectName(self.trUtf8("actionCandles10m"))
        self.actionCandles30m=QAction(self)
        self.actionCandles30m.setText(self.trUtf8("30 minutos"))
        self.actionCandles30m.setEnabled(False)
        self.actionCandles30m.setObjectName(self.trUtf8("actionCandles30m"))
        self.actionCandles60m=QAction(self)
        self.actionCandles60m.setText(self.trUtf8("1 hora"))
        self.actionCandles60m.setEnabled(False)
        self.actionCandles60m.setObjectName(self.trUtf8("actionCandles60m"))
        
        QMetaObject.connectSlotsByName(self)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self,SIGNAL('customContextMenuRequested(QPoint)'), self.on_customContextMenuRequested)
#        self.connect(self, SIGNAL('wheelEvent(QWheelEvent'), self.on_wheelEvent)
#        self.connect(self.fig.canvas, SIGNAL('button_press_event), self.on_press)
#        cid = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
#        
#    def on_press(self, event):
#        print ('you pressed', event.button, event.xdata, event.ydata)

# {
#     int numDegrees = event->delta() / 8;
#     int numSteps = numDegrees / 15;
#
#     if (event->orientation() == Qt.Horizontal) {
#         scrollHorizontally(numSteps);
#     } else {
#         scrollVertically(numSteps);
#     }
#     event->accept();
# }

class canvasChartIntraday(canvasChart):
    def __init__(self, cfg,  parent):
        self.cfg=cfg
        canvasChart.__init__(self, parent)
        self.setupUi()
        self.settings("canvasIntraday")
        

    def price(self, x): 
        """Se sobreescribe para mostrar el % de inicio"""
#        return '{0}{1}{2}'.format(round(x, 2), self.investment.currency.symbol,  (self.penultimate.quote-x)*100/self.penultimate.quote)
        return  (self.penultimate.quote-x)*100/self.penultimate.quote
        
    def load_data_intraday(self, investment):
        self.result=investment.result
        self.data=self.result.intradia.arr
        self.penultimate=self.result.penultimate
        self.investment=investment
        self._draw_lines_from_quotes(self.data)
        
    def on_customContextMenuRequested(self, pos):
        menu=QMenu()
        ohcl=QMenu("OHCL")
        ohcl.addAction(self.actionOHCL5m)
        ohcl.addAction(self.actionOHCL10m)
        ohcl.addAction(self.actionOHCL30m)
        ohcl.addAction(self.actionOHCL60m)
        menu.addMenu(ohcl)        
        lines=QMenu("Líneas")
        lines.addAction(self.actionLinesIntraday)
        lines.addAction(self.actionLines5m)
        lines.addAction(self.actionLines10m)
        lines.addAction(self.actionLines30m)
        lines.addAction(self.actionLines60m)
        menu.addMenu(lines)        
        candles=QMenu("Candles")
        candles.addAction(self.actionCandles5m)
        candles.addAction(self.actionCandles10m)
        candles.addAction(self.actionCandles30m)
        candles.addAction(self.actionCandles60m)
        menu.addMenu(candles)        
        menu.addSeparator()
        indicadores=QMenu("Indicadores")
        indicadores.addAction(self.actionSMA50)
        indicadores.addAction(self.actionSMA200)
        menu.addMenu(indicadores)            
        menu.exec_(self.mapToGlobal(pos))
        
    def setupUi(self):
        self.actionLinesIntraday=QAction(self)
        self.actionLinesIntraday.setText(self.trUtf8("Intradia"))
        self.actionLinesIntraday.setObjectName(self.trUtf8("actionLinesIntraday"))
        self.common_actions()
class canvasChartHistorical(canvasChart):
    
    def __init__(self, cfg,   parent):
        self.cfg=cfg
        canvasChart.__init__(self, parent)
        self.num=50#Numero de items a mostrar
        self.setupUi()
        self.settings("canvasHistorical")
        
    def __draw(self):
        if self.type==ChartType.lines:
            self.on_actionLines1d_activated()
        elif self.type==ChartType.ohcl:
            self.on_actionOHCL1d_activated()
        elif self.type==ChartType.candles:
            self.on_actionCandles1d_activated()
            
           
    def price(self, x): 
        return '{0} {1}'.format(round(x, 2), self.investment.currency.symbol)
    def setupUi(self):
        self.actionLinesIntraday=QAction(self)
        self.actionLinesIntraday.setText(self.trUtf8("Intradia"))
        self.actionLinesIntraday.setObjectName(self.trUtf8("actionLinesIntraday"))
        
        self.actionLines1d=QAction(self)
        self.actionLines1d.setText(self.trUtf8("1 dia"))
        self.actionLines1d.setObjectName(self.trUtf8("actionLines1d"))
        self.actionLines7d=QAction(self)
        self.actionLines7d.setText(self.trUtf8("1 semana"))
        self.actionLines7d.setObjectName(self.trUtf8("actionLines7d"))
        self.actionLines7d.setEnabled(False)
        self.actionLines30d=QAction(self)
        self.actionLines30d.setText(self.trUtf8("1 mes"))
        self.actionLines30d.setObjectName(self.trUtf8("actionLines30d"))
        self.actionLines30d.setEnabled(False)
        self.actionLines365d=QAction(self)
        self.actionLines365d.setText(self.trUtf8("1 año"))
        self.actionLines365d.setObjectName(self.trUtf8("actionLines365d"))        
        self.actionLines365d.setEnabled(False)
        
        self.actionOHCL1d=QAction(self)
        self.actionOHCL1d.setText(self.trUtf8("1 dia"))
        self.actionOHCL1d.setObjectName(self.trUtf8("actionOHCL1d"))
        self.actionOHCL7d=QAction(self)
        self.actionOHCL7d.setText(self.trUtf8("1 semana"))
        self.actionOHCL7d.setObjectName(self.trUtf8("actionOHCL7d"))
        self.actionOHCL30d=QAction(self)
        self.actionOHCL30d.setText(self.trUtf8("1 mes"))
        self.actionOHCL30d.setObjectName(self.trUtf8("actionOHCL30d"))
        self.actionOHCL365d=QAction(self)
        self.actionOHCL365d.setText(self.trUtf8("1 año"))
        self.actionOHCL365d.setObjectName(self.trUtf8("actionOHCL365d"))
        
        self.actionCandles1d=QAction(self)
        self.actionCandles1d.setText(self.trUtf8("1 dia"))
        self.actionCandles1d.setEnabled(False)
        self.actionCandles1d.setObjectName(self.trUtf8("actionCandles1d"))
        self.actionCandles7d=QAction(self)
        self.actionCandles7d.setText(self.trUtf8("1 semana"))
        self.actionCandles7d.setEnabled(False)
        self.actionCandles7d.setObjectName(self.trUtf8("actionCandles7d"))
        self.actionCandles30d=QAction(self)
        self.actionCandles30d.setText(self.trUtf8("1 mes"))
        self.actionCandles30d.setEnabled(False)
        self.actionCandles30d.setObjectName(self.trUtf8("actionCandles30d"))
        self.actionCandles365d=QAction(self)
        self.actionCandles365d.setText(self.trUtf8("1 año"))
        self.actionCandles365d.setEnabled(False)
        self.actionCandles365d.setObjectName(self.trUtf8("actionCandles365d"))
        
        self.common_actions()
        self.fig.canvas.mpl_connect('scroll_event', self.on_wheelEvent)
        
    def on_wheelEvent(self, event):
#        print (event.button, event.step)
        if event.button=='up':
            self.num=self.num-120
        else:
            self.num=self.num+120
#        print (self.num)
        if self.num<50:
            QApplication.beep()
            self.num=50
            return
        elif self.num>=self.currentMatrizDataLength:
            QApplication.beep()
            self.num=self.currentMatrizDataLength
            return
        self.__draw()
#    figzoom.canvas.draw()
    @pyqtSignature("")
    def on_actionOHCL7d_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type", ChartType.ohcl)
        ohclWeekly=self.result.ohclWeekly.arr
        self.currentMatrizDataLength=len(ohclWeekly)
        
        if len(ohclWeekly)>self.num:            
            self.ohcl(ohclWeekly[len(ohclWeekly)-1-self.num:len(ohclWeekly)], datetime.timedelta(days=7))       
        else:
            self.ohcl(ohclWeekly, datetime.timedelta(days=7))     
        self.draw()
    @pyqtSignature("")
    def on_actionOHCL30d_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type", ChartType.ohcl)
        ohclMonthly=self.result.ohclMonthly.arr
        self.currentMatrizDataLength=len(ohclMonthly)
        
        if len(ohclMonthly)>self.num:            
            self.ohcl(ohclMonthly[len(ohclMonthly)-1-self.num:len(ohclMonthly)], datetime.timedelta(days=30))       
        else:
            self.ohcl(ohclMonthly, datetime.timedelta(days=30))     
        self.draw()
    @pyqtSignature("")
    def on_actionOHCL365d_activated(self):
        self.cfg.config_set_value(self.cfg.config_ui, self.section, "type", ChartType.ohcl)
        ohclYearly=self.result.ohclYearly.arr
        self.currentMatrizDataLength=len(ohclYearly)
        
        if len(ohclYearly)>self.num:            
            self.ohcl(ohclYearly[len(ohclYearly)-1-self.num:len(ohclYearly)], datetime.timedelta(days=365))       
        else:
            self.ohcl(ohclYearly, datetime.timedelta(days=365))     
        self.draw()
        
    def on_customContextMenuRequested(self, pos):
        menu=QMenu()
        ohcl=QMenu("OHCL")
        ohcl.addAction(self.actionOHCL5m)
        ohcl.addAction(self.actionOHCL10m)
        ohcl.addAction(self.actionOHCL30m)
        ohcl.addAction(self.actionOHCL60m)
        ohcl.addAction(self.actionOHCL1d)
        ohcl.addAction(self.actionOHCL7d)
        ohcl.addAction(self.actionOHCL30d)
        ohcl.addAction(self.actionOHCL365d)
        menu.addMenu(ohcl)        
        lines=QMenu("Líneas")
        lines.addAction(self.actionLines5m)
        lines.addAction(self.actionLines10m)
        lines.addAction(self.actionLines30m)
        lines.addAction(self.actionLines60m)
        lines.addAction(self.actionLines1d)
        lines.addAction(self.actionLines7d)
        lines.addAction(self.actionLines30d)
        lines.addAction(self.actionLines365d)
        menu.addMenu(lines)        
        candles=QMenu("Candles")
        candles.addAction(self.actionCandles5m)
        candles.addAction(self.actionCandles10m)
        candles.addAction(self.actionCandles30m)
        candles.addAction(self.actionCandles60m)
        candles.addAction(self.actionCandles1d)
        candles.addAction(self.actionCandles7d)
        candles.addAction(self.actionCandles30d)
        candles.addAction(self.actionCandles365d)
        menu.addMenu(candles)        
        menu.addSeparator()
        indicadores=QMenu("Indicadores")
        indicadores.addAction(self.actionSMA50)
        indicadores.addAction(self.actionSMA200)
        menu.addMenu(indicadores)            
        menu.exec_(self.mapToGlobal(pos)) 

    def load_data(self, investment,  result):
        self.investment=investment
        self.result=result
        self.__draw()