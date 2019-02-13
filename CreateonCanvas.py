#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import time
import random
import os
import json
import codecs
import csv #einstellungen
stand = "17.01.2019"
def printausgabe():
    print ((" ") + 53*"#")
    print (" # Python 3 Programm zum erzeugen Canvas Zeichnungen #")
    print ((" # Software Stand: ") + (stand) + ("                        #"))
    print (" # geschrieben von NAVARRA                           #")
    print (" # let my Software do it for YOU                     #")
    print ((" ") + 53*"#")
#printausgabe()
#from alexaaugenweiss import alexas_gesicht
bedienung = tk.Tk()
bedienung.wm_title("Create on Canvas")
bedienung.configure(background='black')
global XGROSS,YGROSS,XPOSbedienung,YPOSbedienung
XGROSS = int
XGROSS = 800
YGROSS = 480
XPOSbedienung = (XGROSS)
YPOSbedienung = 00

bedienung.geometry("+%d+%d" % (XPOSbedienung, YPOSbedienung))
#bedienung.geometry("%d %s %d" % (XGROSS,("x"), YGROSS))
bedienung.geometry("800x480")
bedienung.resizable(False, False)
bedienung.wm_overrideredirect(True)
#bedienung.wm_attributes("-topmost",1)
leeresblatt = tk.Tk()
leeresblatt.wm_title("Canvas Zeichenprogramm")
leeresblatt.configure(background='black')
#leeresblatt.wm_attributes('-transparentcolor',leeresblatt['bg'])
global XPOSleeresblatt,YPOSleeresblatt
XPOSleeresblatt = 0
YPOSleeresblatt = 0
leeresblatt.geometry("+%d+%d" % (XPOSleeresblatt, YPOSleeresblatt))
#leeresblatt.geometry("+%d+%d" % (XGROSS, YGROSS))
leeresblatt.geometry("800x480")
leeresblatt.resizable(False, False)
leeresblatt.wm_overrideredirect(True)
w = Canvas(leeresblatt, width=(XGROSS), height=(YGROSS))
w.pack()
b = Canvas(bedienung, width=(XGROSS), height=(YGROSS))
b.configure(background='black')
b.pack()
##koordinaten default kreis
global widthkordsysX,widthkordsysY,anzahlstricheX
global x,y,x1,x2,y1,y2
global x,y,yx1,y2,yy1,yy2
x1 = int
y1 = int
x2 = int
y2 = int
x  = 0
y  = 0
x1 = 0
y1 = 480
x2 = 0
y2 = 0
yx1 = 0
yy1 = 0
yx2 = 800
yy2 = 0
width_var = 5
fill_var = "black"
outline_var = ""
widthkordsysX = int
widthkordsysX = 10
widthkordsysY = 10
anzahlstricheX = int
anzahlstricheX = int(XGROSS/widthkordsysX)
anzahlstricheY = int
anzahlstricheY = int(YGROSS/widthkordsysY)
global background_var
background_var = "white"
#farben die zur auswahl stehen
global farb_palette
farb_palette = ['red','white','blue','green','orange','black','grey','yellow','pink']
##formen
formen_var = ""
sFilename = ('aktuell.csv')
#checkbox 
NewKordsysCheck = IntVar()
NewOvalCheck = IntVar()
NewRechteckCheck = IntVar()
NewLineCheck = IntVar()
dashCheck = IntVar()
global dash_var
dash_var = ""
global form_factor
form_factor = ""
global code
code = "bitte erst eine form auswählen"

def X1_plus():
    global x1
    x1 += 10    
def X1_minus():
    global x1
    x1 -= 10
def Y1_plus():
    global y1
    y1 += 10
def Y1_minus():
    global y1
    y1 -= 10
def X2_plus():
    global x2
    x2 += 10
def X2_minus():
    global x2
    x2 -= 10
def Y2_plus():
    global y2
    y2 += 10
def Y2_minus():
    global y2
    y2 -= 10
def Y_minus():
    global y1,y2
    y1 -= 10
    y2 -= 10    
def Y_plus():
    global y1,y2
    y1 += 10
    y2 += 10
def X_minus():
    global x1,x2
    x1 -= 10
    x2 -= 10
def X_plus():
    global x1,x2
    x1 += 10
    x2 += 10    
def width_plus():
    global width_var
    width_var +=1
def width_minus():
    global width_var
    width_var -=1

def widthkordsysX_plus():
    global widthkordsysX
    widthkordsysX +=1
