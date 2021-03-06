import tkinter as tk
from tkinter import ttk
import tkcalendar as tc
from datetime import date

class vardrawing(tk.Widget):
    def __init__(self,name,window,vartype,posx,posy,tmpdict):
        self.name=name
        self.window=window
        if type(vartype)==list: self.vartype=vartype[0]
        else: self.vartype=vartype
        self.posx=posx
        self.posy=posy
        if type(vartype)==list:
            self.extra=vartype[1:]
        else:
            self.extra=[]
        self.tmpdict=tmpdict

        if vartype=="if":
            #print(type(tmpdict[name]))
            if type(tmpdict[name])==list:
                self.vartype=tmpdict[name][0]
                self.extra=tmpdict[name][1:]
            else:
                self.vartype=tmpdict[name]
                self.extra=[]


    def drawheading(self):
            heading = tk.Label(
                self.window,
                text="Zmienna "+str(self.name)+" typu: "+str(self.vartype),
                font=("Helvetica", 14),
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
            self.posy+=20

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
        
        if self.vartype=="CB":
            bodies=[]
            allvars=[]
            for option in self.extra:
                var = tk.StringVar()
                self.posy+=20
                body = tk.Checkbutton(
                    self.window,
                    text=option,
                    variable=var,
                    onvalue=option,
                    offvalue=''
                )
                body.pack()
                body.place(x=self.posx, y=self.posy, height=20, width=300)
                body.focus_set()

                allvars.append(var)
                #body.destroy()]
                bodies.append(body)
            

            
            return allvars, bodies

        if self.vartype=="SB":
            self.posy+=20
            body = tk.ttk.Combobox(
                    self.window,
                    values=self.extra,  
                    state="readonly",
                    takefocus=1  
                )
            body.pack()
            body.place(x=self.posx, y=self.posy, height=20, width=300)
            body.focus_set()
        
            return body, body

        if self.vartype=="IF":
            bodies=[]
            extravals=[]

            def returnDrawing():
                new = vardrawing(self.extra[1],self.window,"if",self.posx,self.posy-40,self.tmpdict)
                
                heading = new.drawheading()

                newvals, newbodies = new.drawbody()

                bodies.append(heading)
                bodies.append(newbodies)
                #bodies.append(newvals)

                increment=20

           
                if new.vartype=="CB":
                    extravals.extend(newvals)
                    bodies.extend(newbodies)
                elif new.vartype=="DT":
                    extravals.append(newvals)
                    bodies.extend(newbodies)
                elif new.vartype=="RC":
                    extravals.append(newvals)
                    bodies.extend(newbodies)
                elif new.vartype=="TN": ##todo if+TN
                    extravals.append(newvals)
                    bodies.extend(newbodies)
                elif new.vartype=="NB": ##todo if+NB
                    increment=40
                    extravals.append(newvals)
                    bodies.extend(newbodies)
                else:
                    extravals.append(newvals)
                    #bodies.extend(newbodies)

                body3 = tk.Button(
                self.window,
                text="zrezygnuj",
                command=destroyBodies,
                    )
                body3.pack()
                body3.place(x=new.posx, y=new.posy+increment, height=20, width=300)
                bodies.append(body3)


                
            
            def destroyBodies():
                for body in bodies[3:]:
                    if type(body)==list:
                        for draw in body:
                            try: 
                                draw.destroy()
                            except:
                                pass
                    else: 
                        try: 
                            body.destroy()
                        except:
                            pass
                        extravals.clear()

                

            self.posy+=20

            question = tk.Label(
                    self.window,
                    text=self.extra[0],
                    font=("Helvetica", 16),
                    bg='yellow'
                )
            question.pack()
            question.place(x=self.posx, y=self.posy, height=20, width=300)
            bodies.append(question)

            self.posy+=20
            body = tk.Button(
                    self.window,
                    text="Tak",
                    command=returnDrawing,
                )
            body.pack()
            body.place(x=self.posx, y=self.posy, height=20, width=150)
            bodies.append(body)
            
            body2 = tk.Button(
                    self.window,
                    text="Nie",
                    command=destroyBodies,
                )
            body2.pack()
            body2.place(x=self.posx+150, y=self.posy, height=20, width=150)
            bodies.append(body2)

            return extravals, bodies

        
        if self.vartype=="TN":
            bodies=[]

            var = tk.StringVar()
            var.set('')
      
            def destroyVars():
                var.set('')
                for body in bodies[3:]:
                    body.destroy()


            def returnPositive():
                try: 
                    var.set(self.extra[1])
                except:
                    var.set('Tak')

                body3 = tk.Button(
                        self.window,
                        text="zrezygnuj",
                        command=destroyVars,
                    )
                body3.pack()
                body3.place(x=self.posx, y=self.posy+20, height=20, width=300)
                bodies.append(body3)

            def returnNegative():
                try:
                    var.set(self.extra[2])
                except:
                    var.set('Nie')
                body3 = tk.Button(
                        self.window,
                        text="zrezygnuj",
                        command=destroyVars,
                    )
                body3.pack()
                body3.place(x=self.posx, y=self.posy+20, height=20, width=300)
                bodies.append(body3)

            self.posy+=20

            try:
                question = tk.Label(
                        self.window,
                        text=self.extra[0],
                        font=("Helvetica", 16),
                        bg='yellow'
                    )
                question.pack()
                question.place(x=self.posx, y=self.posy, height=20, width=300)
                bodies.append(question)
            except IndexError:
                question = tk.Label(
                        self.window,
                        text="Generyczna zmienna",
                        font=("Helvetica", 16),
                        bg='yellow'
                    )
                question.pack()
                question.place(x=self.posx, y=self.posy, height=20, width=300)
                bodies.append(question)


            self.posy+=20
            body = tk.Button(
                    self.window,
                    text="Tak",
                    command=returnPositive,
                )
            body.pack()
            body.place(x=self.posx, y=self.posy, height=20, width=150)
            bodies.append(body)
            
            body2 = tk.Button(
                    self.window,
                    text="Nie",
                    command=returnNegative,
                )
            body2.pack()
            body2.place(x=self.posx+150, y=self.posy, height=20, width=150)
            bodies.append(body2)

            return var, bodies

        if self.vartype=="DT":
            bodies=[]
            calendar = tk.StringVar()
            today = date.today().strftime("%d-%m-%y")
            calendar.set(today)

            self.posy+=20            
            self.question = tk.Label(
                    self.window,
                    text=calendar.get(),
                    font=("Helvetica", 16),
                    bg='yellow'
                    )
            self.question.pack()
            self.question.place(x=self.posx, y=self.posy, height=20, width=300)
            bodies.append(self.question)


            def redrawLabel(y,window=None):
                self.question.configure(text=calendar.get())
                bodies.append(self.question)
                if window:
                    window.destroy()


            def createCalendar():
                top = tk.Toplevel()
                x = self.window.winfo_x()
                y = self.window.winfo_y()
                top.geometry("+%d+%d" % (x + self.posx, y + self.posy))
                
                cal = tc.Calendar(
                    top,
                    font="Georgia 14",
                    selectmode='day',
                    locale="pl",
                    textvariable=calendar,
                    foreground="red",
                    selectforeground="red",
                    background="grey",
                    showweeknumbers=False,
                    )
                cal.pack(fill="both", expand=True)
                cal.bind('<<CalendarSelected>>',lambda event: redrawLabel(-20, top))
                #cal.bind('<<CalendarSelected>>',lambda event: top.destroy())

                # btn = tk.Button(
                #     top,
                #     text="ok",
                #     command=cal.selection_get)
                # btn.pack(fill="both",expand=True)

          

            self.posy+=20
            body = tk.Button(
                    self.window,
                    text="Ustaw",
                    command=createCalendar,
                    takefocus=1
                )
            body.pack()
            body.place(x=self.posx, y=self.posy, height=20, width=150)
            bodies.append(body)

            def deleteVar():
                calendar.set("")
                redrawLabel(-20)
            
            body2 = tk.Button(
                    self.window,
                    text="Zrezygnuj",
                    command=deleteVar,
                    takefocus=1
                )
            body2.pack()
            body2.place(x=self.posx+150, y=self.posy, height=20, width=150)
            bodies.append(body2)

            return calendar, bodies

        if self.vartype=="NB":
            self.posy+=20

            try:
                sc = tk.Scale(
                    self.window,
                    orient="horizontal",
                    from_=self.extra[0],
                    to=self.extra[1],
                    takefocus=1
                )
                sc.pack()
                sc.focus_set()
                sc.place(x=self.posx, y=self.posy, height=40, width=300)
                return sc, sc
            except IndexError:
                sc = tk.Scale(
                    self.window,
                    orient="horizontal",
                    from_=69,
                    to=666,
                    takefocus=1
                )
                sc.pack()
                sc.focus_set()
                sc.place(x=self.posx, y=self.posy, height=40, width=300)
                return sc, sc

        
        else:
            body = tk.Label(
                self.window,
                text="bledny typ zmiennej ",
                font=("Helvetica", 16),
                bg="red"
            )
            body.pack()
            body.place(x=self.posx, y=self.posy+20, height=20, width=300)
            return body, body
        
            

