from ui_mainform import *

from PyQt5.QtCore  import QModelIndex
from PyQt5.QtWidgets import QWidget
from core.winapimodelchild import WinApiModelc
from idc import Jump

class MainForm(QWidget,Ui_Form):
    
    def __init__(self, parent=None):
        
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.manage_winapi()

    def manage_winapi(self):
       
        
        self.winapi_model = WinApiModelc()
        self.winapi_treeview.setModel(self.winapi_model)
        self.winapi_treeview.doubleClicked.connect(self._onFunctionClicked)

    def _onFunctionClicked(self, mi):
        
        """
        If a function in the functions table is clicked, the view of the calls and parameter table are updated.
        """
        item = mi.internalPointer()
        addr_to_jump = item.data(0)
        Jump(int(addr_to_jump,16))



