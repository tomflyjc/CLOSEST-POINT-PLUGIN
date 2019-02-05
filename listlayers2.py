# -*- coding: utf-8 -*-
# (c) JC BAUDIN 2019 02 05
# import de QGIS
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtWidgets import     (QMessageBox,
                                    QDialog,
                                    QProgressBar,
                                    QDialogButtonBox,
                                    QAction,
                                    QLabel,
                                    QComboBox,
                                    QPushButton,
                                    QLineEdit,
                                    QApplication)

 

from qgis.core import  (QgsProject,
                        QgsMapLayer,
                        QgsWkbTypes,
                       QgsVectorLayer,
                       QgsField,
                       QgsFields,
                       QgsFeature,
                       QgsFeatureSink,
                       QgsFeatureRequest,
                       QgsGeometry,
                       QgsPointXY,
                       QgsWkbTypes,
                       QgsRectangle,
                       QgsFeature,
                       QgsSpatialIndex,
                       QgsCoordinateTransform,
                       QgsFeatureRequest,
                       QgsVector,
                       QgsProject,
                       QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform)
                       
from qgis.utils import iface

import os
import os.path
import fonctionsF
import doAbout

class Ui_Dialog(object):
    """
    def __init__(self, iface):
        self.iface = iface
    """
    def setupUi(self, Dialog):
        self.iface = iface
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,340,250).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowTitle("ClosestPoint")
        
        # QLabel lancer recherche
        self.label10 = QLabel(Dialog)
        self.label10.setGeometry(QtCore.QRect(15,15,320,18))
        self.label10.setObjectName("label10")
        self.label10.setText("Select a layer of points to project (with points selected):  ")

        ListeCouchesPoint=[""]
        NbCouches=self.iface.mapCanvas().layerCount()
        if NbCouches==0: QMessageBox.information(None,"information:","No layers ! ")
        else:
            for i in range(0,NbCouches):
                couche=self.iface.mapCanvas().layer(i)
                # 0 pour point
                if couche.geometryType()== 0 or couche.geometryType()==3 :
                    if couche.isValid():
                       ListeCouchesPoint.append(couche.name())
                    else:
                       QMessageBox.information(None,"information:","No layers with points ! ")
                       return None
        self.ComboBoxPoints = QComboBox(Dialog)
        self.ComboBoxPoints.setMinimumSize(QtCore.QSize(300, 25))
        self.ComboBoxPoints.setMaximumSize(QtCore.QSize(300, 25))
        self.ComboBoxPoints.setGeometry(QtCore.QRect(10, 35, 300,25))
        self.ComboBoxPoints.setObjectName("ComboBoxPoints")
        for i in range(len(ListeCouchesPoint)):  self.ComboBoxPoints.addItem(ListeCouchesPoint[i])

        # QLabel de couche ligne
        self.label = QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15,60,320,18))
        self.label.setObjectName("label")
        self.label.setText("Select a layer of lines (with lines selected): ")

        ListeCouchesLigne=[""]
        NbCouches=self.iface.mapCanvas().layerCount()
        for i in range(0,NbCouches):
            couche=self.iface.mapCanvas().layer(i)
            # 1 pour ligne
            if couche.geometryType()== 1 or couche.geometryType()== 4 :
                if couche.isValid():
                   ListeCouchesLigne.append(couche.name())
                else:
                   QMessageBox.information(None,"information:","no layer with lines ! ")
                   return None
        
        self.ComboBoxLignes = QComboBox(Dialog)
        self.ComboBoxLignes.setMinimumSize(QtCore.QSize(300, 25))
        self.ComboBoxLignes.setMaximumSize(QtCore.QSize(300, 25))
        self.ComboBoxLignes.setGeometry(QtCore.QRect(10, 80, 300,25))
        self.ComboBoxLignes.setObjectName("ComboBoxLignes")
        for i in range(len(ListeCouchesLigne)):  self.ComboBoxLignes.addItem(ListeCouchesLigne[i])

        # QLabel entrer le facteur k nearest neighbor
        self.labelKNearestNeighbor = QLabel(Dialog)
        self.labelKNearestNeighbor.setGeometry(QtCore.QRect(15,115,280,23))
        self.labelKNearestNeighbor.setObjectName(" KNearestNeighbor")
        self.labelKNearestNeighbor.setText("Enter the k number of nearest lines objects - try 3 :")
        
        self.TextEditKNearestNeighbor = QLineEdit(Dialog)
        self.TextEditKNearestNeighbor.setMinimumSize(QtCore.QSize(40, 20))
        self.TextEditKNearestNeighbor.setMaximumSize(QtCore.QSize(40, 20))
        self.TextEditKNearestNeighbor.setGeometry(QtCore.QRect(265,115,40,20))
        self.TextEditKNearestNeighbor.setObjectName("TextEditKNearestNeighbor")
        
        #Exemple de QPushButton
        self.DoButton = QPushButton(Dialog)
        self.DoButton.setMinimumSize(QtCore.QSize(200, 20))
        self.DoButton.setMaximumSize(QtCore.QSize(200, 20))        
        self.DoButton.setGeometry(QtCore.QRect(60,150, 200, 20))
        self.DoButton.setObjectName("DoButton")
        self.DoButton.setText(" Plot the nearest points !")
 
     
        #Exemple de QLCDNumber
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimumSize(QtCore.QSize(260, 15))
        self.progressBar.setMaximumSize(QtCore.QSize(260, 15))
        self.progressBar.setGeometry(QtCore.QRect(30,175,260,15))
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(
            """QProgressBar {border: 2px solid grey; border-radius: 5px; text-align: center;}"""
            """QProgressBar::chunk {background-color: #6C96C6; width: 20px;}"""
        )
        #Pose a minima une valeur de la barre de progression / slide contrôle
        self.progressBar.setValue(0)
        
        
        #Exemple de QPushButton
        self.aboutButton = QPushButton(Dialog)
        self.aboutButton.setMinimumSize(QtCore.QSize(70, 20))
        self.aboutButton.setMaximumSize(QtCore.QSize(70, 20))        
        self.aboutButton.setGeometry(QtCore.QRect(30, 195, 70, 23))
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.setText(" Read me ")
        
        self.PushButton = QPushButton(Dialog)
        self.PushButton.setMinimumSize(QtCore.QSize(100, 20))
        self.PushButton.setMaximumSize(QtCore.QSize(100, 20))
        self.PushButton.setGeometry(QtCore.QRect(185, 195, 100,20))
        self.PushButton.setObjectName("PushButton")
        self.PushButton.setText("Close")

        self.PushButton.clicked.connect(Dialog.reject)
        self.ComboBoxPoints.activated[str].connect(self.onComboP)
        self.ComboBoxLignes.activated[str].connect(self.onComboL)
        self.aboutButton.clicked.connect(self.doAbout)
        self.DoButton.clicked.connect(self.Run)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
                                                             
    def onComboP(self):
        SelectionP = self.ComboBoxPoints.currentText()
        #QMessageBox.information(None,"information:","couche selectionnee: "+ (SelectionP))
        CoucheP=fonctionsF.getVectorLayerByName(SelectionP)
        counterP=0
        for featP in CoucheP.selectedFeatures():
            counterP+=1
        if counterP==0:
            QMessageBox.information(None,"information:","Select a least one point feature in "+ str(CoucheP.name())+" layer !")
        # Selected point only are used with :
        # EnregistrementsP=CoucheP.selectedFeatures()
        # to work with all the points of a layer change for: 
        # Enregistrements=Couche.getFeatures(QgsFeatureRequest())
        
    def onComboL(self):
        SelectionL = self.ComboBoxLignes.currentText()
        #QMessageBox.information(None,"information:","couche selectionnee: "+ (SelectionL))
        CoucheL=fonctionsF.getVectorLayerByName(SelectionL)
        counterL=0
        for featL in CoucheL.selectedFeatures():
            counterL+=1
        if counterL==0:
            QMessageBox.information(None,"information:","Select a least one line feature in "+ str(CoucheL.name())+ " layer !") 
        
                
    def doAbout(self):
        d = doAbout.Dialog()
        d.exec_()
    
    def Run(self):
        
        SelectionP = self.ComboBoxPoints.currentText()
        CoucheP=fonctionsF.getVectorLayerByName(SelectionP)
        SelectionL = self.ComboBoxLignes.currentText()
        CoucheL=fonctionsF.getVectorLayerByName(SelectionL)
        counterP=counterL=counterN=counterProgess=0
        for featP in CoucheP.selectedFeatures():
            counterP+=1
        counterSelec=0
        counterSelec = int(self.TextEditKNearestNeighbor.text())
        if counterSelec==0 :
            QMessageBox.information(None,"information:","enter a value for k, at least 1 ") 
        
        #zdim est le compteur de la progress bar    
        zDim = counterP
        indexBerge=QgsSpatialIndex()
        for featL in CoucheL.selectedFeatures():
            indexBerge.insertFeature(featL)
            counterL+=1
            #QMessageBox.information(None,"DEBUGindex:",str(indexBerge)) 
        if counterP!=0:
            if  counterL!=0: 
                PtsProj= QgsVectorLayer("Point", str(CoucheP.name())+"_Projected", "memory")
                QgsProject.instance().addMapLayer(PtsProj)
                prPtsProj = PtsProj.dataProvider()
                providerP = CoucheP.dataProvider()
                fieldsP = providerP.fields()
                for f in fieldsP:
                    znameField= f.name()
                    Type= str(f.typeName())
                    if Type == 'Integer': prPtsProj.addAttributes([ QgsField( znameField, QVariant.Int)])
                    if Type == 'Real': prPtsProj.addAttributes([ QgsField( znameField, QVariant.Double)])
                    if Type == 'String': prPtsProj.addAttributes([ QgsField( znameField, QVariant.String)])
                    else : prPtsProj.addAttributes([ QgsField( znameField, QVariant.String)])
                prPtsProj.addAttributes([QgsField("DistanceP", QVariant.Double),
                                          QgsField("XDep", QVariant.Double),
                                          QgsField("YDep", QVariant.Double),
                                          QgsField("Xproj", QVariant.Double),
                                          QgsField("Yproj", QVariant.Double)])
                #QMessageBox.information(None,"DEBUG3:","npos ")
             
                for featP in CoucheP.selectedFeatures():
                    attributs=featP.attributes()
                    counterProgess+=1
                    geomP=featP.geometry()
                    PointP=geomP.asPoint()
                    nearestsfids=indexBerge.nearestNeighbor(geomP.asPoint(),counterSelec)
                    #QMessageBox.information(None,"DEBUGnearestIndex:",str(nearestsfids))
                    #http://blog.vitu.ch/10212013-1331/advanced-feature-requests-qgis
                    #layer.getFeatures( QgsFeatureRequest().setFilterFid( fid ) )
                    request = QgsFeatureRequest().setFilterFids( nearestsfids )
                    #list = [ feat for feat in CoucheL.getFeatures( request ) ]
                    # QMessageBox.information(None,"DEBUGnearestIndex:",str(list))
                    min_dist=Distance=0.0
                    nearest_point = None
                    minVal=0.0
                    first= True
                    for featL in CoucheL.getFeatures(request):
                        geomL=featL.geometry()
                        distinit,mindistpt,aftervertexinit,leftoff=geomL.closestSegmentWithContext(PointP)
                        #https://qgis.org/api/classQgsGeometry.html
                        ProjPoint=QgsPointXY(mindistpt[0],mindistpt[1])
                        Distance=fonctionsF.magnitude(PointP, ProjPoint)
                        #QMessageBox.information(None,"DEBUG", 'Distance:  Distance' +str(Distance))
                        if first:
                            minVal,nearest_point,first = Distance,ProjPoint,False
                        else:
                            if Distance < minVal:minVal,nearest_point=Distance,ProjPoint
                    PProjMin=nearest_point
                    min_dist=minVal

                    Geom= QgsGeometry().fromPointXY(PProjMin)    
                    PX=float(format(geomP.asPoint().x(), '.2f'))
                    PY=float(format(geomP.asPoint().y(), '.2f'))
                    newfeat = QgsFeature()
                    newfeat.setGeometry(Geom)
                    Values= featP.attributes()
                    Values.append(min_dist)
                    Values.append(fonctionsF.twodecimal(PX))
                    Values.append(fonctionsF.twodecimal(PY))
                    Values.append(fonctionsF.twodecimal(PProjMin.x()))
                    Values.append(fonctionsF.twodecimal(PProjMin.y()))
                    newfeat.setAttributes(Values)
                    #bascule en mode édition- comme icône crayon  :
                    PtsProj.startEditing()
                    # ce qui suit ajoute les géom et valeurs des enregistrements,
                    prPtsProj.addFeatures([ newfeat ])
                    # même effet que: PtsProj.addFeature(newfeat,True)
                    #Quitte le mode édition et enregistre les modifs:
                    PtsProj.commitChanges()
                    zPercent = int(100 * counterProgess / zDim)
                    self.progressBar.setValue(zPercent)
                    self.iface.mapCanvas().refresh()    
            else: pass          
        else: pass
                
                
             
