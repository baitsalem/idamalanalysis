# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 500)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.qtabw = QtWidgets.QTabWidget(Form)
        self.qtabw.setObjectName("qtabw")
        self.win_api_addr = QtWidgets.QWidget()
        self.win_api_addr.setObjectName("win_api_addr")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.win_api_addr)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.winapi_treeview = QtWidgets.QTreeView(self.win_api_addr)
        self.winapi_treeview.setObjectName("winapi_treeview")
        self.gridLayout_2.addWidget(self.winapi_treeview, 0, 0, 1, 1)
        self.qtabw.addTab(self.win_api_addr, "")
        self.vul_bof_func = QtWidgets.QWidget()
        self.vul_bof_func.setObjectName("vul_bof_func")
        self.qtabw.addTab(self.vul_bof_func, "")
        self.gridLayout.addWidget(self.qtabw, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.qtabw.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.qtabw.setTabText(self.qtabw.indexOf(self.win_api_addr), _translate("Form", "WINAPI_ADDR"))
        self.qtabw.setTabText(self.qtabw.indexOf(self.vul_bof_func), _translate("Form", "VUL_BOF_FUNC"))

