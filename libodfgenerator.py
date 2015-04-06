from PyQt5.QtCore import *
import odf
import odf.opendocument
import odf.style
import odf.text
import odf.table
import odf.draw
import odf.meta
import odf.dc
import os
from wdgTotal import *
from wdgInvestments import *
from libxulpymoney import *

class ODT(QObject):
    def __init__(self, mem, filename, template=None):    
        QObject.__init__(self)
        
        self.mem=mem
        self.filename=filename
        self.doc=odf.opendocument.OpenDocumentText()
        
        if template!=None:
            templatedoc= odf.opendocument.load(template)
            for style in templatedoc.styles.childNodes[:]:
                self.doc.styles.addElement(style)
          
            for autostyle in templatedoc.automaticstyles.childNodes[:]:
                self.doc.automaticstyles.addElement(autostyle)
                
            for master in templatedoc.masterstyles.childNodes[:]:
                self.doc.masterstyles.addElement(master)
            
        
    def emptyParagraph(self, style="Standard", number=1):
        for i in range(number):
            self.simpleParagraph("",style)
            
    def simpleParagraph(self, text, style="Standard"):
        p=odf.text.P(stylename=style, text=text)
        self.doc.text.addElement(p)
        
    def header(self, text, level):
        h=odf.text.H(outlinelevel=level, stylename="Heading {}".format(level), text=text)
        self.doc.text.addElement(h)
        
        
        
    def table(self, header, orientation,  data, sizes, font, number)       :
        """Headerl text
        Data: data
        sizes: arr with column widths in cm
        size=font size
        number=name"""  
    
        tablesize=sum(sizes)
        
        s=odf.style.Style(name="Tabla{}".format(number))
        s.addElement(odf.style.TableProperties(width="{}cm".format(tablesize), align="center"))
        self.doc.automaticstyles.addElement(s)
        
        #Column sizes
        for i, size in enumerate(sizes):
            sc= odf.style.Style(name="Tabla{}.{}".format(number, chr(65+i)), family="table-column")
            sc.addElement(odf.style.TableColumnProperties(columnwidth="{}cm".format(sizes[i])))
            self.doc.automaticstyles.addElement(sc)
        
        #Cell header style
        sch=odf.style.Style(name="Tabla{}.HeaderCell".format(number, chr(65), 1), family="table-cell")
        sch.addElement(odf.style.TableCellProperties(border="0.05pt solid #000000"))
        self.doc.automaticstyles.addElement(sch)        
        
        #Cell normal
        sch=odf.style.Style(name="Tabla{}.Cell".format(number), family="table-cell")
        sch.addElement(odf.style.TableCellProperties(border="0.05pt solid #000000"))
        self.doc.automaticstyles.addElement(sch)

    
        #Table columns
        table = odf.table.Table(stylename="Tabla{}".format(number))
        for i, head in enumerate(header):
            table.addElement(odf.table.TableColumn(stylename="Tabla{}.{}".format(number, chr(65+i))))  
            
        #Header rows
        headerrow=odf.table.TableHeaderRows()
        tablerow=odf.table.TableRow()
        headerrow.addElement(tablerow)
        for i, head in enumerate(header):
            p=odf.text.P(stylename="Table Heading", text=head)
            tablecell=odf.table.TableCell(stylename="Tabla{}.HeaderCell".format(number))
            tablecell.addElement(p)
            tablerow.addElement(tablecell)
        table.addElement(headerrow)
            
        #Data rows
        for row in data:
            tr = odf.table.TableRow()
            table.addElement(tr)
            for i, col in enumerate(row):
                tc = odf.table.TableCell(stylename="Tabla{}.Cell".format(number))
                tr.addElement(tc)
                if orientation[i]=="<":
                    p = odf.text.P(stylename="Table Contents",text=col)
                elif orientation[i]==">":
                    p = odf.text.P(stylename="Contenido de la tabla derecha",text=col)
                tc.addElement(p)
        
        self.doc.text.addElement(table)
        
    def image(self, filename, width, height):
        p = odf.text.P(stylename="Illustration")
        href = self.doc.addPicture(filename)
        f = odf.draw.Frame(name="filename", anchortype="as-char", width="{}cm".format(width), height="{}cm".format(height)) #, width="2cm", height="2cm", zindex="0")
        p.addElement(f)
        img = odf.draw.Image(href=href, type="simple", show="embed", actuate="onLoad")
        f.addElement(img)
        self.doc.text.addElement(p)

    def pageBreak(self):    
        p=odf.text.P(stylename="PageBreak")#Is an automatic style
        self.doc.text.addElement(p)
#
#    def link(self):
#        para = odf.text.P()
#        anchor = odf.text.A(href="http://www.com/", text="A link label")
#        para.addElement(anchor)
#        self.doc.text.addElement(para)
#        
#    #######################################

