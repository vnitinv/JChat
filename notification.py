__author__ = 'aamish'
# -*- coding: utf-8 -*-
import sys
from juniper.jet.ttypes import *
from threading import Thread
import zmq
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_Dialog(object):
    def setupUi(self, Dialog,message):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(327, 237)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.alert_message = QtGui.QTextBrowser(Dialog)
        self.alert_message.setObjectName(_fromUtf8("alert_message"))
        self.alert_message.append(message)
        self.gridLayout.addWidget(self.alert_message, 0, 0, 1, 1)
        self.ok_button = QtGui.QPushButton(Dialog)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.gridLayout.addWidget(self.ok_button, 1, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.ok_button.setText(_translate("Dialog", "OK", None))

def showNotification(message,device):
    # TODO Add the event dialog open window
    print "Received notification from device %s" %(device), "message ", message
    # app = QtGui.QApplication(sys.argv)
    # Dialog = QtGui.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog,message= "Received notification from device %s" %(device))


class NotificationDevice():
    def __init__(self,host,port='5556'):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://%s:%s" % (host, port))
        self.socket.setsockopt(zmq.SUBSCRIBE, str(NotificationType.ROUTE_ADD))
        self.socket.setsockopt(zmq.SUBSCRIBE, str(NotificationType.ROUTE_DELETE))
        self.socket.setsockopt(zmq.SUBSCRIBE, str(NotificationType.ROUTE_CHANGE))
        self.handler = showNotification
        self.host = host
        self.eventThread = None

    def startListening(self):
        self.eventThread = Thread(
                                 target=self.serverHandle,
                                 args=(self.socket,)
                                 )
        self.eventThread.daemon = True
        self.eventThread.start()

    def serverHandle(self):
        while True:
            string = self.socket.recv()
            filter, topicdata = string.split(':')
            transportIn = TTransport.TMemoryBuffer(topicdata)
            protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
            evMsg = EventMessage()
            evMsg.read(protocolIn)
            self.handler(evMsg,self.host)

