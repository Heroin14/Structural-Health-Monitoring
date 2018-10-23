# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window1_1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import arima

path_input= None
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

class Ui_Form(object):

    def pressRun(self):
        
        arima.main(self.lineEdit.text())
        # Output Data

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(270, 80, 107, 95))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 80, 244, 97))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.widget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.lineEdit.returnPressed.connect(self.checkPath)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        



    def temp_func(self):
        self.temp_messageBox= QtGui.QMessageBox()
        self.temp_messageBox.setInformativeText("The path isnt correct, Please re-enter path")
        self.temp_messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
        
        ret = self.temp_messageBox.exec_()
        if(ret == QtGui.QMessageBox.Yes):
            return
        
        
        
    def checkPath(self):

        path_input12= self.lineEdit.text()
        
        output= arima.checkPath(path_input12)
        if output is False:
            self.temp_func()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Auto Regression", None))
        self.pushButton_3.setText(_translate("Form", "Enter Path", None))
        self.pushButton.setText(_translate("Form", "Run", None))

        self.pushButton.clicked.connect(self.pressRun)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

