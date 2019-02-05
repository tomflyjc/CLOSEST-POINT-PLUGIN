# -*- coding: iso-8859-1 -*-

from qgis.PyQt.QtWidgets import QAction, QMessageBox,QDialog
from qgis.utils import iface
#import de la classe boîte de dialogue, liste des couches
# Qgis2: from listlayers2 import Ui_Dialog
from listlayers2 import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
        def __init__(self,):
                QDialog.__init__(self)
                self.setupUi(self)
 
