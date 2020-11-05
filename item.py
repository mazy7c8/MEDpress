import datetime
import os, os.path
import time

class ListItem(object):
    def __init__(self,name,date,source):
        self.name=name.rstrip(".txt")
        self.abbr=name[0:4]
        self.date=date
        self.source=name

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
    return data.read()


