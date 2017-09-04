# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import *
from qgis.gui  import QgsMapCanvas
from qgis.core import *
from qgis.gui import *
import os
from qgis.gui  import QgsMapCanvas
#import de la classe boîte de dialogue, liste des couches
from listlayers2 import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
 
