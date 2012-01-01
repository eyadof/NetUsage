'''
Created on Dec 30, 2011

@author: eyadof
'''
import sqlite3
import os
import time

class MDatabase():
    def __init__(self):
        path=os.path.expanduser("~")+"/.NetUsage/"
        fpath=path+"source.db"
        if os.path.exists(fpath):             
            self.source=sqlite3.connect(fpath)
            self.cur=self.source.cursor()
        else:
            if not os.path.exists(path):
                os.mkdir(path)
                tmp=open(fpath,"w")
                tmp.close()
            else :
                tmp=open(fpath,"w")
                tmp.close()
            self.source=sqlite3.connect(fpath)
            self.cur=self.source.cursor()
            self.CreatTable()

    def CreatTable(self):
        self.cur.execute('''CREATE TABLE NetUsage (
        id INTEGER PRIMARY KEY , 
        iface TEXT,
        MAC TEXT ,
        Today  DOUBLE ,
        Today_date INTEGER ,
        month DOUBLE ,
        month_date INTEGER ,
        year DOUBLE ,
        year_date INTEGER )''')
        self.source.commit()        
    def IncertData(self,ifaceDict):
        old=self.getData()
        Current_time=time.localtime()
        if len(old) == 0:
            for key in ifaceDict:
                self.cur.execute(" INSERT INTO `NetUsage` (`iface`, `MAC`,`Today_date`,`month_date`,`year_date`) VALUES ('{0}','{1}',{2},{3},{4});".format(key,ifaceDict[key][1],Current_time[2],Current_time[2],Current_time[1]))
                self.source.commit()
        else:
            for key in ifaceDict:
                found=False
                for i in range(len(old)):
                    if key == unicode(old[i]['iface']):
                        found=True
                if not found:
                    self.cur.execute(" INSERT INTO `NetUsage` (`iface`, `MAC`, `month_date`,`year_date`) VALUES ('{0}','{1}',{2},{3});".format(key,ifaceDict[key][1],Current_time[2],Current_time[1]))
                    self.source.commit()
        self.cur.execute("select * from NetUsage")
        for set in self.cur.fetchall():
            print unicode(set)            
    def UpdateData(self,ifaceDict):
        Current=self.getData()
        for key in ifaceDict:
            for i in range(len(Current)):
                if time.localtime()[2]!=Current[i]['Today_date']:
                    self.cur.execute("update NetUsage SET Today_date={0} WHERE id={2} ".format(time.localtime()[2],Current[i]['id']))
                    self.source.commite()
                
    def getData(self):
        self.cur.execute("SELECT * from NetUsage")
        data=[]
        for info in self.cur.fetchall():
            entry={"id":info[0],"iface":info[1],"MAC":info[2],"Today":info[3],"Today_date":info[4],"month":info[5],"month_date":info[6],"year":info[7],"year_date":info[8]}
            data.append(entry)
        return data
    
    def __del__(self):
        self.source.close()
        print "database closed"