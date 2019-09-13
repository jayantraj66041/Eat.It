import wx
from wx import *
import os
from datetime import datetime
app = App()
root = Frame(None, title="Eat.it",size=(1100,650))
root.Centre()
root.SetBackgroundColour("#D81B60")
panel = Panel(root)
mainbox = BoxSizer(VERTICAL)

top = BoxSizer(HORIZONTAL)
bottom = BoxSizer(HORIZONTAL)
time = StaticText(panel,1)
time.SetForegroundColour("white")
logo = StaticText(panel,1,label="Eat.it")
logo.SetForegroundColour("white")
font = Font(28,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)
logo.SetFont(font)

top.Add(logo,4,EXPAND|ALL,border=20)
top.Add(time,1,EXPAND|TOP,border=40)

t = Timer(root,1)
t.Start(100)
def on_timer(event):
    time.SetLabel(str(datetime.now()))
on_timer(None)
root.Bind(EVT_TIMER,on_timer)
left = BoxSizer(VERTICAL)
right = GridSizer(5,1,10,10)

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

display = TextCtrl(panel,style=TE_MULTILINE)

order = Button(panel,1,label="order")
order.Disable()
totals = Button(panel,1,label="total")
clear = Button(panel,1,label="clear")
setting = Button(panel,1,label="setting")
exits = Button(panel,1,label="exits")

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
os.chdir("orders")
def save(event):
    now = datetime.now()
    files = open(str(now.strftime("%Y%m%d%H%M%S"))+".txt",'w')
    files.write(display.GetValue())
    files.close()
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
    display.AppendText("----------------\nTotal \t"+str(total))
    display.AppendText("\n----------------\nGST(18%)\t"+str(gst))
    display.AppendText("\n----------------\nSub Total\t"+str(gst+total))
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

left.Add(recipes,3,ALL|EXPAND)
left.Add(display,1,EXPAND|TOP,border=10)

bottom.Add(left,3,EXPAND|ALL,border=20)
bottom.Add(right,1,TOP|BOTTOM|RIGHT|EXPAND,border=20)

mainbox.Add(top,0,ALL|EXPAND)
mainbox.Add(bottom,1,ALL|EXPAND)
panel.SetSizer(mainbox)
root.Show()
app.MainLoop()