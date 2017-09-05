# ClosestPoint
<b><br> A little QGIS plugin to find the nearest point from a points layer to a lines layer, inspire by:
http://gis.stackexchange.com/questions/396/nearest-neighbor-between-a-point-layer-and-a-line-layer  </b>

WARNING one ! : This plugin only deal with points and lines objects not multi-points or multi-lines objects !

WARNING two ! : read below, in very hypothetical spetial cases depending on a chosen parameter asked, mismatchs may occur.

WARNING three !: Work with projected datas only, in other words do not use geographical (long-lat type) reference systems !

In order to work, previous starting, the user must choose a selection of points in the point layer and a selection of lines in the lines layers.
Of course, all ojects can be selected. 
It plots the nearest projection of the points to a the lines.

It use the QGIS function 'nearestNeighbor' and ask for a k parameter. 
This function is used to speed up the code and not compare a point object to all the vertex and nodes of all the lines'ones.
This parameter 'k' is used to return this very number k of nearest neighbor lines objects to a single point object. 
See for further explanations for instance: http://blog.vitu.ch/10212013-1331/advanced-feature-requests-qgis. 
Once the nearest neighbors are found the point is projected to the closest vertex or nodes.
As this function use bounding boxes, errors may occurs in special/hypothetical cases with very special geometries that could share the same or nearly same bounding boxes and so the closest geometry may not be "retreaved' by the nearestNeighbor' process.
The speed of the working process depend of this K parameter.
With few lines objets of equal size you may use k=1, but rather use k=3 in general cases. 
With bigger amount of lines near a point better to rise k to k=5 or even greater.

Althougth same treatment exists in a better way with sql function in postgis or can be achieved with grass v.net.connect, i hope this plugins may be of some help. 
