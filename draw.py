import tkinter as tk

class vardrawing(tk.Widget):
    def __init__(self,name,window,vartype,posx,posy,tmpdict):
        self.name=name
        self.window=window
        if type(vartype)==list: self.vartype=vartype[0]
        else: self.vartype=vartype
        self.posx=posx
        self.posy=posy
        self.extra=vartype[1:]
        self.tmpdict=tmpdict

        if vartype=="if":
            self.vartype=tmpdict[name][0]
            self.extra=tmpdict[name][1:]


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
                    state="readonly"    
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
                bodies.append(newvals)

                body3 = tk.Button(
                        self.window,
                        text="zrezygnuj",
                        command=destroyBodies,
                    )
                body3.pack()
                body3.place(x=new.posx, y=new.posy+20, height=20, width=300)
                bodies.append(body3)

                if new.vartype=="CB": 
                    extravals.extend(newvals)
                    bodies.extend(newbodies)
                else:
                    extravals.append(newvals)

                
            
            def destroyBodies():
                for body in bodies[3:]:
                    if type(body)==list:
                        for draw in body:
                            try: 
                                draw.destroy()
                            except:
                                pass
                    else: 
                        body.destroy()
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
        
            




