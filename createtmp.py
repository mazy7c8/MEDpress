import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Canvas, Frame, INSERT, END
from item import ListItem, readTemplate
from jinja2schema import infer


def template_window(self,template):
    self.window = tk.Toplevel()
    self.window.geometry("868x712")
    self.window.title("Tworz szablony")
    self.window['bg'] = ('#EFE3B8')

    self.textaction=False

   

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

    def saveValues():
        value = titleentry.get()
        value2 = authorentry.get()
        value3 = textcode.get(1.0,END)
        ListItem.updateName(template,value)
        ListItem.writeAuthor(template,value2)
        if self.textaction==True: 
            ListItem.updateText(template,value3)

        print("updated")

    def textAction():
        self.textaction=True

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
    if template.author==None:
        template.author=ListItem.readAuthor(template)
    authorentry.insert(0,template.author)
    authorentry.place(x=600, y=64, height=30, width=226)

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
        plaincode = readTemplate(template)
        textcode.insert(INSERT,plaincode)
    except:
        pass

    textcode.pack()
    textcode.place(y=144, x=36, height=481, width=226)

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
    texttemplate.pack()
    try:
        texttemplate.insert(INSERT,infer(plaincode))
    except: 
        pass
    texttemplate.place(y=144, x=320, height=481, width=226)
    texttemplate.bind_all("<Key>", lambda event : textAction())

    
    legendlabel = tk.Label(
        self.window,
        text="Legenda",
        bg=self.window['bg'],
    )
    legendlabel.pack()
    legendlabel.place(x=600, y=120)

    textlegend = tk.Text(
        self.window,
        bg='white',
    )
    textlegend.pack()
    textlegend.place(y=144, x=600, height=481, width=226)

    generatebutton = tk.Button(
        self.window,
        text="Generuj kod",
        width=10,
        height=2,
        bg="lightgrey",
        command=None
    )
    generatebutton.pack()
    generatebutton.place(x=36, y=630)

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

    btn = tk.Button(
        self.window,
        text="Close",
        command=self.frameHandler(self.window)
        )
    btn.pack()

    