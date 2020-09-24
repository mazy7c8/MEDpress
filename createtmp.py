import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Canvas, Frame



def template_window(self):
    self.window = tk.Toplevel()
    self.window.geometry("868x712")
    self.window.title("Tworz szablony")
    self.window['bg']=('#EFE3B8')




    titleentry = tk.Entry(
        self.window,
        bg='white',
    )
    titleentry.pack()
    titleentry.place(x=36,y=64,height=30,width=226)

    abbrentry = tk.Entry(
        self.window,
        bg='white',
    )
    abbrentry.pack()
    abbrentry.place(x=320,y=64,height=30,width=226)

    authorentry = tk.Entry(
        self.window,
        bg='white',
    )
    authorentry.pack()
    authorentry.place(x=600,y=64,height=30,width=226)

    textcode=tk.Text(
            self.window,
            bg='white',
        )
    textcode.pack()
    textcode.place(y=144,x=36,height=481,width=226)

    texttemplate=tk.Text(
            self.window,
            bg='white',
        )
    texttemplate.pack()
    texttemplate.place(y=144,x=320,height=481,width=226)

    textlegend=tk.Text(
            self.window,
            bg='white',
        )
    textlegend.pack()
    textlegend.place(y=144,x=600,height=481,width=226)




    btn = tk.Button(self.window, text="Close", command=self.frameHandler(self.window))
    btn.pack()