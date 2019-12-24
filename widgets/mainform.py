from ui_mainform import *

from PyQt5.QtCore  import QModelIndex
from PyQt5.QtWidgets import QWidget
from core.winapimodelchild import WinApiModelc
from idc import Jump
from PyQt5 import QtWidgets
from apitreeview import WinApiTreeView


class MainForm(QWidget,Ui_Form):
    
    def __init__(self, parent=None):
        
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.manage_winapi()

    def manage_winapi(self):
       
        
        self.winapi_model = WinApiModelc()
        self.winapi_treeview = WinApiTreeView(self.win_api_addr,self.winapi_model)
        self.show_winapi_treeview()
        self.winapi_treeview.doubleClicked.connect(self._onFunctionClicked)

    def _onFunctionClicked(self, mi):
        
        """
        If a function in the functions table is clicked, the view of the calls and parameter table are updated.
        """
        item = mi.internalPointer()
        addr_to_jump = item.data(0)
        Jump(int(addr_to_jump,16))


    def show_winapi_treeview(self):


        gridLayout_2 = QtWidgets.QGridLayout(self.win_api_addr)
        gridLayout_2.setContentsMargins(0, 0, 0, 0)
        gridLayout_2.setObjectName("gridLayout_2")
        gridLayout_2.addWidget(self.winapi_treeview, 0, 0, 1, 1)

        
        
