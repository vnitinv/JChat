from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

import chatwin
import deviceconnect
import creategroup
from boxes import ConnectedDevice

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainChatWindow(object):
    def setupUi(self, MainChatWindow):
        self.cd_maincw = ConnectedDevice()
        MainChatWindow.setObjectName(_fromUtf8("MainChatWindow"))
        MainChatWindow.resize(377, 554)
        self.centralWidget = QtGui.QWidget(MainChatWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeView = QtGui.QTreeView(self.centralWidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        MainChatWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainChatWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 277, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDevice = QtGui.QMenu(self.menuBar)
        self.menuDevice.setObjectName(_fromUtf8("menuDevice"))
        self.menuGroup = QtGui.QMenu(self.menuBar)
        self.menuGroup.setObjectName(_fromUtf8("menuGroup"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainChatWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainChatWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainChatWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainChatWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainChatWindow.setStatusBar(self.statusBar)
        self.actionConnect = QtGui.QAction(MainChatWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionExit = QtGui.QAction(MainChatWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionEdit = QtGui.QAction(MainChatWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionCreate = QtGui.QAction(MainChatWindow)
        self.actionCreate.setObjectName(_fromUtf8("actionCreate"))
        self.actionOnline = QtGui.QAction(MainChatWindow)
        self.actionOnline.setObjectName(_fromUtf8("actionOnline"))
        self.menuDevice.addAction(self.actionConnect)
        self.menuDevice.addAction(self.actionExit)
        self.menuGroup.addAction(self.actionEdit)
        self.menuGroup.addAction(self.actionCreate)
        self.menuView.addAction(self.actionOnline)
        self.menuBar.addAction(self.menuDevice.menuAction())
        self.menuBar.addAction(self.menuGroup.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainChatWindow)
        QtCore.QObject.connect(self.actionConnect, QtCore.SIGNAL(_fromUtf8("triggered()")), self.openDeviceConnect)
        QtCore.QObject.connect(self.actionCreate, QtCore.SIGNAL(_fromUtf8("triggered()")), self.openCreateGroup)
        QtCore.QObject.connect(self.treeView, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.openChatWindow)
        QtCore.QMetaObject.connectSlotsByName(MainChatWindow)

    def retranslateUi(self, MainChatWindow):
        MainChatWindow.setWindowTitle(_translate("MainChatWindow", "JChat", None))
        self.menuDevice.setTitle(_translate("MainChatWindow", "Device", None))
        self.menuGroup.setTitle(_translate("MainChatWindow", "Group", None))
        self.menuView.setTitle(_translate("MainChatWindow", "View", None))
        self.actionConnect.setText(_translate("MainChatWindow", "Connect", None))
        self.actionExit.setText(_translate("MainChatWindow", "Exit", None))
        self.actionEdit.setText(_translate("MainChatWindow", "Edit", None))
        self.actionCreate.setText(_translate("MainChatWindow", "Create", None))
        self.actionOnline.setText(_translate("MainChatWindow", "Online", None))


    def openDeviceConnect(self):
        self.DeviceConnect = QtGui.QMainWindow()
        self.connect_ui = deviceconnect.Ui_DeviceConnect()
        self.connect_ui.setupUi(self.DeviceConnect)
        self.DeviceConnect.show()
        self.DeviceConnect.closeEvent = self.updateTree

    def openCreateGroup(self):
        self.CreateGroup = QtGui.QWidget()
        self.cg_ui = creategroup.Ui_CreateGroup()
        self.cg_ui.setupUi(self.CreateGroup)
        self.CreateGroup.show()

    def updateTree(self, event=None):
        self.model = QtGui.QStandardItemModel()
        self.model.invisibleRootItem()
        for grp, devices in self.cd_maincw.groups.items():
            rt = QtGui.QStandardItem(grp)
            self.model.appendRow(rt)
            for device in devices:
                dv = QtGui.QStandardItem(device)
                dv.setForeground(QtGui.QColor(0,200,0))
                dv.setFont(QtGui.QFont("Courier", 17))
                rt.appendRow(dv)

        dev_in_grps = []
        [dev_in_grps.extend(i) for i in self.cd_maincw.groups.values()]
        for device in self.cd_maincw.devices:
            if device[0] not in dev_in_grps:
                dv = QtGui.QStandardItem(device[0])
                dv.setForeground(QtGui.QColor(0,200,0))
                dv.setFont(QtGui.QFont("Courier", 17))
                self.model.appendRow(dv)

        self.treeView.setModel(self.model)
        self.treeView.expandAll()

    def openChatWindow(self, index):
        # print index.parent().row()
        # print index.row()
        self.JChatMain = QtGui.QMainWindow()
        self.chat_ui = chatwin.Ui_JChatMain()
        self.chat_ui.setupUi(self.JChatMain, index)
        self.JChatMain.show()