def widthkordsysX_minus():
    global widthkordsysX
    widthkordsysX -=1
def widthkordsysY_plus():
    global widthkordsysY
    widthkordsysY +=1
def widthkordsysY_minus():
    global widthkordsysY
    widthkordsysY -=1
    
def somevar_plus():
    global LA_move_LR,RA_move_LR
    LA_move_LR +=10
    RA_move_LR +=10
def somevar_minus():
    global LA_move_LR,RA_move_LR
    LA_move_LR -=10
    RA_move_LR -=10
def somevar01_plus():
    global LA_move_UD,RA_move_UD
    LA_move_UD +=10
    RA_move_UD +=10
def somevar01_minus():
    global LA_move_UD,RA_move_UD
    LA_move_UD -=10
    RA_move_UD -=10
def code_ausgabe():
    global code
    if form_factor == "oval":
        code = (("w.create_oval(")+str(x1)+str(",")+str(y1)+(",")+str(x2)+(",")+str(y2)+str(", outline=") + ("'") + str(outline_var)+ ("'") + str(",width =")+ str(width_var)+(",")+("fill=")+ ("'") + str(fill_var) + ("'")+(")") + str("  ## Bemerkung:"))
    elif form_factor == "rechteck":
        code = (("w.create_rectangle(")+str(x1)+str(",")+str(y1)+(",")+str(x2)+(",")+str(y2)+str(", outline=") + ("'") + str(outline_var)+ ("'") + str(",width =")+ str(width_var)+(",")+("fill=")+ ("'") + str(fill_var) + ("'")+(")") + str("  ## Bemerkung:"))
    elif form_factor == "line":
        code = (("w.create_line(")+str(x1)+str(",")+str(y1)+(",")+str(x2)+(",")+str(y2)+ str(",width =")+ str(width_var)+(",")+("fill=")+ ("'") + str(fill_var) + ("'")+(")") + str("  ## Bemerkung:"))
    elif form_factor == "kordsys":
        code = (("w.create_line(")+str(x1)+str(",")+str(y1)+(",")+str(x2)+(",")+str(y2)+ str(",width =")+ str(width_var)+(",")+("fill=")+ ("'") + str(fill_var) + ("'")+(")") + str("  ## Bemerkung:"))
    command = 'echo ' + (code) + '| clip'
    os.system(command)
    print (code)
form_name = "aktuell"
activefill_var = "orange"
spare = "spare"


def alexas_gesicht():
    global x,y,x1,y1,x2,y2,anzahlstricheX,anzahlstricheY
    global yx1,y2,yy1,yy2
    #hintergrund farbe ändern
    w.configure(background=(background_var))
    #w.delete(ALL)
    b.delete(ALL)
    ##aktuelle werte in bedienung anzeigen
    b.create_text(270,240,text=(("x1:")+str(x1)),fill="red",font="arial")
    b.create_text(385,340,text=(("y1:")+str(y1)),fill="red",font="arial")
    b.create_text(510,240,text=(("x2:")+str(x2)),fill="red",font="arial")
    b.create_text(385,130,text=(("y2:")+str(y2)),fill="red",font="arial")
    b.create_text(230,380,text=((widthkordsysY)),fill="red",font="arial")
    b.create_text(230,410,text=((widthkordsysX)),fill="red",font="arial")
    b.create_text(230,440,text=((width_var)),fill="red",font="arial")
    global form_factor
    
    if NewKordsysCheck.get() ==1:
        global form_factor
        form_factor = "kordsys"
        
        if x == (anzahlstricheX):
            pass
        else:
            for x in range (0,(anzahlstricheX),1):
                x  += 1
                x1 += 10 + widthkordsysX
                x2 += 10 + widthkordsysX
                w.create_line((x1), (y1),(x2), (y2), width = (width_var), fill= str(fill_var), activefill= (activefill_var))
                
        
        if y == (anzahlstricheY):
            pass
        else:
        
            for y in range (0,(anzahlstricheY),1):
                y  += 1
                yy1 += 10 + widthkordsysY
                yy2 += 10 + widthkordsysY
                w.create_line((yx1), (yy1),(yx2), (yy2), width = (width_var), fill= str(fill_var), activefill= (activefill_var))
    
    elif NewOvalCheck.get() ==1:
        w.delete(ALL)
        w.create_oval((x1), (y1),(x2), (y2), outline= str(outline_var),width = str(width_var), fill= str(fill_var), activefill= 'orange') ## default kreis
        form_factor = "oval"
        
    elif NewRechteckCheck.get() ==1:
        w.delete(ALL)
        w.create_rectangle((x1), (y1),(x2), (y2), outline= str(outline_var),width = (width_var), fill= str(fill_var), activefill= (activefill_var))
        form_factor = "rechteck"
        
    elif dashCheck.get() ==1:
        w.delete(ALL)
        global dash_var
        dash_var = (1,1)
        w.create_line((x1), (y1),(x2), (y2), width = (width_var), dash = (dash_var), fill= str(fill_var), activefill= (activefill_var))
        
    elif NewLineCheck.get() ==1:
        w.delete(ALL)
        w.create_line((x1), (y1),(x2), (y2), width = (width_var), fill= str(fill_var), activefill= (activefill_var))
        form_factor = "line"
        
    else:
        pass
    
    bedienung.after(200, alexas_gesicht)
