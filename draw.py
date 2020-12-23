import tkinter as tk

class vardrawing(tk.Widget):
    def __init__(self,name,window,vartype,posx,posy,*args):
        self.name=name
        self.window=window
        if type(vartype)==list: self.vartype=vartype[0]
        else: self.vartype=vartype
        self.posx=posx
        self.posy=posy
        self.extra=vartype[1:]


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

            return body, body

        if self.vartype=="RC":
            var = tk.StringVar()
            bodies=[]
            for option in self.extra:
                self.posy+=20
                body = tk.Radiobutton(
                    self.window,
                    text=option,
                    variable=var,
                    value=option
                )
                body.pack()
                body.place(x=self.posx, y=self.posy, height=20, width=300)
                body.focus_set()
                #body.destroy()]
                bodies.append(body)

            return var, bodies
        
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
            




