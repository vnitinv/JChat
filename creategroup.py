# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creategroup.ui'
#
# Created: Mon Nov 24 22:17:01 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_CreateGroup(object):
    def setupUi(self, CreateGroup):
        self.cd_cg = ConnectedDevice()
        CreateGroup.setObjectName(_fromUtf8("CreateGroup"))
        CreateGroup.resize(405, 114)
        self.gridLayout = QtGui.QGridLayout(CreateGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.grou_name_label = QtGui.QLabel(CreateGroup)
        self.grou_name_label.setObjectName(_fromUtf8("grou_name_label"))
        self.horizontalLayout.addWidget(self.grou_name_label)
        self.group_name_lineEdit = QtGui.QLineEdit(CreateGroup)
        self.group_name_lineEdit.setDragEnabled(True)
        self.group_name_lineEdit.setObjectName(_fromUtf8("group_name_lineEdit"))
        self.horizontalLayout.addWidget(self.group_name_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.cg_pushButton = QtGui.QPushButton(CreateGroup)
        self.cg_pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.cg_pushButton, 1, 0, 1, 1)

        self.retranslateUi(CreateGroup)
        QtCore.QObject.connect(self.cg_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.updateGroups)
        QtCore.QMetaObject.connectSlotsByName(CreateGroup)

    def updateGroups(self):
        host = str(self.group_name_lineEdit.text())
        if host not in self.cd_cg.groups:
            self.cd_cg.groups[host] = ()

    def retranslateUi(self, CreateGroup):
        CreateGroup.setWindowTitle(_translate("CreateGroup", "Group", None))
        self.grou_name_label.setText(_translate("CreateGroup", "Group Name:", None))
        self.cg_pushButton.setText(_translate("CreateGroup", "Create", None))

#
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     CreateGroup = QtGui.QWidget()
#     ui = Ui_CreateGroup()
#     ui.setupUi(CreateGroup)
#     CreateGroup.show()
#     sys.exit(app.exec_())

