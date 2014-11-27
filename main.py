from PyQt4 import QtCore, QtGui
import mainchatwindow

import sys

from twisted.internet import reactor, threads
from jnpr.junos import Device
from boxes import ConnectedDevice

def pleaseConnect(devices):
    for k,v in devices.items():
        dev = Device(host = v[1][0],
                     user = v[1][1],
                     passwd = v[1][2])
        dev.open()
        devices[k]=(dev,v[1])
    return devices

def resultReturned(x):
    reactor.stop()

app = QtGui.QApplication(sys.argv)
MainChatWindow = QtGui.QMainWindow()
ui = mainchatwindow.Ui_MainChatWindow()
ui.setupUi(MainChatWindow)
MainChatWindow.show()

d = threads.deferToThread(pleaseConnect, ConnectedDevice.devices)
d.addCallback(resultReturned)
reactor.run()
ui.updateTree()

sys.exit(app.exec_())
