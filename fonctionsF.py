# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Fichier des fonctions du plugin cc
                                 A QGIS plugin
 Projette des points sur une ligne/bordure de polygone à la distance la plus courte: "ClosestPoint"
                              -------------------
        begin                : 2013-11-04
        copyright            : (C) 2017 by Jean-Christophe Baudin d'après "Nearest neighbor between a point layer and a line layer
                               in http://gis.stackexchange.com/questions/396/
                               nearest-pojected-point-from-a-point-
                               layer-on-a-line-or-polygon-outer-ring-layer
        email                : jean-christophe.baudin@ymail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import unicodedata,sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from qgis.core import *
from qgis.gui import *

from osgeo import ogr
from math import sqrt
from sys import maxint

import csv, sys
import re
import os
import unicodedata
 
def twodecimal(number):
    NB=int((number * 100) + 0.5) / 100.0 # Adding 0.5 rounds it up
    return  NB
def magnitude(p1, p2):
    if p1==p2: return 1
    else:
        vect_x = p2.x() - p1.x()
        vect_y = p2.y() - p1.y()
        return sqrt(vect_x**2 + vect_y**2)

def intersect_point_to_line(point, line_start, line_end):
    line_magnitude =  magnitude(line_end, line_start)
    u = ((point.x()-line_start.x())*(line_end.x()-line_start.x())+(point.y()-line_start.y())*(line_end.y()-line_start.y()))/(line_magnitude**2)
    # closest point does not fall within the line segment, 
    # take the shorter distance to an endpoint
    if u < 0.0001 or u > 1:
        ix = magnitude(point, line_start)
        iy = magnitude(point, line_end)
        if ix > iy:
            return line_end
        else:
            return line_start
    else:
        ix = line_start.x() + u * (line_end.x() - line_start.x())
        iy = line_start.y() + u * (line_end.y() - line_start.y())
        return QgsPoint(ix, iy)



def getVectorLayerByName(NomCouche):
    layermap=QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layermap.iteritems():
        if layer.type()==QgsMapLayer.VectorLayer and layer.name()==NomCouche:
            if layer.isValid():
               return layer
            else:
               return None
            

    



