from os import write
import tkinter as tk
from tkinter import font
from tkinter.constants import LEFT
import tkinter.ttk as ttk
from tkinter import Canvas, Frame, INSERT, END
from item import ListItem, readHeader, readTemplate, readBody, writeToFile
import json
from idlelib.tooltip import Hovertip
import re
import ast


def template_window(self,template):
    #print(template)
    self.window = tk.Toplevel()
    self.window.geometry("868x712")
    self.window.title("Tworz szablony")
    self.window['bg'] = ('#EFE3B8')
    self.window.protocol("WM_DELETE_WINDOW", self.frameHandler(self.window))
    #self.window.protocol("WM_DELETE_WINDOW", self.window.destroy())

    self.textaction=False
    self.varaction=False
    self.nameaction=False
    self.authoraction=False

    legend = """TX = standardowa
zmienna tekstowa

RC = przyciski wyboru typu
radio jednokrotnego wyboru

CB = przyciski typu combo
multi wyboru

SB = lista typu wybierz jedno

IF = jezeli tak to zmienna

TN = pytanie, prawda, falsz

DT = widżet daty

NB = widżet liczby"""


    def nameAction():
        self.nameaction=True

    titlelabel = tk.Label(
        self.window,
        text="Tytuł",
        bg=self.window['bg'],
    )
    titlelabel.pack()
    titlelabel.place(x=36, y=40)

    titleentry = tk.Entry(
        self.window,
        bg='white',
    )
    titleentry.pack()
    titleentry.insert(0,template.name)
    titleentry.place(x=36, y=64, height=30, width=226)
    titleentry.bind("<Key>", lambda event : nameAction())

    myTip1=Hovertip(titleentry,"Tutaj mozen zmienic nazwę pliku")

    def saveValues():
        savebutton.config(bg="#00FF00")
        self.root.after(100, lambda: savebutton.config(bg='lightgrey'))

        value = titleentry.get()
        value2 = authorentry.get()
        value3 = textcode.get(1.0,END)
        value4 = texttemplate.get(1.0,END)
        
        if self.textaction==True: 
            #ListItem.updateText(template,value3)
            #template.updateText(value3)
            template.body=value3
            writeToFile(template,template.header,value3)
            print("textaction")

        if self.varaction==True:
            #ListItem.writeVars(template,value4,value2)
            template.dictionary=ast.literal_eval(value4)
            template.header=value4
            writeToFile(template,value4,template.body)
            print("varaction")

        
        if self.nameaction==True:
            ListItem.updateName(template,value)
            print("nameaction")

        if self.authoraction==True:
            print("authoraction")
            ListItem.writeAuthor(template,value2)

    def textAction():
        self.textaction=True

    def varAction():
        self.varaction=True

    def authorAction():
        self.authoraction=True

    abbrlabel = tk.Label(
        self.window,
        text="Skrót",
        bg=self.window['bg'],
    )
    abbrlabel.pack()
    abbrlabel.place(x=320, y=40)

    abbrentry = tk.Entry(
        self.window,
        bg='white',
    )
    abbrentry.pack()
    abbrentry.insert(0,template.abbr)
    abbrentry.place(x=320, y=64, height=30, width=226)
    myTip2=Hovertip(abbrentry,"Tutaj mozesz zdefiniowac customowy skrot")

    authorlabel = tk.Label(
        self.window,
        text="Autor",
        bg=self.window['bg'],
    )
    authorlabel.pack()
    authorlabel.place(x=600, y=40)

    authorentry = tk.Entry(
        self.window,
        bg='white',
    )
    authorentry.pack()
    #if template.author==None:
        #template.author=ListItem.readAuthor(template)
    authorentry.insert(0,template.author)
    authorentry.place(x=600, y=64, height=30, width=226)
    authorentry.bind("<Key>", lambda event : authorAction())
    myTip3=Hovertip(authorentry,"Tutaj wpisz swoje imie jezeli chcesz")

    codelabel = tk.Label(
        self.window,
        text="Tekst szablonu",
        bg=self.window['bg'],
    )
    codelabel.pack()
    codelabel.place(x=36, y=120)

    textcode = tk.Text(
        self.window,
        bg='white',
    )

    try:
        plaincode = readBody(template,None)
        textcode.insert(INSERT,plaincode)
    except:
        plaincode = readTemplate(template)
        textcode.insert(INSERT,plaincode)

    textcode.pack()
    textcode.place(y=144, x=36, height=481, width=226)
    textcode.bind("<Key>", lambda event : textAction())
    myTip4=Hovertip(textcode,"To tekst szablonu wraz z nagłówkiem, możesz dodawać zmienne")

    templatelabel = tk.Label(
        self.window,
        text="Kod szablonu",
        bg=self.window['bg'],
    )
    templatelabel.pack()
    templatelabel.place(x=320, y=120)

    texttemplate = tk.Text(
        self.window,
        bg='white',
    )
    try:
        texttemplate.insert(INSERT,template.dictionary)

    except: 
        pass

    texttemplate.pack()
    texttemplate.place(y=144, x=320, height=481, width=226)
    texttemplate.bind("<Key>", lambda event : varAction())
    myTip5=Hovertip(texttemplate,"Tutaj zdefiniuj każdą ze zmiennych wg własnych potrzeb")


    
    legendlabel = tk.Label(
        self.window,
        text="Legenda",
        bg=self.window['bg'],
    )
    legendlabel.pack()
    legendlabel.place(x=600, y=120)

    textlegend = tk.Label(
        self.window,
        bg=self.window['bg'],
        text=legend,
        font=("Helvetica", 14),
        justify=LEFT
    )
    textlegend.pack()
    textlegend.place(y=144, x=600)
    #textlegend.insert(INSERT, legend)
    myTip6=Hovertip(textlegend,"To są skroty zmiennych ktore wykorzystasz w polu z lewej")

    def generateVars():
        newListItem = ListItem(template.name,None,None)
        newListItem.updateText(textcode.get(1.0,END))
        new = newListItem.makeDict(template.name)
        texttemplate.delete('1.0', END)
        texttemplate.insert(INSERT,new)
        #self.varaction=True
        #aveValues()



    generatebutton = tk.Button(
        self.window,
        text="Generuj kod",
        width=10,
        height=2,
        bg="lightgrey",
        command=generateVars
    )
    generatebutton.pack()
    generatebutton.place(x=36, y=630)
    myTip7=Hovertip(generatebutton,"Wygeneruj kod szablonu dla nowych zmiennych")

    savebutton = tk.Button(
        self.window,
        text="Zapisz szablon",
        width=15,
        height=2,
        bg="lightgrey",
        command=saveValues
        )
    savebutton.pack()
    savebutton.place(x=600, y=630)
    myTip8=Hovertip(savebutton,"Zapisz wszystkie zmiany")
    self.window.bind("<Control-s>",  lambda event, : saveValues ())

    keyinfolabel = tk.Label(
            self.window,
            text="Ctrl+s zapisz zmiany",
            font=("Georgia", 10),
            bg=self.window['bg']
        )
    keyinfolabel.pack()
    keyinfolabel.place(x=600, y=600, height=20, width=150)




    btn = tk.Button(
        self.window,
        text="Close",
        command=self.frameHandler(self.window)
        )
    btn.pack()

    