def exit():
    leeresblatt.destroy()
    bedienung.destroy()
##einzelne punkte bewegen
X1plus   = Button(bedienung, text='X1+',command=lambda: X1_plus(),  width=3, height=1, bg='black', fg='red').place(x=430,y=210);
X1minus  = Button(bedienung, text='X1-',command=lambda: X1_minus(), width=3, height=1, bg='black', fg='red').place(x=325,y=210);
Y1plus   = Button(bedienung, text='Y1+',command=lambda: Y1_plus(),  width=3, height=1, bg='black', fg='red').place(x=360,y=270);
Y1minus  = Button(bedienung, text='Y1-',command=lambda: Y1_minus(), width=3, height=1, bg='black', fg='red').place(x=360,y=180);
Y2plus   = Button(bedienung, text='Y2+',command=lambda: Y2_plus(),  width=3, height=1, bg='black', fg='red').place(x=395,y=270);
Y2minus  = Button(bedienung, text='Y2-',command=lambda: Y2_minus(), width=3, height=1, bg='black', fg='red').place(x=395,y=180);
X2plus   = Button(bedienung, text='X2+',command=lambda: X2_plus(),  width=3, height=1, bg='black', fg='red').place(x=430,y=240);
X2minus  = Button(bedienung, text='X2-',command=lambda: X2_minus(), width=3, height=1, bg='black', fg='red').place(x=325,y=240);
#breite ändern
widthminus  = Button(bedienung, text='width-',command=lambda: width_minus(), width=7, height=1, bg='black', fg='red').place(x=150,y=430);
widthplus   = Button(bedienung, text='width+',command=lambda: width_plus(),  width=7, height=1, bg='black', fg='red').place(x=250,y=430);
#breite des koordinaten system ändern
widthminuskordsysX  = Button(bedienung, text='width X -',command=lambda: widthkordsysX_minus(), width=7, height=1, bg='black', fg='red').place(x=150,y=400);
widthpluskordsysX   = Button(bedienung, text='width X +',command=lambda: widthkordsysX_plus(),  width=7, height=1, bg='black', fg='red').place(x=250,y=400);
widthminuskordsysY  = Button(bedienung, text='width Y -',command=lambda: widthkordsysY_minus(), width=7, height=1, bg='black', fg='red').place(x=150,y=370);
widthpluskordsysY   = Button(bedienung, text='width Y +',command=lambda: widthkordsysY_plus(),  width=7, height=1, bg='black', fg='red').place(x=250,y=370);

