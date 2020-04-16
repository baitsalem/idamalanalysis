#-*- coding: latin_1 -*-

from collections import namedtuple
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant, QObject, pyqtSlot , QMetaObject, pyqtSignal, QThreadPool

from winapifind import *

"""
    Import this module if you want to interpret the volatility command results 
"""


class WinApiModel(QAbstractTableModel):

    """
    Model that parses results of a  volatility command 
    """

    def __init__(self):
        
        super(WinApiModel,self).__init__()
        
        self.titresColonnes = ["func_addr","func_name"]        
        self.rows  = []

        
    def builtModel(self):

        self.rows = get_winapi_addr()


    def headerData(self,section,orientation,role):

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.titresColonnes[section]

        return QVariant()

    def columnCount(self,parent):

        return len(self.titresColonnes)

    def rowCount(self,parent):
        return len(self.rows)

    def data(self,index,role):

        if role == Qt.DisplayRole and index.isValid():

            return (self.rows[index.row()][index.column()])
        return QVariant()





