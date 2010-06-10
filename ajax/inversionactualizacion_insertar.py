#-*- coding: UTF-8 -*-
from mod_python import util
from core import *
from validar import *
import validar, sys
def index(req):
    form=util.FieldStorage(req)    
    con=Conection()
    
    arr=("id_inversiones","fecha","valor")
    if hasReferer(req) and checkParametros(req,arr):
        if isInt(form['id_inversiones']) and isDate(form['fecha']) and isFloat(form['valor']):
            if InversionActualizacion().insertar(form['id_inversiones'], form['fecha'], form['valor'])==True:
                req.write ("True|")
            else:
                req.write ("False|Ha habido un error en la base de datos")
        else:
            req.write ("False|Error de validación del servidor. Incidencia registrada")
    else:
        req.write ("Logout|Se ha registrado una incidencia grave de seguridad. Ha sido expulsado de la sesión")
    con.close()
