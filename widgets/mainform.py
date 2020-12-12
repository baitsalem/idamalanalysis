from ui_mainform import *

from PyQt5.QtCore  import QModelIndex
from PyQt5.QtWidgets import QWidget, QTextBrowser, QVBoxLayout
from PyQt5 import QtWidgets


from core.winapimodelchild import WinApiModelc
from core.msdnrequest import *
from apitreeview import WinApiTreeView
from msdnview import MsdnView 
from ida_kernwin import jumpto

class MainForm(QWidget,Ui_Form):
    
    def __init__(self, parent=None):
        
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.manage_winapi()

    def manage_winapi(self):
       
        
        self.winapi_model = WinApiModelc()
        
        self.winapi_treeview = WinApiTreeView(self.win_api_addr,self.winapi_model)
        self.show_winapi_treeview()
        self.winapi_treeview.menuActionClicked.connect(self._onWinApiTreeContextMenuCicked) # ici la fonction
        self.winapi_treeview.doubleClicked.connect(self._onFunctionClicked)
        
        # msdn windows creation
        self.msdn_window =  MsdnView(self.web)
        self.web_layout.addWidget(self.msdn_window)

    def _onFunctionClicked(self, mi):
        
        """
        If a function in the functions table is clicked, the view of the calls and parameter table are updated.
        """
        item = mi.internalPointer()
        addr_to_jump = item.data(0)
        jumpto(int(addr_to_jump,16))


    def show_winapi_treeview(self):

        self.gridLayout_2 = QtWidgets.QGridLayout(self.win_api_addr)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.addWidget(self.winapi_treeview, 0, 0, 1, 1)

        
        
    def show_winapi_webBrowser(self):

        self.gridLayout_4 = QtWidgets.QGridLayout(self.web)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.addWidget(self.msdn_window, 0, 0, 1, 1)

    
    def _onWinApiTreeContextMenuCicked(self, keyword):

        self.msdn_window.setHtml(getOnlineMsdnContent(keyword))



