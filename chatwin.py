# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jchatmain.ui'
#
# Created: Sun Nov 23 13:15:17 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from lxml import etree

from boxes import ConnectedDevice

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

class Ui_JChatMain(object):
    def setupUi(self, JChatMain, index):
        self.chat_index = index
        self.cd_chat = ConnectedDevice()
        JChatMain.setObjectName(_fromUtf8("JChatMain"))
        JChatMain.resize(414, 397)
        self.centralWidget = QtGui.QWidget(JChatMain)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setAcceptRichText(False)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        JChatMain.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(JChatMain)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        JChatMain.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(JChatMain)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        JChatMain.setStatusBar(self.statusBar)

        self.retranslateUi(JChatMain)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.lineEdit.selectAll)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.updateUi)
        QtCore.QMetaObject.connectSlotsByName(JChatMain)

    def retranslateUi(self, JChatMain):
        JChatMain.setWindowTitle(_translate("JChatMain", self.cd_chat.devices[0][1]._hostname, None))
        self.comboBox.setItemText(0, _translate("JChatMain", "cli", None))
        self.comboBox.setItemText(1, _translate("JChatMain", "rpc", None))
        self.lineEdit.setPlaceholderText(_translate("JChatMain", "Type an expression and press Enter", None))

    def updateUi(self):
        command = self.comboBox.currentText()
        input = unicode(self.lineEdit.text())
        if command == "cli":  # disconnects from current connection
            output = self.cd_chat.devices[0][1].cli(input, format='text')
        elif command == "rpc":  # disconnects from current connection
            output = etree.tostring(getattr(self.cd_chat.devices[0][1].rpc, str(input).replace('-','_'))())
        try:
            #self.textBrowser.append("%s: %s\n" % (command, input))
            self.textBrowser.setPlainText("\n%s: %s\n\n%s: %s\n" % (command, input, self.cd_chat.devices[0][0], output))
            #self.textBrowser.append("<b>%s</b>: %s" % (self.cd_chat.devices[0][0], output))
        except:
            self.textBrowser.append(
            "<font color=red>%s is invalid!</font>" % input)


