import wx
import wx.lib.agw.hyperlink as li
from wx import *
import os
from datetime import datetime
app = App()
root = Frame(None, title="Eat.it",size=(1100,650))
root.Centre()
root.SetBackgroundColour("#80CBC4")
panel = Panel(root)
mainbox = BoxSizer(VERTICAL)

top = BoxSizer(HORIZONTAL)
bottom = BoxSizer(HORIZONTAL)

logo = StaticBitmap(panel,-1,Bitmap("image/Food Stuff.png"))
font = Font(28,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL,FONTWEIGHT_BOLD)
d_font = Font(11,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL,FONTWEIGHT_BOLD)
fonts = Font(16,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)
small_font = Font(11,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)


top.Add(logo,4,EXPAND|ALL,border=20)


left = BoxSizer(VERTICAL)

recipes = GridSizer(3,3,10,10)


samosa = Button(panel,1,label="Samosa")
idli = Button(panel,1,label="idli")
sandwitch = Button(panel,1,label="sandwitch")
dosa = Button(panel,1,label="dosa")
momos = Button(panel,1,label="momos")
coke = Button(panel,1,label="coke")
rolls = Button(panel,1,label="rolls")
dhokla = Button(panel,1,label="dhokla")
icecream = Button(panel,1,label="icecream")
samosa.SetFont(fonts)
idli.SetFont(fonts)
sandwitch.SetFont(fonts)
dosa.SetFont(fonts)
momos.SetFont(fonts)
coke.SetFont(fonts)
rolls.SetFont(fonts)
dhokla.SetFont(fonts)
icecream.SetFont(fonts)
recipes.AddMany([
    (samosa,1,EXPAND|ALL),
    (idli,1,EXPAND|ALL),
    (sandwitch,1,EXPAND|ALL),
    (dosa,1,EXPAND|ALL),
    (momos,1,EXPAND|ALL),
    (coke,1,EXPAND|ALL),
    (rolls,1,EXPAND|ALL),
    (dhokla,1,EXPAND|ALL),
    (icecream,1,EXPAND|ALL)
])
left.Add(recipes,3,ALL|EXPAND)

display = TextCtrl(panel,style=TE_MULTILINE|TE_READONLY)
display.SetFont(small_font)

left.Add(display,1,EXPAND|TOP,border=10)

def close_window(event):
    root.Close()

def clear_display(event):
    display.SetValue("")
    global text
    text = ""
    global total
    total = 0
    samosa.Enable()
    sandwitch.Enable()
    order.Disable()
    dosa.Enable()
    idli.Enable()
    coke.Enable()
    totals.Enable()
    dhokla.Enable()
    icecream.Enable()
    momos.Enable()
    rolls.Enable()

def save(event):
    os.chdir("orders")
    now = datetime.now()
    files = open(str(datetime.now().strftime("%d-%m-%Y %H-%I-%S"))+".txt",'w')
    files.write(display.GetValue())
    files.close()
    viewframe = Frame(root,title="Order Details",size=(400,600))
    childpanel = Panel(viewframe)
    box = BoxSizer()
    viewbox = TextCtrl(childpanel,style=TE_MULTILINE|TE_READONLY)
    viewbox.SetValue(display.GetValue())
    box.Add(viewbox,1,ALL|EXPAND)
    childpanel.SetSizer(box)
    viewframe.Show()
    order.Disable()
    samosa.Enable()
    sandwitch.Enable()
    dosa.Enable()
    idli.Enable()
    coke.Enable()
    totals.Enable()
    dhokla.Enable()
    icecream.Enable()
    momos.Enable()
    rolls.Enable()

total = 0
text = ""
def setsamosa(event):
    global total
    global text
    text += "Samosa \t7/-\n"
    total += 7
    display.SetValue(text)

def setmomos(event):
    global total
    global text
    text += "Momos \t35/-\n"
    total += 35
    display.SetValue(text)

def seticecream(event):
    global total
    total += 150
    global text
    text += "Icecream \t 150/-\n"
    display.SetValue(text)

def setidli(event):
    global total
    total += 45
    global text
    text += "Idli \t 45/-\n"
    display.SetValue(text)

def setdosa(event):
    global total
    global text
    total += 50
    text += "Dosa \t50/-\n"
    display.SetValue(text)

def setroll(event):
    global total
    global text
    text += "Rolls \t40/-\n"
    total += 40
    display.SetValue(text)

def setdhokla(event):
    global total
    global text
    text += "Dhokla \t36/-\n"
    total += 36
    display.SetValue(text)

def setcoke(event):
    global total
    global text
    text += "Coke \t45/- \n"
    total += 45
    display.SetValue(text)

def setsandwitch(event):
    global total
    global text
    text += "Sandwitch \t15/-\n"
    total += 15
    display.SetValue(text)

def totals_value(event):
    global total
    gst = round(total*0.18)
    display.AppendText("----------------\nTotal \t"+str(total)+"/-")
    display.AppendText("\n----------------\nGST(18%)\t"+str(gst)+"/-")
    display.AppendText("\n----------------\nSub Total\t"+str(gst+total)+"/-")
    samosa.Disable()
    sandwitch.Disable()
    totals.Disable()
    order.Enable()
    dosa.Disable()
    idli.Disable()
    coke.Disable()
    dhokla.Disable()
    icecream.Disable()
    momos.Disable()
    rolls.Disable()

