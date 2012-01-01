'''
Created on Dec 24, 2011

@author: eyadof
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time
import netifaces as ni
import  sys

import netusage
import MDataBase

class NetUsage(netusage.Ui_MainWindow,QMainWindow):
    def __init__(self,Parent=None):
        super(QMainWindow,self).__init__(Parent)
        self.setupUi(self) 
        self.db=MDataBase.MDatabase()
        self.GetInterfaces()
        
        self.interfaces.currentIndexChanged.connect(self.UpdateInfo)
        
        self.db.IncertData(self.GetDetails())
        
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.UpdateInfo)
        self.timer.start(1000)
        
    def GetInterfaces(self):
        for iname in ni.interfaces():
            self.interfaces.addItem(iname)
    def GetDetails(self):
        Details={}
        for iface in ni.interfaces():
            info=ni.ifaddresses(iface)
            if info.has_key(2):
                ip=info[2][0]['addr']
            elif info.has_key(10):
                ip=info[10][0]['addr']
            else:
                ip="None"
            if info.has_key(17):
                if info[17][0].has_key('addr'):
                    MAC=info[17][0]['addr']
                else:
                    MAC='None'
            else:
                MAC='None'
            Details[iface]=[ip,MAC]
        return Details
    def GetNetworkByte(self,iface):
        import re
        import subprocess
        
        output=subprocess.Popen(['ifconfig',iface],stdout=subprocess.PIPE).communicate()[0]
        rx_bytes=re.findall('RX bytes:([0-9]*) ', output)[0]
        tx_bytes = re.findall('TX bytes:([0-9]*) ', output)[0]
        tx_bytes= convert_bytes(tx_bytes)
        rx_bytes=convert_bytes(rx_bytes)
        return [tx_bytes,rx_bytes]
    
    def UpdateInfo(self):
        Current_iface=str(self.interfaces.currentText())
        Current_Bytes=self.GetNetworkByte(Current_iface)
        
        info=self.GetDetails()[Current_iface]
        
        self.ip4_label.setText(info[0])
        self.mac_label.setText(info[1])
        self.upload_label.setText(str(Current_Bytes[0]))
        self.download_label.setText(str(Current_Bytes[1]))
        
def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size

app=QApplication(sys.argv)
form=NetUsage()

form.show()
app.exec_()