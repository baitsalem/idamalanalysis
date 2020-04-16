# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTreeView, QWidget,QMessageBox, QMenu,QAction
from PyQt5.QtCore import  pyqtSlot , QMetaObject, Qt, pyqtSignal

class WinApiTreeView(QTreeView):
    '''
        subclass  QTreeView to manage windows api tree view
    '''
    
    menuActionClicked = pyqtSignal('QString',name='menuActionClicked')

    def __init__(self,parent,model):

        super(WinApiTreeView,self).__init__(parent)
        QMetaObject.connectSlotsByName(self)  
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openContextMenu) # widget class signal

        self.model = model
        self.setModel(self.model) 
    
    def openContextMenu(self, position):
        
        menu = QMenu()
        menu.triggered.connect(self.qmenuActionTriggered)
        

        menu.addAction("auto_rename")
        menu.addAction("rename")
        menu.addAction("msdn help")

        menu.exec_(self.viewport().mapToGlobal(position))
    

    def qmenuActionTriggered(self,action):
       
        indexes = self.selectedIndexes()
        item = indexes[0].internalPointer()

        if(item.childCount() == 0):
            api_name = item.data(1)
            self.menuActionClicked.emit(api_name)


        #indexes = self.selectedIndexes()
        #print(action.text())
        #print(indexes[0].row())
       # if len(indexes) > 0:

        #    indexSelection = indexes[0]
         #   print(indexSelection.row())
          #  self.menuActionClicked.emit([self.model.objets[indexSelection.row()]],action.text())

            
       
