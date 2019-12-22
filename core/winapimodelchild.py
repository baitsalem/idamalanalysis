#!/usr/bin/env python


from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt, QVariant 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTreeView

from winapihandler import WinApiHandler 


class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)


    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0


class WinApiModelc(QAbstractItemModel):
    def __init__(self, parent=None):
        super(WinApiModelc, self).__init__(parent)

        self.rootItem = TreeItem(("Address", "Name"))
        self.setupModelData(self.rootItem)

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        
        item = index.internalPointer()

        if ( role == Qt.ForegroundRole ):
            if (item.childCount() == 0):
                return QVariant(QColor(Qt.blue))

        if role != Qt.DisplayRole:
            return None


        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, parent):

        
        self.winapi_handler = WinApiHandler()  
        
        for func in self.winapi_handler.winapi_tree.keys():
            
            item = TreeItem(self.winapi_handler.winapi_tree[func][0],parent)
            parent.appendChild(item)
            for ref in self.winapi_handler.winapi_tree[func][1:]:
                item1 = TreeItem(ref,item)
                item.appendChild(item1)


