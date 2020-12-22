import tkinter as tk

class vardrawing(tk.Widget):
    def __init__(self,name,window,vartype,posx,posy,*args):
        self.name=name
        self.window=window
        self.vartype=vartype
        self.posx=posx
        self.posy=posy
        self.extra=list(args)


    def drawheading(self):
            heading = tk.Label(
                self.window,
                text="Zmienna "+str(self.name)+" typu:"+str(self.vartype),
                font=("Helvetica", 16),
                bg=self.window["bg"]
            )
            heading.pack()
            heading.place(x=self.posx, y=self.posy, height=20, width=300)

            return heading
        
    
    def drawbody(self):
        if self.vartype=='TX':
            body = tk.Entry(
                self.window,
            )
            body.pack()
            body.place(x=self.posx, y=self.posy+20, height=20, width=300)
            body.focus_set()

            return body
        
        else:
            body = tk.Label(
                self.window,
                text="bledny typ zmiennej ",
                font=("Helvetica", 16),
                bg="red"
            )
            body.pack()
            body.place(x=self.posx, y=self.posy+20, height=20, width=300)
            return body
            




