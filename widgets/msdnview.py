from PyQt5.QtWidgets import QWidget, QTextBrowser, QVBoxLayout, QMenu,QAction
from PyQt5.QtCore import  Qt

#from PyQt5.QtCore import  pyqtSlot , QMetaObject, Qt, pyqtSignal


from core.msdnrequest import *

class MsdnView(QTextBrowser):



    def __init__(self, parent=None):
        
        super(MsdnView, self).__init__(parent)
    
        self.setOpenLinks(True)
        self.anchorClicked.connect(self.on_anchor_clicked)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openContextMenu) # widget class signal

        self.msdn_model = MsdnModel()


    def on_anchor_clicked(self,url):
        
        self.setHtml(self.msdn_model.getOnlineMsdnLinkContent(url))

    def openContextMenu(self, position):
        
        menu = self.createStandardContextMenu() #QMenu()
        menu.triggered.connect(self.on_action_in_context_menu)
       
        menu.addAction("Backward")
        menu.addAction("Forward")

        menu.exec_(self.viewport().mapToGlobal(position))

    def on_action_in_context_menu(self,action):
        
        if ( action.text() == "Backward" ) :
            print(action.text() )
            self.setHtml(self.msdn_model.backward())

            
        if ( action.text() == "Forward" ) :
            print(action.text() )
            self.setHtml(self.msdn_model.forward())
          



