#!/usr/bin/python
########################################################################
# Copyright (c) 2019
# AIT SALEM BOUSSAD <boussad.aitsalem<at>gmail<dot>com>
# All rights reserved.
########################################################################
#
#  This file is part of IDAMalAnalysis
#
#  IDAMalAnalysis is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see
#  <http://www.gnu.org/licenses/>.
#
########################################################################

from idaapi import PluginForm
from PyQt5 import QtCore, QtGui, QtWidgets
import sip
from widgets.mainform import MainForm

class IDAMalAnalysis(PluginForm):
    def OnCreate(self, form):
        """
        Called when the widget is created
        """

        # Get parent widget
        self.parent = self.FormToPyQtWidget(form)
        self.printBanner()
        self.PopulateForm()


    def PopulateForm(self):
        
        #Create layout
        layout = QtWidgets.QVBoxLayout()
        self.mainform = MainForm()
        layout.addWidget(self.mainform)
        self.parent.setLayout(layout)


    def printBanner(self):

         
        banner= '''
                ###################################################################
                ___ ____    _    __  __       _    _                _           _     
               |_ _|  _ \  / \  |  \/  | __ _| |  / \   _ __   __ _| |_   _ ___(_)___ 
                | || | | |/ _ \ | |\/| |/ _` | | / _ \ | '_ \ / _` | | | | / __| / __|
                | || |_| / ___ \| |  | | (_| | |/ ___ \| | | | (_| | | |_| \__ \ \__ \ 
               |___|____/_/   \_\_|  |_|\__,_|_/_/   \_\_| |_|\__,_|_|\__, |___/_|___/
                                                                      |___/           
               #######################################################################
               By boussad AIT SALEM, www.securitylab.fr/home
               #######################################################################
               '''

        print (banner)

        print ("Loading IDAMalAnalysis IHM...")
    
    def OnClose(self, form):

        """
        Called when the widget is closed
        """
        pass

thisplugin = IDAMalAnalysis()
thisplugin.Show("IDAMalAnalysis 1.0")
