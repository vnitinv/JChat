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
        self.treeViewIndex = index
        self.cd_chat = ConnectedDevice()
        self.clickedItemDetail()
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
        JChatMain.setWindowTitle(_translate("JChatMain", self.chat_title, None))
        self.comboBox.setItemText(0, _translate("JChatMain", "cli", None))
        self.comboBox.setItemText(1, _translate("JChatMain", "rpc", None))
        self.lineEdit.setPlaceholderText(_translate("JChatMain", "Type an expression and press Enter", None))

    def updateUi(self):
        command = self.comboBox.currentText()
        input = unicode(self.lineEdit.text())
        if not self.group_clicked:
            if command == "cli":
                output = self.cd_chat.devices[self.dev_in_action][0].cli(input, format='text')
            elif command == "rpc":
                output = etree.tostring(getattr(self.cd_chat.devices[self.dev_in_action][0].rpc, str(input).replace('-','_'))())
            try:
                self.textBrowser.setPlainText("\n%s: %s\n\n%s: %s\n" % (command, input, self.dev_in_action, output))
            except:
                self.textBrowser.append(
                "<font color=red>%s is invalid!</font>" % input)
        else:
            if command == "cli":
                output = ''
                for dev in self.cd_chat.groups[self.grp_in_action]:
                    op = self.cd_chat.devices[dev][0].cli(input, format='text')
                    output += "\n%s: %s\n\n%s: %s\n" % (command, input, dev, op)
            elif command == "rpc":
                output = ''
                for dev in self.cd_chat.groups[self.grp_in_action]:
                    op = etree.tostring(getattr(self.cd_chat.devices[dev][0].rpc, str(input).replace('-','_'))())
                    output += "\n%s: %s\n\n%s: %s\n" % (command, input, dev, op)
            try:
                self.textBrowser.setPlainText(output)
            except:
                self.textBrowser.append(
                "<font color=red>%s is invalid!</font>" % input)

    def clickedItemDetail(self):
        mdl = self.treeViewIndex.model()
        if self.treeViewIndex.parent().row() != -1:
            self.group_clicked = False
            self.grp_in_action = str(mdl.item(self.treeViewIndex.parent().row()).text())
            self.dev_in_action = self.chat_title = self.cd_chat.groups[self.grp_in_action][self.treeViewIndex.row()]
        else:   #group got clicked
            self.group_clicked = True
            self.grp_in_action = self.chat_title =  str(mdl.item(self.treeViewIndex.row()).text())
            if self.grp_in_action not in self.cd_chat.groups:
                self.dev_in_action = self.grp_in_action



