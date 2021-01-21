import datetime
import os, os.path
import time
import re
from tkinter import messagebox, Toplevel,Label,Button
from tkinter.constants import LEFT
import traceback, sys
from typing import Type
from jinja2schema import infer, to_json_schema
import ast

class ListItem(object):
    def __init__(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name
        self.author=self.readAuthor()
        self.dictionary=self.makeDict(self.name)
        self.header=readHeader(self,self.name)
        self.body=readBody(self,self.name)

    def updateInstance(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name


    def makeDict(self,name):
        if name!="":
            data = open(os.path.join("szablony",name+".txt"),"r",encoding="utf-8")
            plaincode = data.read()
            schema = infer(plaincode)
            #schema = (json.dumps(schema,indent=3))
            for item in schema.keys():
                schema.__setitem__(item,"TX")

            with open(os.path.join("szablony",name+".txt"),'r+') as f:
                f.seek(0, 0)
                firstline = f.readline()
                if firstline.startswith('###'):
                    hardcodeddict = re.search(r'(?<=\{)(.*?)(?=\})',firstline)
                    if hardcodeddict != None:
                        decodeddict = dict(ast.literal_eval('{'+hardcodeddict.group()+'}'))
                        diff = set(schema.keys()) - set(decodeddict.keys())
                        #print(diff,list(diff))
                        if not list(diff):
                            return decodeddict
                        else: 
                            print('dodano zmnienno')
                            for item in diff:
                                decodeddict[item]="TX"
                            return decodeddict
            
            return schema
        pass

    def updateName(self,var):
        os.rename(os.path.join("szablony",self.name+".txt"),os.path.join("szablony",var+".txt"))

    def readAuthor(self):
        try:
            with open(os.path.join("szablony",self.name+".txt"),'r+') as f:
                content = f.read()
                f.seek(0, 0)
                firstline = f.readline()
                f.close()
                if firstline.startswith('###'):
                    firstline=re.search('author=(\w+)',firstline)
                    #firstline.split("=")
                return firstline.groups()
        except:
            return ("nieznany")
        

    def writeAuthor(self,var):
        self.author=var
        infoline="### author="+var
        with open(os.path.join("szablony",self.name+".txt"),'r+') as f:
            content = f.read()
            f.seek(0, 0)
            firstline = f.readline()
            if firstline.startswith('###'):
               firstline=re.sub('author=[a-z]*',"author="+self.author,firstline)
               f.seek(0, 0)
               f.readline()
               content=f.read()
               f.seek(0,0)
               f.write(firstline + content)
               f.close()
            else:
                print("dodano autora")
                f.seek(0, 0)
                f.write(infoline.rstrip('\r\n') +'\n'+'\n'+ content)
                f.close()
    
    def updateText(self,var):
        with open(os.path.join("szablony",self.name+".txt"),'r+',encoding="utf-8") as f:
            f.truncate(0)
            f.seek(0,0)
            f.write(var)
            f.close()

    def writeVars(self,vars,aut):
        try:
            self.dictionary = ast.literal_eval(vars)
           
            varline=str(vars)
            varline=varline.strip('\n')
            varline=varline.strip('\r')
            with open(os.path.join("szablony",self.name+".txt"),'r+') as f:
                content = f.read()
                f.seek(0, 0)
                firstline = f.readline()
                if firstline.startswith('###'):
                    firstline="### author="+aut+" "+varline+'\n'
                    f.seek(0, 0)
                    f.readline()
                    content=f.read()
                    f.seek(0,0)
                    f.write(firstline + content)
                    f.close()
                else:
                    print("bez naglowka")
                    f.seek(0, 0)
                    content=f.read()
                    f.seek(0, 0)
                    firstline="### author="+aut+" "+varline+'\n'
                    f.write(firstline +'\n'+ content)
                    f.close()
        
        except SyntaxError as e:
            error = traceback.format_exc()
            #messagebox.showinfo("blad skladni", error)
            window = Toplevel()

            label = Label(window, text=error, font="Consolas 10",justify=LEFT)
            label.pack(fill='x', padx=20, pady=100)

            button_close = Button(window, text="Zamknij", command=window.destroy,)
            button_close.pack(fill='x')
            button_close.config(bg='red')
        
        


def readFolder():
    file_list = os.listdir("szablony")
    data=()

    for file_name in file_list:
        with open(os.path.join("szablony", file_name), "r") as src_file:
            txttime = time.ctime(os.path.getctime(src_file.name))
            data += ((src_file.name, file_name, txttime),)

    return data

def readTemplate(template):
    data = open(os.path.join("szablony",template.name+".txt"),"r",encoding="utf-8")
    #data.readline()
    return data.read()

def readHeader(template,name):
    if name!="":
        try:
            data=open(os.path.join("szablony",template.name+".txt"),"r",encoding="utf-8")
        except FileNotFoundError:
            data=open(os.path.join("szablony",name+".txt"),"r",encoding="utf-8")

        readed=data.read()
        data.seek(0,0)
        firstline=data.readline()
        if firstline.startswith('###'):
            stripped = re.search(r'###.*\n', readed)
            return stripped.group(0)
        else:
            return ''
            

def readBody(template,name):
    if name!="":
        try:
            data=open(os.path.join("szablony",template.name+".txt"),"r",encoding="utf-8")
        except FileNotFoundError:
            data=open(os.path.join("szablony",name+".txt"),"r",encoding="utf-8")

        readed = data.read()
        data.seek(0, 0)
        firstline = data.readline()
        if firstline.startswith('###') or firstline.startswith('{'):
            stripped = re.search(r'\n\n.*', readed)
            stripped = re.sub(r'^$\n', '', stripped.group(0), flags=re.MULTILINE)
            return stripped
        else:
            return readed


def writeToFile(template,header,body):
    with open(os.path.join("szablony",template.name+".txt"),'r+',encoding="utf-8") as f:
            f.truncate(0)
            f.seek(0,0)
            whole = header+'\n'+body
            f.write(whole)
            f.close()