right = GridSizer(5,1,10,10)

order = Button(panel,1,label="order")
# order.SetBackgroundColour("#2E7D32")
# order.SetForegroundColour("white")
order.Disable()
totals = Button(panel,1,label="total")
clear = Button(panel,1,label="clear")
setting = Button(panel,1,label="setting")
setting.Disable()
exits = Button(panel,1,label="exits")
order.SetFont(fonts)
totals.SetFont(fonts)
clear.SetFont(fonts)
setting.SetFont(fonts)
exits.SetFont(fonts)

exits.Bind(EVT_BUTTON, close_window, exits)
clear.Bind(EVT_BUTTON, clear_display, clear)
samosa.Bind(EVT_BUTTON, setsamosa, samosa)
sandwitch.Bind(EVT_BUTTON, setsandwitch, sandwitch)
dosa.Bind(EVT_BUTTON, setdosa, dosa)
idli.Bind(EVT_BUTTON, setidli, idli)
coke.Bind(EVT_BUTTON, setcoke, coke)
dhokla.Bind(EVT_BUTTON, setdhokla, dhokla)
icecream.Bind(EVT_BUTTON, seticecream, icecream)
momos.Bind(EVT_BUTTON, setmomos, momos)
rolls.Bind(EVT_BUTTON, setroll, rolls)
totals.Bind(EVT_BUTTON, totals_value, totals)
order.Bind(EVT_BUTTON, save, order)

right.AddMany([
    (order,1,EXPAND|ALL),
    (totals,1,EXPAND|ALL),
    (clear,1,EXPAND|ALL),
    (setting,1,EXPAND|ALL),
    (exits,1,EXPAND|ALL)
])


bottom.Add(left,3,EXPAND|ALL,border=20)
bottom.Add(right,1,TOP|BOTTOM|RIGHT|EXPAND,border=20)
footer = BoxSizer(HORIZONTAL)
col1 = BoxSizer(VERTICAL)
col2 = BoxSizer(VERTICAL)
col3 = BoxSizer(VERTICAL)
footer.AddMany([
    (col1,2,EXPAND|ALL),
    (col2,2,EXPAND|ALL),
    (col3,1,EXPAND|ALL)
])

comp_name = StaticText(panel,label="CWS Lab..")
comp_address = StaticText(panel,label="Madhubani, Purnea")
comp_web = li.HyperLinkCtrl(panel,label="www.cws.co.in",URL="www.cws.co.in")
comp_contact = StaticText(panel,label="9060201899")
comp_support = StaticText(panel,label="support@cwslab.com")
comp_name.SetForegroundColour("white")
comp_address.SetForegroundColour("white")
comp_web.SetForegroundColour("white")
comp_web.SetBackgroundColour("#80CBC4")
comp_contact.SetForegroundColour("white")
comp_support.SetForegroundColour("white")
comp_name.SetFont(small_font)
comp_address.SetFont(small_font)
comp_web.SetFont(small_font)
comp_contact.SetFont(small_font)
comp_support.SetFont(small_font)

col1.Add(comp_name,0,EXPAND|ALL)
col1.Add(comp_address,0,EXPAND|ALL)
col1.Add(comp_web,0,EXPAND|ALL)
col1.Add(comp_contact,0,EXPAND|ALL)
col1.Add(comp_support,0,EXPAND|ALL)

name = StaticText(panel,label="Jayant Raj")
post = StaticText(panel,label="Software Developer")
contact = StaticText(panel,label="7322866041")
website = li.HyperLinkCtrl(panel,label="www.aboutjayant.epizy.com",URL="www.aboutjayant.epizy.com")
website.SetBackgroundColour("#80CBC4")
website.SetForegroundColour("white")
email = StaticText(panel,label="jayantraj66041@gmail.com")
name.SetForegroundColour("white")
post.SetForegroundColour("white")
contact.SetForegroundColour("white")
email.SetForegroundColour("white")
name.SetFont(small_font)
post.SetFont(small_font)
contact.SetFont(small_font)
website.SetFont(small_font)
email.SetFont(small_font)

col2.AddMany([
    (name,0,EXPAND|ALL),
    (post,0,EXPAND|ALL),
    (contact,0,EXPAND|ALL),
    (website,0,EXPAND|ALL),
    (email,0,EXPAND|ALL)
])

time = StaticText(panel)
time.SetForegroundColour("white")
time.SetFont(font)
date = StaticText(panel)
date.SetForegroundColour("white")
date.SetFont(d_font)
t = Timer(root,1)
t.Start(100)
def on_timer(event):
    time.SetLabel(str(datetime.now().strftime("%H:%I:%S")))
    date.SetLabel(str(datetime.now().strftime("%d/%m/%Y")))
on_timer(None)
root.Bind(EVT_TIMER,on_timer)
col3.Add(time,0,EXPAND|ALL)
col3.Add(date,0,EXPAND|ALL)
mainbox.Add(top,0,ALL|EXPAND)
mainbox.Add(bottom,1,ALL|EXPAND)
mainbox.Add(footer,0,EXPAND|LEFT|RIGHT|BOTTOM,border=20)
panel.SetSizer(mainbox)
root.Show()
root.ShowFullScreen(True)
app.MainLoop()
