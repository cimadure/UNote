# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\unote_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 1027)
        MainWindow.setToolTipDuration(5)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPage = QtWidgets.QMenu(self.menubar)
        self.menuPage.setObjectName("menuPage")
        self.menuPageMove = QtWidgets.QMenu(self.menuPage)
        self.menuPageMove.setObjectName("menuPageMove")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setCheckable(False)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionLoad_PDF = QtWidgets.QAction(MainWindow)
        self.actionLoad_PDF.setObjectName("actionLoad_PDF")
        self.actionText_Mode = QtWidgets.QAction(MainWindow)
        self.actionText_Mode.setCheckable(True)
        self.actionText_Mode.setObjectName("actionText_Mode")
        self.actionHighlight_Mode = QtWidgets.QAction(MainWindow)
        self.actionHighlight_Mode.setCheckable(True)
        self.actionHighlight_Mode.setObjectName("actionHighlight_Mode")
        self.actionSave_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_PDF.setObjectName("actionSave_PDF")
        self.actionPageInsertHere = QtWidgets.QAction(MainWindow)
        self.actionPageInsertHere.setObjectName("actionPageInsertHere")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        self.actionExtract.setObjectName("actionExtract")
        self.actionPageDeleteActive = QtWidgets.QAction(MainWindow)
        self.actionPageDeleteActive.setObjectName("actionPageDeleteActive")
        self.actionPageMoveUp = QtWidgets.QAction(MainWindow)
        self.actionPageMoveUp.setObjectName("actionPageMoveUp")
        self.actionPageMoveDown = QtWidgets.QAction(MainWindow)
        self.actionPageMoveDown.setObjectName("actionPageMoveDown")
        self.actionPageMoveTo_Page = QtWidgets.QAction(MainWindow)
        self.actionPageMoveTo_Page.setObjectName("actionPageMoveTo_Page")
        self.actionHelpAbout = QtWidgets.QAction(MainWindow)
        self.actionHelpAbout.setObjectName("actionHelpAbout")
        self.actionSave_PDF_as = QtWidgets.QAction(MainWindow)
        self.actionSave_PDF_as.setObjectName("actionSave_PDF_as")
        self.actionNew_PDF = QtWidgets.QAction(MainWindow)
        self.actionNew_PDF.setObjectName("actionNew_PDF")
        self.actionPageGoto = QtWidgets.QAction(MainWindow)
        self.actionPageGoto.setObjectName("actionPageGoto")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.menuFile.addAction(self.actionNew_PDF)
        self.menuFile.addAction(self.actionLoad_PDF)
        self.menuFile.addAction(self.actionSave_PDF)
        self.menuFile.addAction(self.actionSave_PDF_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPageMove.addAction(self.actionPageMoveUp)
        self.menuPageMove.addAction(self.actionPageMoveDown)
        self.menuPageMove.addAction(self.actionPageMoveTo_Page)
        self.menuPage.addAction(self.actionPageInsertHere)
        self.menuPage.addAction(self.actionPageDeleteActive)
        self.menuPage.addAction(self.menuPageMove.menuAction())
        self.menuPage.addSeparator()
        self.menuPage.addAction(self.actionPageGoto)
        self.menuHelp.addAction(self.actionHelpAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDonate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UNote"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPage.setTitle(_translate("MainWindow", "Page"))
        self.menuPageMove.setTitle(_translate("MainWindow", "Move Active"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionLoad_PDF.setText(_translate("MainWindow", "Load PDF"))
        self.actionLoad_PDF.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionText_Mode.setText(_translate("MainWindow", "Text Mode"))
        self.actionText_Mode.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionHighlight_Mode.setText(_translate("MainWindow", "Highlight Mode"))
        self.actionHighlight_Mode.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionSave_PDF.setText(_translate("MainWindow", "Save PDF"))
        self.actionSave_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPageInsertHere.setText(_translate("MainWindow", "Insert Here"))
        self.actionPageInsertHere.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionExtract.setText(_translate("MainWindow", "Extract"))
        self.actionPageDeleteActive.setText(_translate("MainWindow", "Delete Active"))
        self.actionPageMoveUp.setText(_translate("MainWindow", "Up"))
        self.actionPageMoveDown.setText(_translate("MainWindow", "Down"))
        self.actionPageMoveTo_Page.setText(_translate("MainWindow", "To Page"))
        self.actionHelpAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_PDF_as.setText(_translate("MainWindow", "Save PDF as"))
        self.actionSave_PDF_as.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.actionNew_PDF.setText(_translate("MainWindow", "New PDF"))
        self.actionNew_PDF.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionPageGoto.setText(_translate("MainWindow", "Goto"))
        self.actionPageGoto.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionDonate.setText(_translate("MainWindow", "Donate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

