# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Feb  5 09:08:12 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(761, 591)
        self.configurationTab = QtGui.QWidget()
        self.configurationTab.setObjectName("configurationTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.configurationTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.configurationTree = QtGui.QTreeView(self.configurationTab)
        self.configurationTree.setObjectName("configurationTree")
        self.horizontalLayout.addWidget(self.configurationTree)
        self.configurationDetailsLayout = QtGui.QVBoxLayout()
        self.configurationDetailsLayout.setObjectName("configurationDetailsLayout")
        self.configurationEditLayout = QtGui.QVBoxLayout()
        self.configurationEditLayout.setObjectName("configurationEditLayout")
        self.configurationVariableLabel = QtGui.QLabel(self.configurationTab)
        self.configurationVariableLabel.setObjectName("configurationVariableLabel")
        self.configurationEditLayout.addWidget(self.configurationVariableLabel)
        self.configurationValueEdit = QtGui.QPlainTextEdit(self.configurationTab)
        self.configurationValueEdit.setObjectName("configurationValueEdit")
        self.configurationEditLayout.addWidget(self.configurationValueEdit)
        self.configurationEditButtonsLayout = QtGui.QHBoxLayout()
        self.configurationEditButtonsLayout.setObjectName("configurationEditButtonsLayout")
        self.configurationDefaultButton = QtGui.QPushButton(self.configurationTab)
        self.configurationDefaultButton.setObjectName("configurationDefaultButton")
        self.configurationEditButtonsLayout.addWidget(self.configurationDefaultButton)
        self.configurationSetButton = QtGui.QPushButton(self.configurationTab)
        self.configurationSetButton.setObjectName("configurationSetButton")
        self.configurationEditButtonsLayout.addWidget(self.configurationSetButton)
        self.configurationEditLayout.addLayout(self.configurationEditButtonsLayout)
        self.configurationDetailsLayout.addLayout(self.configurationEditLayout)
        self.configurationHelpLabel = QtGui.QLabel(self.configurationTab)
        self.configurationHelpLabel.setObjectName("configurationHelpLabel")
        self.configurationDetailsLayout.addWidget(self.configurationHelpLabel)
        self.configurationHelp = QtGui.QPlainTextEdit(self.configurationTab)
        self.configurationHelp.setObjectName("configurationHelp")
        self.configurationDetailsLayout.addWidget(self.configurationHelp)
        self.horizontalLayout.addLayout(self.configurationDetailsLayout)
        window.addTab(self.configurationTab, "")
        self.commandsTab = QtGui.QWidget()
        self.commandsTab.setObjectName("commandsTab")
        window.addTab(self.commandsTab, "")

        self.retranslateUi(window)
        window.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(QtGui.QApplication.translate("window", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationVariableLabel.setText(QtGui.QApplication.translate("window", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationDefaultButton.setText(QtGui.QApplication.translate("window", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationSetButton.setText(QtGui.QApplication.translate("window", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.configurationHelpLabel.setText(QtGui.QApplication.translate("window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        window.setTabText(window.indexOf(self.configurationTab), QtGui.QApplication.translate("window", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        window.setTabText(window.indexOf(self.commandsTab), QtGui.QApplication.translate("window", "Commands", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QTabWidget()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
