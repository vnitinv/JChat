# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connector.ui'
#
# Created: Sun Nov 23 19:20:52 2014
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

class Ui_connector(object):
    def setupUi(self, connector):
        connector.setObjectName(_fromUtf8("connector"))
        connector.resize(400, 300)
        self.layoutWidget = QtGui.QWidget(connector)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 250, 371, 32))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_connect = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.horizontalLayout_2.addWidget(self.pushButton_connect)
        self.checkBox_savedetails = QtGui.QCheckBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_savedetails.sizePolicy().hasHeightForWidth())
        self.checkBox_savedetails.setSizePolicy(sizePolicy)
        self.checkBox_savedetails.setChecked(True)
        self.checkBox_savedetails.setObjectName(_fromUtf8("checkBox_savedetails"))
        self.horizontalLayout_2.addWidget(self.checkBox_savedetails)
        self.layoutWidget_2 = QtGui.QWidget(connector)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 101, 221))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.layoutWidget_3 = QtGui.QWidget(connector)
        self.layoutWidget_3.setGeometry(QtCore.QRect(127, 10, 251, 221))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEdit_host = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.verticalLayout_4.addWidget(self.lineEdit_host)
        self.lineEdit_user = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.verticalLayout_4.addWidget(self.lineEdit_user)
        self.lineEdit_passwd = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_passwd.setAutoFillBackground(True)
        self.lineEdit_passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName(_fromUtf8("lineEdit_passwd"))
        self.verticalLayout_4.addWidget(self.lineEdit_passwd)
        self.lineEdit_nickname = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEdit_nickname.setObjectName(_fromUtf8("lineEdit_nickname"))
        self.verticalLayout_4.addWidget(self.lineEdit_nickname)
        self.comboBox_group = QtGui.QComboBox(self.layoutWidget_3)
        self.comboBox_group.setObjectName(_fromUtf8("comboBox_group"))
        self.verticalLayout_4.addWidget(self.comboBox_group)

        self.retranslateUi(connector)
        QtCore.QObject.connect(self.pushButton_connect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_host.clear)
        QtCore.QMetaObject.connectSlotsByName(connector)

    def abcd(self):
        print 'nitin'

    def retranslateUi(self, connector):
        connector.setWindowTitle(_translate("connector", "Form", None))
        self.pushButton_connect.setText(_translate("connector", "Connect", None))
        self.checkBox_savedetails.setText(_translate("connector", "Save details", None))
        self.label_6.setText(_translate("connector", "Host or IP:", None))
        self.label_7.setText(_translate("connector", "User Name:", None))
        self.label_8.setText(_translate("connector", "Password:", None))
        self.label_9.setText(_translate("connector", "Nick Name:", None))
        self.label_10.setText(_translate("connector", "Add to group:", None))
        self.lineEdit_nickname.setPlaceholderText(_translate("connector", "Optional", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    connector = QtGui.QWidget()
    ui = Ui_connector()
    ui.setupUi(connector)
    connector.show()
    sys.exit(app.exec_())

