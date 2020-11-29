import datetime
import os, os.path
import time
import re

class ListItem(object):
    def __init__(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name
        self.author=None

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
                f.write(infoline.rstrip('\r\n') + '\n' + content)
                f.close()


def readFolder():
    file_list = os.listdir("szablony")
    data=()

    for file_name in file_list:
        with open(os.path.join("szablony", file_name), "r") as src_file:
            txttime = time.ctime(os.path.getctime(src_file.name))
            data += ((src_file.name, file_name, txttime),)

    return data

def readTemplate(template):
    data = open(os.path.join("szablony",template.name+".txt"),"r")
    #data.readline()
    return data.read()


