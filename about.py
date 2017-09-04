# -*- coding: utf-8 -*-

import os.path
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,320,360).size()).expandedTo(Dialog.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")

        font = QtGui.QFont()
        font.setPointSize(15) 
        font.setWeight(50) 
        font.setBold(True)
        
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,1,1,2)
         
        self.textEdit = QtGui.QTextEdit(Dialog)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.width = 320
        self.textEdit.height = 360
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
       
        self.gridlayout.addWidget(self.textEdit,2,1,5,2) 

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridlayout.addWidget(self.pushButton,4,2,1,1) 

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,3,1,1,1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Polygons_Pile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Polygons_Pile 0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><span style=\" font-weight:600;\">"
        "Plus Proche Point Projeté :</span>" "  A little QGIS plugin to find the nearest point from a points layer to a lines layer                                                                                              "+
        " <br><b>WARNING one !:</b><br> <b>This plugin only deal with points and lines objects not multi-points or multi-lines objects  !</b>                                              " +
        " <br><b>WARNING two  !:</b><br> <b>Read below, in very spetial cases, depending on a chosen parameter asked, mismatchs may occurs  !</b>                                              " +
        " <br><b>WARNING three  !:</b><br> <b>Work vith projected datas only, in other words do not use geographical (long-lat type) reference systems    !</b>                                              " +
        " In order to work, previous starting, the user must choose a selection of points in the point layer and a selection of lines in the lines layers.                                                      "+
        " Of course, all ojects can be selected. It plots the nearest projection of the points to a the lines.                                                              "+
        " It use the QGIS function 'nearestNeighbor' and ask for a k parameter : nearestsfids=indexBerge.nearestNeighbor(geomP.asPoint(),counterSelec)                          "+     #QMessageBox.information(None,"DEBUGnearestIndex:",str(nearestsfids))
        " This function is used to speed up the code and not compare a point object to all the vertex and nodes of all the lines'ones.                                      "+
        " This parameter 'k' is used to return this very number k of nearest neighbor lines objects to a single point object.                                                                      "+
        " See for instance http://blog.vitu.ch/10212013-1331/advanced-feature-requests-qgis. for further explanations.                                              "+
        " Once the nearest neighbors are found the point is projected to the closest vertex or nodes.                                                                        " +
		" As this function use bounding boxes, errors may occurs in special cases as a very spectial geometry may be the closest one but may not be 'retreaved' by the nearestNeighbor' process.  "+
        " The speed of the working process depend of this K parameter.                                                                                                          "+
        " With few lines objets of equal size you may use k=1, but rather use k=3 in general cases.                                                                               "+
	    " With bigger amount of lines near a point better to rise k to k=5 or even greater.                                                                                       "+
        " Althougth same treatments exist in a better ways - with sql function in postgis - or can be achieved with grass v.net.connect, i hope this plugins may be of some help.                                                                                                          "+
        " the plugin produces a layer of projedted points with the points layer attribute table with some more extra attributes columns :                                                                                          "+
        " - a distance attribute with the  distance between the point and the line closest vertex or node,                                                         " +
        " - two columns with the coordinates of the starting point,                                                                                                " +                                                           
        " - two columns with the coordinates of the projected point uppon lines objects,                                                                                       " +
        "                                                        "+
        "                                                                                                                                                                           "+
        " NOTA BENE: all rasters should be unchecked in layer panel or the plugin won't work !                                                                          </b>" 
        " This plugin is not a part of Qgis engine and any problems should be reported only to the author. </p></td></tr></table>"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        "<p style=\"margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
        "                   "
        "<br><b>jeanchristophebaudin@ymail.com</b><br>"
        "<br><br><i>code 0.1 (04 september 2017).</i></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))



