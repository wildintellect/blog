---
date: '2009-01-18 20:40 -0700'
layout: post
title: Grass Syntax Hints
---

Short Story
-----------

<a href="http://grass.osgeo.org" class="ext-link"> GRASS GIS</a> command
line syntax can be a little tricky and none of the graphical interfaces
seem to make it easy because there's always some option you need that
isn't on the GUI.

Importing a shapefile

    v.in.ogr dsn=/path/to/folder/ layer=nameofshp output=giveitaname

notes: don't put .shp on the layer name, If it complains about not being
the right projection but you know it is add a -o (no that's not a zero)

Long Story
----------

I was testing out <a href="http://qgis.osgeo.org" class="ext-link"> QGIS
1.0</a> and the grass toolbox v.in.ogr was having issues, without giving
me an useful error message to work from.

So I compiled the latest grass release (6.4 RC2) and tried the new
wxpython interface which also failed.

Lucky for me the good ol command line worked once I gave it all the info
it wanted in the proper syntax.

-   Posted: 2009-01-18 20:40 (Updated: 2009-02-15 13:02)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [qgis](category/qgis.html) [grass](category/grass.html)
    [gis](category/gis.html) [research](category/research.html)

Comments
--------

No comments.
