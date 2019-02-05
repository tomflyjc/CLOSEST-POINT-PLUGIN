# -*- coding: utf-8 -*-

import os
import os.path
from qgis.core import QgsProject, QgsMapLayer, QgsWkbTypes
from qgis.PyQt.QtCore import QFileInfo, QSettings, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox,QDialog

import sys
#from qgis.core import *
#import de la classe boîte de dialogue "A propos ..."
from aboutClosestPoint import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		
