import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Canvas, Frame
import keyboard
from template import *


class MEDpress(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("Ekran Glowny")
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.root['bg']="#FCAFAF"
        

        canvas = Canvas(self.frame,width=1300,height=900,bg="#FCAFAF")
        canvas.create_rectangle(492,260,1287,884,fill="#ED6868")
        canvas.pack()

        button1 = tk.Button(
            self.frame,
            text="Stwórz szablon",
            width=20,
            height=10,
            bg="#DCE19C",
            command=self.openFrame
        )
        button1.pack()
        button1.place(y=44,x=79)
        
        
        button2 = tk.Button(
            self.frame,
            text="Wgraj z pliku",
            width=20,
            height=10,
            bg="#C0D9B7",
        )
        button2.pack()
        button2.place(y=44,x=279)

        button3 = tk.Button(
            self.frame,
            text="Chmura szablonów",
            width=20,
            height=10,
            bg="#B2D4DC",
        )
        button3.pack()
        button3.place(y=44,x=479)

        textfield=tk.Text(
            self.frame,
            bg='white',
        )
        textfield.pack()
        textfield.place(y=44,x=714,height=147,width=573)

        texfieldlabel = tk.Label(
            self.frame,
            text="Wpisz skroty szablonow/gotowy tekst",
            font=("Helvetica", 16),
            bg=self.root['bg']
        )
        texfieldlabel.pack()
        texfieldlabel.place(x=713,y=17,height=20,width=379)

        Xbutton = tk.Button(
            self.frame,
            text="X",
            width=4,
            height=2,
            bg="lightgrey",
        )
        Xbutton.pack()
        Xbutton.place(x=1250,y=44)

        tree= ttk.Treeview()
        tree["columns"]=("COL2","COL3")
        tree.column("#0",width=100)
        tree.heading("#0",text="Nazwa",anchor=tk.W)
        tree.column("COL2",width=100)
        tree.heading("COL2",text="Skrót",anchor=tk.W)
        tree.column("COL3",width=100)
        tree.heading("COL3",text="Data edycji",anchor=tk.W)

        tree.insert('', 'end', 'ID1', text='Demo', values=("Demo","demo"))
        tree.pack()
        tree.place(x=44,y=251,height=633,width=382)

        treelabel = tk.Label(
            self.frame,
            text="Twoje szablony",
            font=("Helvetica", 16),
            bg=self.root['bg']
        )
        treelabel.pack()
        treelabel.place(x=20,y=222,height=20,width=150)

        editbutton = tk.Button(
            self.frame,
            text="Edytuj w edytorze",
            width=14,
            height=1,
            bg="#DCE19C",
        )
        editbutton.pack()
        editbutton.place(y=224,x=180)

        savebutton = tk.Button(
            self.frame,
            text="Zapisz do pliku",
            width=14,
            height=1,
            bg="#C0D9B7",
        )
        savebutton.pack()
        savebutton.place(y=224,x=320)

        startbutton = tk.Button(
            self.frame,
            text="Rozpocznij wypis",
            width=14,
            height=2,
            bg="lightgrey",
        )
        startbutton.pack()
        startbutton.place(x=840,y=201)

        clipboardbutton = tk.Button(
            self.frame,
            text="Do schowka",
            width=14,
            height=2,
            bg="lightgrey",
        )
        clipboardbutton.pack()
        clipboardbutton.place(x=998,y=201)

        exportbutton = tk.Button(
            self.frame,
            text="Eksport pdf/rtf",
            width=14,
            height=2,
            bg="lightgrey",
        )
        exportbutton.pack()
        exportbutton.place(x=1156,y=201)
        progressbar= ttk.Progressbar(self.frame,orient="horizontal", length=500, mode="determinate")
        progressbar.pack()
        progressbar.place(x=511,y=853)
        progressbar['value']=20

        progresslabel = tk.Label(
            self.frame,
            text="Szablon w kolejce 0/X",
            font=("Helvetica", 10),
            bg=("#ED6868")
        )
        progresslabel.pack()
        progresslabel.place(x=1020,y=850)

        backspacebutton = tk.Button(
            self.frame,
            text="Cofnij etap",
            width=10,
            height=2,
            bg="lightgrey",
        )
        backspacebutton.pack()
        backspacebutton.place(x=1175,y=839)

    
    def hide(self):
        self.root.withdraw()
        
    def openFrame(self):
        self.hide()
        template_window(self)

    def frameHandler(self, otherFrame):
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        return handler

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()
        
    def show(self):
        self.root.update()
        self.root.deiconify()
        

    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x900")
    app = MEDpress(root)
    root.mainloop()

