# -*- coding: UTF-8 -*-
from mod_python import util
from core import *
from xul import *




def index(req):
    def page():
        req.content_type="application/vnd.mozilla.xul+xml"
        s=xulheaderwindowmenu("Informe de referencia al Ibex35")

        s=s+'<vbox align="center">\n'
        s=s+'<label id="titulo"  value="Informe de referencia al Ibex35" />\n'
        s=s+'<label/>\n'
        s=s+'</vbox>\n'
        s=s+'<vbox flex="1">\n'
        s=s+grafico
        s=s+'<label flex="0"  style="text-align: center;font-weight : bold;" value="Saldo actual de las inversiones: '+euros(actual)+'" />\n'
        s=s+'<label flex="0"  style="text-align: center;font-weight : bold;" value="Saldo invertido: '+euros(total)+'" />\n'
        s=s+'</vbox>\n'
        s=s+'</window>\n'
        return s
        
    #Consultas BD
    # Para ver como funciona la funcion ver Inversion.nombre_tpcvariable()
    con=Conection()
    cd=ConectionDirect()        
    arrP=[]
    sql="select * from tmpoperinversiones, inversiones where tmpoperinversiones.id_inversiones=inversiones.id_inversiones order by fecha"
    curs=cd.con.Execute(sql);
    while not curs.EOF:
        row = curs.GetRowAssoc(0)
        arrP.append((row["inversion"], row['fecha'], row['acciones'], row['importe'],  InversionOperacion().referencia_ibex35(row['fecha'])))
        curs.MoveNext()
    curs.Close()
    
    firstyear=arrP[0][1].year#Por lo menos 3 años
    if datetime.date.today().year-firstyear<3:
        firstyear=datetime.date.today().year-3#Año de la primea operación. 
    
    arrI=[]
    sql="select * from ibex35 where fecha>='"+str(firstyear)+"-01-01' order by fecha"
    curs=cd.con.Execute(sql);
    while not curs.EOF:
        row = curs.GetRowAssoc(0)
        arrI.append((row["fecha"], row['cierre']))
        curs.MoveNext()
    curs.Close()
    
    arrM=[]
    total=Total().saldo_total(datetime.date.today())
    sql="select distinct(floor(ibex35.cierre/1000))*1000 as miles , sum(importe) as sumimporte from ibex35, tmpoperinversiones where tmpoperinversiones.fecha=ibex35.fecha  group by miles order by miles;"
    curs=cd.con.Execute(sql); 
    actual=Total().saldo_todas_inversiones(datetime.date.today())#saldo actual
    total=cd.con.Execute("select sum(importe) as importe from tmpoperinversiones;").GetRowAssoc(0)["importe"]#total invertido
    while not curs.EOF:
        row = curs.GetRowAssoc(0)   
        arrM.append((row['miles'], row['sumimporte'],  round(100*row['sumimporte']/total, 2)))
        curs.MoveNext()     
    curs.Close()
    con.close()

    grafico=Total().grafico_inversionoperacion_refibex(arrI,arrP, arrM)
    return page()
