# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os
import os.path
import doAbout
import doListLayers2
from qgis.gui  import QgsMapCanvas

# chargement des fichiers d'interface graphique
 
import fonctionsF

#Fonction de reconstruction du chemin absolu vers la ressource image
def getThemeIcon(theName):
    myPath = CorrigePath(os.path.dirname(__file__));
    myDefPathIcons = myPath + "/icons/"
    myDefPath = myPath.replace("\\","/")+ theName;
    myDefPathIcons = myDefPathIcons.replace("\\","/")+ theName;
    myCurThemePath = QgsApplication.activeThemePath() + "/plugins/" + theName;
    myDefThemePath = QgsApplication.defaultThemePath() + "/plugins/" + theName;
    #Attention, ci-dessous, le chemin est à persoonaliser :
    #remplacer "extension" par le nom du répertoire de l'extension.
    myQrcPath = "python/plugins/extension/" + theName;
    if QFile.exists(myDefPath): return myDefPath
    elif QFile.exists(myDefPathIcons): return myDefPathIcons  
    elif QFile.exists(myCurThemePath): return myCurThemePath
    elif QFile.exists(myDefThemePath): return myDefThemePath
    elif QFile.exists(myQrcPath): return myQrcPath
    elif QFile.exists(theName): return theName
    else: return ""

#Fonction de correction des chemins
#(ajout de slash en fin de chaîne)
def CorrigePath(nPath):
    nPath = str(nPath)
    a = len(nPath)
    subC = "/"
    b = nPath.rfind(subC, 0, a)
    if a != b : return (nPath + "/")
    else: return nPath  

    
class MainPlugin(object):
  def __init__(self, iface):
    #self.name = "Closest Point"
    #référence à l'objet interface QGIS
    self.iface = iface
    self.toolButton = QToolButton()
    self.toolButton.setMenu(QMenu())
    self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)
    self.iface.addToolBarWidget(self.toolButton)

  def initGui(self):
    #déclaration des actions élémentaires
    menuIcon = getThemeIcon("ClosestPoint.png")
    self.commande2 = QAction(QIcon(menuIcon),"Closest Point",self.iface.mainWindow())
    self.commande2.setText("Closest Point")

    menuIcon = getThemeIcon("about.png")
    self.about = QAction(QIcon(menuIcon), "Read me", self.iface.mainWindow())
    self.about.setText("Read me")
    #Construction du menu
    ButtonIcon = getThemeIcon("ClosestPoint.png")
    self.toolButton.setIcon(QIcon(ButtonIcon))
    menu = self.toolButton.menu()
    menu.addAction(self.commande2)
    menu.addSeparator()
    menu.addAction(self.about)
    #Construction du menu Vector
    self.iface.addPluginToVectorMenu("Closest Point", self.commande2)
    self.iface.addPluginToVectorMenu("Closest Point", self.about)

    #Connection de la commande à l'action
    
    QObject.connect(self.commande2,SIGNAL("triggered()"),self.LoadDlgBox2)
    QObject.connect(self.about,SIGNAL("triggered()"),self.doInfo)

  #Méthode au déchargement de l'extension
  def unload(self):
    self.iface.removePluginMenu("Closest Point", self.commande2)
    self.iface.removePluginMenu("Closest Point", self.about)
   
    """
    self.iface.removeToolBarIcon(self.commande2)
    self.iface.removeToolBarIcon(self.about)
    """
   
  #Exemple d'appel d'une boîte de dialogue (ici : exemple d'objets Qt) 
  def LoadDlgBox2(self):
      d = doListLayers2.Dialog()
      #d.show()
      d.exec_()

  def doInfo(self):
      d = doAbout.Dialog()
      d.exec_()
