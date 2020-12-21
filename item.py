import datetime
import os, os.path
import time
import re
from jinja2schema import infer, to_json_schema
import ast

class ListItem(object):
    def __init__(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name
        self.author=None
        self.dictionary=self.makeDict(self.name)

    def updateInstance(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name


    def makeDict(self,name):
        if name!="":
            with open(os.path.join("szablony",name+".txt"),'r+') as f:
                f.seek(0, 0)
                firstline = f.readline()
                if firstline.startswith('###'):
                    hardcodeddict = re.search(r'(?<=\{)(.*?)(?=\})',firstline)
                    if hardcodeddict != None:
                        return ast.literal_eval('{'+hardcodeddict.group()+'}')
            
            data = open(os.path.join("szablony",name+".txt"),"r",encoding="utf-8")
            plaincode = data.read()
            schema = infer(plaincode)
            #schema = (json.dumps(schema,indent=3))
            for item in schema.keys():
                schema.__setitem__(item,"TX")
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
                if firstline.startswith('###'):
                    firstline=re.search('author=(\w+)',firstline)
                    #firstline.split("=")
                return firstline.groups()
        except:
            return ("noname")
        

    def writeAuthor(self,var):
        infoline="### author="+var
        with open(os.path.join("szablony",self.name+".txt"),'r+') as f:
            content = f.read()
            f.seek(0, 0)
            firstline = f.readline()
            if firstline.startswith('###'):
               firstline=re.sub('author=[a-z]*',"author="+var,firstline)
               f.seek(0, 0)
               f.readline()
               content=f.read()
               f.seek(0,0)
               f.write(firstline + content)
               f.close()
            else:
                print("puste")
                f.seek(0, 0)
                f.write(infoline.rstrip('\r\n') + '\n'+'\n' + content)
                f.close()
    
    def updateText(self,var):
        with open(os.path.join("szablony",self.name+".txt"),'r+',encoding="utf-8") as f:
            f.truncate(0)
            f.write(var)
            f.close()

    def writeVars(self,vars,aut):
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
                print("puste")
        


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

