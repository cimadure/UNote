# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\preferences_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(894, 1032)
        self.verticalLayout = QtWidgets.QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.horizontalGroupBox = QtWidgets.QGroupBox(PreferencesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox.setSizePolicy(sizePolicy)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelAutosave = QtWidgets.QLabel(self.horizontalGroupBox)
        self.labelAutosave.setObjectName("labelAutosave")
        self.horizontalLayout_2.addWidget(self.labelAutosave)
        self.comboBoxAutosave = QtWidgets.QComboBox(self.horizontalGroupBox)
        self.comboBoxAutosave.setObjectName("comboBoxAutosave")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.comboBoxAutosave.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxAutosave)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalGroupBox)
        self.horizontalGroupBox1 = QtWidgets.QGroupBox(PreferencesDialog)
        self.horizontalGroupBox1.setObjectName("horizontalGroupBox1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTheme = QtWidgets.QLabel(self.horizontalGroupBox1)
        self.labelTheme.setObjectName("labelTheme")
        self.horizontalLayout_3.addWidget(self.labelTheme)
        self.radioButtonDarkTheme = QtWidgets.QRadioButton(self.horizontalGroupBox1)
        self.radioButtonDarkTheme.setChecked(False)
        self.radioButtonDarkTheme.setObjectName("radioButtonDarkTheme")
        self.horizontalLayout_3.addWidget(self.radioButtonDarkTheme)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalGroupBox1)
        self.horizontalGroupBox2 = QtWidgets.QGroupBox(PreferencesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox2.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox2.setSizePolicy(sizePolicy)
        self.horizontalGroupBox2.setObjectName("horizontalGroupBox2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalGroupBox2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelPenDraw = QtWidgets.QLabel(self.horizontalGroupBox2)
        self.labelPenDraw.setObjectName("labelPenDraw")
        self.horizontalLayout_4.addWidget(self.labelPenDraw)
        self.radioButtonPenOnly = QtWidgets.QRadioButton(self.horizontalGroupBox2)
        self.radioButtonPenOnly.setChecked(True)
        self.radioButtonPenOnly.setObjectName("radioButtonPenOnly")
        self.horizontalLayout_4.addWidget(self.radioButtonPenOnly)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalGroupBox2)
        self.verticalLayout_3.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.buttonBox = QtWidgets.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_41.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_41)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "UNote - Preferences"))
        self.labelAutosave.setText(_translate("PreferencesDialog", "Autosave (minutes)"))
        self.comboBoxAutosave.setCurrentText(_translate("PreferencesDialog", "never"))
        self.comboBoxAutosave.setItemText(0, _translate("PreferencesDialog", "0.5"))
        self.comboBoxAutosave.setItemText(1, _translate("PreferencesDialog", "1"))
        self.comboBoxAutosave.setItemText(2, _translate("PreferencesDialog", "5"))
        self.comboBoxAutosave.setItemText(3, _translate("PreferencesDialog", "10"))
        self.comboBoxAutosave.setItemText(4, _translate("PreferencesDialog", "15"))
        self.comboBoxAutosave.setItemText(5, _translate("PreferencesDialog", "30"))
        self.comboBoxAutosave.setItemText(6, _translate("PreferencesDialog", "never"))
        self.labelTheme.setText(_translate("PreferencesDialog", "Theme"))
        self.radioButtonDarkTheme.setText(_translate("PreferencesDialog", "Dark Theme"))
        self.labelPenDraw.setText(_translate("PreferencesDialog", "Pen Draw Only"))
        self.radioButtonPenOnly.setText(_translate("PreferencesDialog", "Pen Draw Only"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreferencesDialog = QtWidgets.QDialog()
    ui = Ui_PreferencesDialog()
    ui.setupUi(PreferencesDialog)
    PreferencesDialog.show()
    sys.exit(app.exec_())

