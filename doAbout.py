# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
#import de la classe boîte de dialogue "A propos ..."
from about import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		
