from PyQt4 import QtCore, QtGui
import mainchatwindow

import sys
app = QtGui.QApplication(sys.argv)
MainChatWindow = QtGui.QMainWindow()
ui = mainchatwindow.Ui_MainChatWindow()
ui.setupUi(MainChatWindow)
MainChatWindow.show()
sys.exit(app.exec_())
