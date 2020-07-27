import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Canvas
window = tk.Tk()
window.geometry("1300x900")
window['bg']=('#FCAFAF')
pixelVirtual = tk.PhotoImage(width=1,height=1)

canvas = Canvas(width=1300,height=900,bg="#FCAFAF")
canvas.pack()
redsquare = canvas.create_rectangle(492,260,1287,884,fill="#ED6868")

title = tk.Label(text='MEDpress',font=("Helvetica", 18),bg=window['bg'])
title.pack()

button1 = tk.Button(
    text="Stwórz szablon",
    image=pixelVirtual,
    width=147,
    height=147,
    bg="#DCE19C",
    compound="c"
)
button1.place(y=44,x=79)

button2 = tk.Button(
    text="Wgraj z pliku",
    image=pixelVirtual,
    width=147,
    height=147,
    bg="#C0D9B7",
    compound="c"
)
button2.place(y=44,x=279)

button3 = tk.Button(
    text="Chmura szablonów",
    image=pixelVirtual,
    width=147,
    height=147,
    bg="#B2D4DC",
    compound="c"
)
button3.place(y=44,x=479)

textfield=tk.Text(
    bg='white',
)
textfield.place(y=44,x=714,height=147,width=573)

texfieldlabel = tk.Label(
    text="Wpisz skroty szablonow/gotowy tekst",
    font=("Helvetica", 16),
    bg=window['bg']
)
texfieldlabel.place(x=713,y=17,height=20,width=379)

Xbutton = tk.Button(
    text="X",
    image=pixelVirtual,
    width=40,
    height=40,
    bg="lightgrey",
    compound="c"
)
Xbutton.place(x=1241,y=44)

tree= ttk.Treeview()
tree["columns"]=("COL2","COL3")
tree.column("#0",width=100)
tree.heading("#0",text="Nazwa",anchor=tk.W)
tree.column("COL2",width=100)
tree.heading("COL2",text="Skrót",anchor=tk.W)
tree.column("COL3",width=100)
tree.heading("COL3",text="Data edycji",anchor=tk.W)

tree.insert('', 'end', 'ID1', text='Demo', values=("Demo","demo"))

tree.place(x=44,y=251,height=633,width=382)

treelabel = tk.Label(
    text="Twoje szablony",
    font=("Helvetica", 16),
    bg=window['bg']
)
treelabel.place(x=20,y=222,height=20,width=150)

editbutton = tk.Button(
    text="Edytuj w edytorze",
    image=pixelVirtual,
    width=100,
    height=15,
    bg="#DCE19C",
    compound="c"
)
editbutton.place(y=224,x=180)

savebutton = tk.Button(
    text="Zapisz do pliku",
    image=pixelVirtual,
    width=100,
    height=15,
    bg="#C0D9B7",
    compound="c"
)
savebutton.place(y=224,x=320)

startbutton = tk.Button(
    text="Rozpocznij wypis",
    image=pixelVirtual,
    width=131,
    height=32,
    bg="lightgrey",
    compound="c"
)
startbutton.place(x=840,y=201)

clipboardbutton = tk.Button(
    text="Do schowka",
    image=pixelVirtual,
    width=131,
    height=32,
    bg="lightgrey",
    compound="c"
)
clipboardbutton.place(x=998,y=201)

exportbutton = tk.Button(
    text="Eksport pdf/rtf",
    image=pixelVirtual,
    width=131,
    height=32,
    bg="lightgrey",
    compound="c"
)
exportbutton.place(x=1156,y=201)

progressbar= ttk.Progressbar(orient="horizontal", length=500, mode="determinate")
progressbar.place(x=511,y=853)
progressbar['value']=20

progresslabel = tk.Label(
    text="Szablon w kolejce 0/X",
    font=("Helvetica", 10),
    bg=("#ED6868")
)
progresslabel.place(x=1020,y=850)

backspacebutton = tk.Button(
    text="Cofnij etap",
    image=pixelVirtual,
    width=100,
    height=32,
    bg="lightgrey",
    compound="c"
)
backspacebutton.place(x=1175,y=839)

""" //////////////////////FRONTSCREEN/////////////////////////////"""





window.mainloop() 