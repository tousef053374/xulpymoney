<% 
from xul import *
from config import *
req.content_type="application/vnd.mozilla.xul+xml"
req.write(xulheaderwindowmenu("Acerca de cuentas"))

f=os.popen("/usr/bin/uname -a")
so=f.read()
f.close()

f=os.popen("/usr/bin/python -V")
py=f.read()
f.close()

f=os.popen("/usr/bin/xulrunner --version")
xu=f.read()
f.close()

f=os.popen("/usr/bin/postgres --version")
po=f.read()
f.close()

%>
<vbox  flex="5">
<label id="titulo" value="Acerca de cuentas" />
<label value="<%=version%>" style="text-align : center;"/>

<spacer flex="1"/>
<hbox flex="4">
<spacer flex="5"/>
<tabbox orient="vertical" flex="1">
<tabs>
<tab label="Autores             " />
<tab label="Tecnología utilizada" />
<tab label="Licencia de programa" />
</tabs>
<tabpanels flex="1">
<vbox>
    <grid pack="center">
        <columns>
            <column flex="1" />
            <column flex="1" />
            <column flex="1" />
        </columns>
        <rows>
            <row>
                <label id="negrita" value="Idea:"/>
                <label value="Mariano Muñoz" />
                <label value="turulomio@yahoo.es" />
            </row>
            <row>
                <label id="negrita" value="Desarrollo:"/>
                <label value="Mariano Muñoz" />
                <label value="turulomio@yahoo.es" />
            </row>
            <row>
                <label id="negrita" value="Traducción:"/>
                <label value="Mariano Muñoz" />
                <label value="turulomio@yahoo.es" />
            </row>
            <row>
                <label id="negrita" value=""/>
                <label value="Mi tía la del pueblo" />
                <label value="mitialadelpueblo@yahoo.es" />
            </row>
        </rows>
    </grid>
</vbox>
<vbox>
    <grid pack="center">
        <columns>
            <column flex="1" />
            <column flex="1" />
        </columns>
        <rows>
            <row>
                <label id="negrita" value="Sistema Operativo:"/>
                <label value="<%=so%>" />
            </row>
            <row>
                <label id="negrita" value="Python:"/>
                <label value="<%=py%>" />
            </row>
            <row>
                <label id="negrita" value="XUL:"/>
                <label value="<%=xu%>" />
            </row>
            <row>
                <label id="negrita" value="Database:"/>
                <label value="<%=po%>" />
            </row>
        </rows>
    </grid>
</vbox>
<vbox>
    <browser id="content" type="content-primary" src="/home/nobu/CVS/cvsphpcuentas/GPL-2"/>
</vbox>
</tabpanels>
</tabbox>

<spacer flex="5"/>
</hbox>

</vbox>
<%
req.write(xulfoot())
%>
