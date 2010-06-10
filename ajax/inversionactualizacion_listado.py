#-*- coding: UTF-8 -*-
from mod_python import util
from core import *
from validar import *

def index(req):
    con=Conection()
    
    form=util.FieldStorage(req)    
    arr=("id_inversiones","year","month")
    if hasReferer(req) and checkParametros(req,arr): 
        if isInt(form['id_inversiones']) and isInt(form['year'])  and isInt(form['month']):
            req.content_type="text/xml"
            con=Conection()
            req.write(InversionActualizacion().xml_listado(InversionActualizacion().cursor_listado(form['id_inversiones'], form['year'], form['month'])))
            con.close()
        else:
            req.write ("False|Error de validación del servidor. Incidencia registrada")
    else:
        req.write ("Logout|Se ha registrado una incidencia grave de seguridad. Ha sido expulsado de la sesión")
    con.close()





