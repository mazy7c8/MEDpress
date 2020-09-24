import datetime

class ListItem(object):
    def __init__(self,name,abbr,source):
        self.name=name
        self.abbr=abbr
        self.date=datetime.datetime.now()
        self.source=source