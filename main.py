import tkinter as tk
window = tk.Tk()
window.geometry("1300x900")
window['bg']=('#FCAFAF')
pixelVirtual = tk.PhotoImage(width=1,height=1)

title = tk.Label(text='MEDpress')
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

window.mainloop() 