class AssetsReport(ODT):
    def __init__(self, mem, filename, template):
        ODT.__init__(self, mem, filename, template)
        self.dir=None#Directory in tmp
        
    def generate(self):
        self.dir='/tmp/AssetsReport-{}'.format(datetime.datetime.now())
        os.makedirs(self.dir)
        self.variables()
        self.metadata()
        self.cover()
        self.body()
        self.doc.save(self.filename)   
        
    def variables(self):
        self.vTotalLastYear=Assets(self.mem).saldo_total(self.mem.data.investments_all(),  datetime.date(datetime.date.today().year-1, 12, 31))
        self.vTotal=Assets(self.mem).saldo_total(self.mem.data.investments_all(),  datetime.date.today())


    def cover(self):
        self.emptyParagraph(number=10)
        self.simpleParagraph(self.tr("Assets Report"), "Title")
        self.simpleParagraph(self.tr("Generated by Xulpymoney-{}".format(version)), "Subtitle")
        self.emptyParagraph(number=8)
        self.simpleParagraph("{}".format(datetime.datetime.now()), "Quotations")        
        self.pageBreak()
        
    def body(self):
        c=self.mem.localcurrency.string
        ## About
        self.header(self.tr("About Xulpymoney"), 1)
        self.header(self.tr("About this report"), 2)
        self.pageBreak()
        ## Assets
        self.header(self.tr("Assets"), 1)
        self.simpleParagraph(self.tr("The total assets of the user is {}.").format(c(self.vTotal)))
        if self.vTotalLastYear!=0:
            moreorless="more"
            if self.vTotal-self.vTotalLastYear<0:
                moreorless="less"
            self.simpleParagraph(self.tr("It's a {} {} of the total assets at the end of the last year.").format(tpc(100*(self.vTotal-self.vTotalLastYear)/self.vTotalLastYear), moreorless))
        
        ### Assets by bank
        self.header(self.tr("Assets by bank"), 2)
        data=[]
        self.mem.data.banks_active.order_by_name()
        for bank in self.mem.data.banks_active.arr:
            data.append((bank.name, c(bank.balance(self.mem.data.accounts_active, self.mem.data.investments_active))))
        self.table( [self.tr("Bank"), self.tr("Balance")], ["<", ">"], data, [3, 2], 12, 1)       
        
        ### Assests current year
        self.header(self.tr("Assets current year evolution"), 2)
#        w=wdgInvestments(self.mem)
#        w.resize(1280, 30*self.mem.data.investments_active.length())
#        w.tblInvestments.on_cellDoubleClicked(0, 0)
#        p=QPixmap(w.size())
#        w.render(p)
#        p.save("{}/wdgInvestments.png".format(self.dir))
#        self.image("{}/wdgInvestments.png".format(self.dir), 17, 12)
        sumpendiente=0
        suminvertido=0
        sumpositivos=0
        sumnegativos=0
        data=[]
        self.mem.data.investments_active.order_by_percentage_sellingpoint()
        for inv in self.mem.data.investments_active.arr:            
            suminvertido=suminvertido+inv.invertido()
            pendiente=inv.pendiente()
            if pendiente>0:
                sumpositivos=sumpositivos+pendiente
            else:
                sumnegativos=sumnegativos+pendiente
            suminvertido=suminvertido+inv.tpc_invertido()
            arr=("{0} ({1})".format(inv.name, inv.cuenta.name), c(inv.balance()), c(pendiente), tpc(inv.tpc_invertido()), tpc(inv.tpc_venta()))
            data.append(arr)

        self.table( [self.tr("Investment"), self.tr("Balance"), self.tr("Gains"), self.tr("% Invested"), self.tr("% Selling point")], ["<", ">", ">", ">", ">"], data, [3, 2, 2, 2, 2], 12, 2)       
        
        if suminvertido!=0:
            self.simpleParagraph(self.tr("Invested assets: {}. Pending: {} - {} = {} ({} assets). Assets average age: {}").format(c(suminvertido), c(sumpositivos),  c(-sumnegativos),  c(sumpendiente), tpc(100*sumpendiente/suminvertido) ,  days_to_year_month(self.mem.data.investments_active.average_age())))
        else:
            self.simpleParagraph(self.tr("There aren't invested assets"))
        
        
        ### Assets evolution graphic
        self.header(self.tr("Assets graphical evolution"), 2)
        
        w=wdgTotal(self.mem)
        w.load_graphic("{}/wdgTotal.png".format(self.dir))
        self.image("{}/wdgTotal.png".format(self.dir), 15, 10)
        self.simpleParagraph("")
        
        self.pageBreak()
        
        
        ## Accounts
        self.header(self.tr("Current Accounts"), 1)
        self.pageBreak()
        
        ## Investments
        self.header(self.tr("Current investments"), 1)
        
        self.header(self.tr("Investments list"), 2)
        
        
        ### Graphics wdgInvestments clases
        self.header(self.tr("Investments group by variable percentage"), 2)
        self.header(self.tr("Investments group by investment type"), 2)
        self.header(self.tr("Investments group by leverage"), 2)
        self.header(self.tr("Investments group by investment product"), 2)
        self.pageBreak()
        
        
        ## Statistics
        self.header(self.tr("Statistics"), 1)
        self.pageBreak()
        
        
    def metadata(self):
        self.doc.meta.addElement(odf.dc.Title(text=self.tr("Assets report")))
        self.doc.meta.addElement(odf.dc.Description(text=self.tr("This is an automatic generated report from Xulpymoney")))
        creator="Xulpymoney-{}".format(version)
        self.doc.meta.addElement(odf.meta.InitialCreator(text=creator))
        self.doc.meta.addElement(odf.dc.Creator(text=creator))
