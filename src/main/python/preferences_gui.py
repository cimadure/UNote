# ---------------------------------------------------------------
# -- Preferences GUI Main File --
#
# Main File for running the Preferences GUI
#
# Author: Melvin Strobl
# ---------------------------------------------------------------

#from fbs_runtime.application_context.PySide2 import ApplicationContext

import os  # launching external python script
import sys  # exit script, file parsing

from PySide2.QtWidgets import QGraphicsDropShadowEffect
from PySide2.QtGui import QColor

from PySide2.QtCore import Signal, Slot, QSettings, QObject, Qt
from PySide2.QtWidgets import QDialog
from PySide2.QtGui import QIcon

from util import readFile, writeFile, toBool

from preferences_receiver import Receivers
from preferences import Preferences
from guiHelper import GuiHelper

# Reload the main ui

from preferences_qt_export import Ui_PreferencesDialog


from pathlib import Path

class App(QObject):
    COMPANY_NAME = "MSLS"
    APPLICATION_NAME = "UNote"

    KEYSFILEPATH = "./preferences.keys"

class PreferencesGUI(App):
    '''
    Main class for the Preferences Window
    '''
    keys = list()
    finished = Signal()


    def __init__(self, appctxt, windowInst):
        super().__init__()
        self.appctxt = appctxt
        self.initUI(windowInst)

        # self.windowInst.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.FramelessWindowHint)

        # self.windowInst.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.settings = QSettings(self.COMPANY_NAME, self.APPLICATION_NAME)

        self.receiversInst = Receivers(self.ui)
        self.receiversInst.confirmSignal.connect(self.handleExit)
        self.connectReceivers()

        self.guiHelper = GuiHelper()

        self.loadKeys()

        self.loadSettings()


    def terminate(self):
        self.storeSettings()
        del self.settings


    def initUI(self, windowInst):
        # self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_PreferencesDialog()
        self.ui.windowInst = windowInst
        self.ui.windowInst.hide()
        self.ui.setupUi(self.ui.windowInst)

        windowInst.setAttribute(Qt.WA_TranslucentBackground)
        self.backgroundEffect = QGraphicsDropShadowEffect(windowInst)
        self.backgroundEffect.setBlurRadius(30)
        self.backgroundEffect.setOffset(0,0)
        self.backgroundEffect.setEnabled(True)


        self.ui.centralwidget.setGraphicsEffect(self.backgroundEffect)

        self.ui.comboBoxAutosaveMode.addItem("Don't Autosave")
        self.ui.comboBoxAutosaveMode.addItem("5 min Autosave")
        self.ui.comboBoxAutosaveMode.addItem("10 min Autosave")
        self.ui.comboBoxAutosaveMode.addItem("15 min Autosave")
        self.ui.comboBoxAutosaveMode.addItem("20 min Autosave")

        self.ui.comboBoxThemeSelect.addItem("Dark Theme")
        self.ui.comboBoxThemeSelect.addItem("Light Theme")
        # self.ui.comboBoxThemeSelect.addItem("Ambient Theme")

    def run(self):
        '''
        Starts the Preferences Window
        '''
        self.loadSettings()
        self.ui.windowInst.show()

    @Slot(bool)
    def handleExit(self, confirmed):
        if confirmed:
            self.storeLooseEntries()
            self.storeSettings()

            print('Settings saved')
        else:
            self.loadSettings()

            print('Settings discarded')

        self.finished.emit()

    def connectReceivers(self):
        '''
        Connects all the buttons to the right receivers
        '''
        self.ui.radioButtonAffectsPDF.clicked.connect(self.receiversInst.setRadioButtonAffectsPDF)
        self.ui.comboBoxThemeSelect.currentIndexChanged.connect(self.receiversInst.setComboBoxThemeSelect)

        self.ui.radioButtonSmoothLines.clicked.connect(self.receiversInst.setradioButtonSmoothLines)

        self.ui.radioButtonSaveOnExit.clicked.connect(self.receiversInst.setRadioButtonSaveOnExit)
        self.ui.comboBoxAutosaveMode.currentIndexChanged.connect(self.receiversInst.setComboBoxAutosaveMode)

        self.ui.pushButtonOk.clicked.connect(lambda:self.receiversInst.confirmReceiver())
        self.ui.pushButtonCancel.clicked.connect(lambda:self.receiversInst.rejectReceiver())

        self.receiversInst.confirmSignal.connect(self.onClose)

    def loadKeys(self):
        '''
        Load the preferences keys
        '''

        scriptPath = os.path.dirname(os.path.abspath(__file__)) + '\\'
        print(scriptPath)
        # absKeysFilePath = os.path.normpath(scriptPath + KEYSFILEPATH)
        #absKeysFilePath = self.appctxt.get_resource('preferences.keys')
        scriptPath = os.path.dirname(os.path.abspath(__file__))
        absKeysFilePath = Path(scriptPath,'preferences.keys').absolute()
        print(absKeysFilePath)
        keysFileContent = readFile(absKeysFilePath)

        for key in keysFileContent['lines']:
            self.keys.append(key.replace('\n',''))

    def storeSettings(self):
        '''
        Store the settings from the gui to the local dict and then to the settings instance
        '''
        for key in self.keys:
            self.settings.setValue(key, str(Preferences.data[key]))

        self.settings.sync()

    def storeLooseEntries(self):
        '''
        Saves all entries, which have been entered without explicit confirmation
        '''
        Preferences.updateKeyValue("radioButtonAffectsPDF", str(self.ui.radioButtonAffectsPDF.isChecked()))
        Preferences.updateKeyValue("comboBoxThemeSelect", str(self.ui.comboBoxThemeSelect.currentIndex()))

        Preferences.updateKeyValue("radioButtonSmoothLines", str(self.ui.radioButtonSmoothLines.isChecked()))
        Preferences.updateKeyValue("radioButtonUsePenAsDefault", str(self.ui.radioButtonSmoothLines.isChecked()))

        Preferences.updateKeyValue("radioButtonSaveOnExit", int(self.ui.radioButtonSaveOnExit.isChecked()))
        Preferences.updateKeyValue("comboBoxAutosaveMode", int(self.ui.comboBoxAutosaveMode.currentIndex()))

        Preferences.updateKeyValue("radioButtonNoInteractionWhileEditing", str(self.ui.radioButtonNoInteractionWhileEditing.isChecked()))

    @Slot(bool)
    def onClose(self, store):
        if store:
            self.saveSettings()
        else:
            self.discardSettings()

    def saveSettings(self):
        self.storeLooseEntries()
        self.storeSettings()

    def discardSettings(self):
        self.loadSettings()

    def loadSettings(self):
        '''
        Load the settings from the settings instance to the local dict
        '''
        for key in self.keys:
            Preferences.updateKeyValue(key, self.settings.value(key, defaultValue=None, type=str))

        self.ensureValidData()

        self.ui.radioButtonAffectsPDF.setChecked(toBool(Preferences.data["radioButtonAffectsPDF"]))
        self.ui.comboBoxThemeSelect.setCurrentIndex(int(Preferences.data["comboBoxThemeSelect"]))
        self.receiversInst.setComboBoxThemeSelect(int(Preferences.data["comboBoxThemeSelect"]))

        self.ui.radioButtonUsePenAsDefault.setChecked(toBool(Preferences.data["radioButtonUsePenAsDefault"]))
        self.ui.radioButtonSmoothLines.setChecked(toBool(Preferences.data["radioButtonSmoothLines"]))

        self.ui.radioButtonSaveOnExit.setChecked(toBool(Preferences.data["radioButtonSaveOnExit"]))
        self.ui.comboBoxAutosaveMode.setCurrentIndex(int(Preferences.data["comboBoxAutosaveMode"]))

        self.ui.radioButtonNoInteractionWhileEditing.setChecked(toBool(Preferences.data["radioButtonNoInteractionWhileEditing"]))


    def ensureValidData(self):
        # Apply all default preferences if necessary

        if Preferences.data['radioButtonAffectsPDF'] == "":
            Preferences.updateKeyValue('radioButtonAffectsPDF', str(True))
        if Preferences.data['comboBoxThemeSelect'] == "":
            Preferences.updateKeyValue('comboBoxThemeSelect', 1)

        if Preferences.data['radioButtonSmoothLines'] == "":
            Preferences.updateKeyValue('radioButtonSmoothLines', str(True))
        if Preferences.data['radioButtonUsePenAsDefault'] == "":
            Preferences.updateKeyValue('radioButtonUsePenAsDefault', str(True))
        if Preferences.data['comboBoxDrawingMode'] == "":
            Preferences.updateKeyValue('comboBoxDrawingMode', 0)

        if Preferences.data['radioButtonSaveOnExit'] == "":
            Preferences.updateKeyValue('radioButtonSaveOnExit', str(True))
        if Preferences.data['comboBoxAutosaveMode'] == "":
            Preferences.updateKeyValue('comboBoxAutosaveMode', 0)

        if Preferences.data['radioButtonNoInteractionWhileEditing'] == "":
            Preferences.updateKeyValue('radioButtonNoInteractionWhileEditing', str(True))

        if Preferences.data['textSize'] == "":
            Preferences.updateKeyValue('textSize', "('0', '0', '0')")
        if Preferences.data['markerSize'] == "":
            Preferences.updateKeyValue('markerSize', "70")
        if Preferences.data['markerColor'] == "":
            Preferences.updateKeyValue('markerColor', "('0', '0', '0')")
        if Preferences.data['freehandSize'] == "":
            Preferences.updateKeyValue('freehandSize', "70")
        if Preferences.data['freehandColor'] == "":
            Preferences.updateKeyValue('freehandColor', "('0', '0', '0')")
        if Preferences.data['formSize'] == "":
            Preferences.updateKeyValue('formSize', "70")
        if Preferences.data['formColor'] == "":
            Preferences.updateKeyValue('formColor', "('0', '0', '0')")

    # def applySettings(self):
    #     '''
    #     Apply the settings from the local dict to the gui instance
    #     '''

    #     self.receiversInst.setTheme(self.ui.comboBoxThemeSelect.currentIndex())
