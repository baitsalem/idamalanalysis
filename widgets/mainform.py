from ui_mainform import *

from PyQt5.QtCore  import QModelIndex
from PyQt5.QtWidgets import QWidget
from core.winapimodel import WinApiModel
from idc import Jump

class MainForm(QWidget,Ui_Form):
    
    def __init__(self, parent=None):
        
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.manage_winapi()

    def manage_winapi(self):
        
        self.winapi_model = WinApiModel()
        self.winapi_treeview.setModel(self.winapi_model)
        self.winapi_model.builtModel()
        self.winapi_treeview.doubleClicked.connect(self._onFunctionClicked)

    def _onFunctionClicked(self, mi):
        
        """
        If a function in the functions table is clicked, the view of the calls and parameter table are updated.
        """
        row = self.winapi_treeview.model().rows[mi.row()]
        Jump(int(row[0],16))