#verschiedene variablen ändern
somevarminus  = Button(bedienung, text='links ',command=lambda: somevar_minus(), width=7, height=1, bg='black', fg='red').place(x=590,y=430);
somevarplus   = Button(bedienung, text='rechts',command=lambda: somevar_plus(),  width=7, height=1, bg='black', fg='red').place(x=710,y=430);
somevar01minus  = Button(bedienung, text='hoch ',command=lambda: somevar01_minus(), width=7, height=1, bg='black', fg='red').place(x=650,y=400);
somevar01plus   = Button(bedienung, text='runter',command=lambda: somevar01_plus(),  width=7, height=1, bg='black', fg='red').place(x=650,y=450);
##ganzes object bewegen
Yminus  = Button(bedienung, text='Y-',command=lambda: Y_minus(), width=7, height=1, bg='black', fg='red').place(x=365,y=150);
Yplus   = Button(bedienung, text='Y+',command=lambda: Y_plus(),  width=7, height=1, bg='black', fg='red').place(x=360,y=300);
Xplus   = Button(bedienung, text='X+',command=lambda: X_plus(),  width=2, height=3, bg='black', fg='red').place(x=460,y=210);
Xminus  = Button(bedienung, text='X-',command=lambda: X_minus(), width=2, height=3, bg='black', fg='red').place(x=300,y=210);
#komplettes koordinaten system
Checkbutton(bedienung, text=("Koordinaten"),variable    =NewKordsysCheck,font="Helvetica 11 bold italic",bg='black', fg='red') .place(x=10,y=380);
#neues oval dazu schalten
Checkbutton(bedienung, text=("Oval"),       variable    =NewOvalCheck,font="Helvetica 11 bold italic",bg='black', fg='red')    .place(x=10,y=400);
#neues rechteck dazu schalten
Checkbutton(bedienung, text=("Rechteck"),   variable    =NewRechteckCheck,font="Helvetica 11 bold italic",bg='black', fg='red').place(x=10,y=420);
#neue linie dazu schalten
Checkbutton(bedienung, text=("Linie"),      variable    =NewLineCheck,font="Helvetica 11 bold italic",bg='black', fg='red')    .place(x=10,y=440);
#linie gestrichelt
Checkbutton(bedienung, text=("Dash"),       variable    =dashCheck,font="Helvetica 11 bold italic",bg='black', fg='red')       .place(x=80,y=440);
#fill farbe festlegen
tkvarfill = StringVar(bedienung)
fill = (farb_palette)
tkvarfill.set('')
popupMenufill = OptionMenu(bedienung, tkvarfill, *fill)
Label(bedienung, text="fill", bg='black', fg='red',font="Helvetica 11 bold italic").place(x=110,y=20);
popupMenufill.place(x=20,y=20);
def change_dropdown_fill(*args):
    #print( tkvarfill.get() )
    global fill_var
    fill_var=( tkvarfill.get())
tkvarfill.trace('w', change_dropdown_fill)
#outline farbe festlegen
tkvaroutline = StringVar(bedienung)
outline = (farb_palette)
tkvaroutline.set('')
popupMenuoutline = OptionMenu(bedienung, tkvaroutline, *outline)
Label(bedienung, text="outline", bg='black', fg='red',font="Helvetica 11 bold italic").place(x=260,y=20);
popupMenuoutline.place(x=180,y=20);
def change_dropdown_outline(*args):
    #print( tkvaroutline.get() )
    global outline_var
    outline_var=( tkvaroutline.get())
tkvaroutline.trace('w', change_dropdown_outline)

#background farbe festlegen
tkvarbackground = StringVar(bedienung)
background = (farb_palette)
tkvarbackground.set('')
popupMenubackground = OptionMenu(bedienung, tkvarbackground, *background)
Label(bedienung, text="background", bg='black', fg='red',font="Helvetica 11 bold italic").place(x=480,y=20);
popupMenubackground.place(x=400,y=20);
def change_dropdown_background(*args):
    #print( tkvarbackground.get() )
    global background_var
    background_var=( tkvarbackground.get())
tkvarbackground.trace('w', change_dropdown_background)

#form zum speichern wählen
tkvarformen = StringVar(bedienung)
formen = [ 'form_1','form_2','form_3','form_4','form_5','form_6','form_7','']
tkvarformen.set('')
popupMenuformen = OptionMenu(bedienung, tkvarformen, *formen)
Label(bedienung, text="object", bg='black', fg='red',font="Helvetica 11 bold italic").place(x=100,y=50);
popupMenuformen.place(x=20,y=50);
def change_dropdown_formen(*args):
    #print( tkvarformen.get() )
    global formen_var
    formen_var=( tkvarformen.get())
tkvarformen.trace('w', change_dropdown_formen)
EXITButton = Button(bedienung, text='EXIT',command=lambda: exit(),         width=8, height=3, bg='black', fg='red').place(x=360,y=210);
CODEButton = Button(bedienung, text='CODE',command=lambda: code_ausgabe(), width=8, height=3, bg='black', fg='red').place(x=360,y=350);
#SAVEButton = Button(bedienung, text='SAVE',command=lambda: einstellungen_speichern(sFilename), width=8, height=3, bg='black', fg='red').place(x=460,y=350);
Label(bedienung, text="NAVARRA", bg='black', fg='red',font="Helvetica 11 bold italic").place(x=650,y=20);
Label(bedienung, text="let my Software do it for you", bg='black', fg='red',font="Helvetica 7 bold italic").place(x=650,y=40);
alexas_gesicht()
bedienung.mainloop()