# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deviceconnect.ui'
#
# Created: Sun Nov 23 14:03:28 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

from boxes import ConnectedDevice
from jnpr.junos import Device

class Ui_DeviceConnect(object):
    def setupUi(self, DeviceConnect):
        self.cd_login = ConnectedDevice()
        DeviceConnect.setObjectName(_fromUtf8("DeviceConnect"))
        DeviceConnect.resize(416, 249)
        DeviceConnect.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralWidget = QtGui.QWidget(DeviceConnect)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        DeviceConnect.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(DeviceConnect)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        DeviceConnect.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(DeviceConnect)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        DeviceConnect.setStatusBar(self.statusBar)

        self.retranslateUi(DeviceConnect)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButton.clicked)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButton.clicked)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connectServer)
        QtCore.QMetaObject.connectSlotsByName(DeviceConnect)

    def connectServer(self):
        host = self.lineEdit_3.text()
        nickname = self.lineEdit_2.text()
        user = self.lineEdit_4.text()
        passwd = self.lineEdit.text()

        dev = Device(host = str(host),
                     user = str(user),
                     passwd = str(passwd))
        dev.open()
        if nickname =='':
            self.cd_login.devices.append((dev._hostname,dev))
        else:
            self.cd_login.devices.append((str(nickname),dev))
        print dev

    def retranslateUi(self, DeviceConnect):
        DeviceConnect.setWindowTitle(_translate("DeviceConnect", "DeviceConnect", None))
        self.pushButton.setText(_translate("DeviceConnect", "Connect", None))
        self.checkBox.setText(_translate("DeviceConnect", "Save details", None))
        self.label_2.setText(_translate("DeviceConnect", "Host or IP:", None))
        self.label_5.setText(_translate("DeviceConnect", "User Name:", None))
        self.label.setText(_translate("DeviceConnect", "Password:", None))
        self.label_3.setText(_translate("DeviceConnect", "Nick Name:", None))
        self.label_4.setText(_translate("DeviceConnect", "Add to group:", None))
        self.lineEdit_2.setPlaceholderText(_translate("DeviceConnect", "Optional", None))


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     DeviceConnect = QtGui.QMainWindow()
#     ui = Ui_DeviceConnect()
#     ui.setupUi(DeviceConnect)
#     DeviceConnect.show()
#     sys.exit(app.exec_())



