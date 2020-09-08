---
date: '2014-04-24 02:42 -0700'
layout: post
title: Batch convert Natural Earth SQLite to Spatialite
---

Happened to be making some maps today, and realized 1:110m would be
better than 1:10m for small world maps in R (much faster too). I had the
whole
<a href="http://www.naturalearthdata.com/" class="ext-link"> Natural
Earth</a> dataset downloaded in sqlite format. SQLite is great but I
can't run spatial queries on that in Spatialite format (they store the
geometries differently).

<a href="http://gdal.org/ogr" class="ext-link"> GDAL/OGR</a> to the
rescue:

``` {.wiki}
ogr2ogr -f SQLite natearth_vector_spatialite.sqlite natural_earth_vector.sqlite -skip-failures -nlt PROMOTE_TO_MULTI -dsco SPATIALITE=YES
```

Turns out Spatialite, and I suspect Postgis, don't like when you mix
Multi and non Multi geometries if a column is declared Multi. Thankfully
EvenR solved this in gdal 1.10 with -nlt PROMOTE\_TO\_MULTI

A few hours later, 400+MB of great base material for cartography...

Oh wait, try to dissolve countries into UN subregions, what are all
those weird partial lines in the middle of what should be solid
polygons? Slivers of course, places where the topology of borders are
not snapped.

Solution?

1.  Processing in QGIS, GRASS tool v.dissolve, advanced set a tolerance

OR

1.  Buffer the polygons 1st before smushing (Thanks Brian)

    ``` {.wiki}
    CREATE TABLE subregionsT AS
    SELECT subregion,CastToMultiPolygon(GUnion(Buffer(Geometry,0.00001))) as geometry
    FROM ne_110m_admin_0_countries
    GROUP BY subregion;
    ```

Solution 1 is probably cleaner, as I don't have to now clip the
continents to match the coastline again, but solution 2 let me keep it
all in the same db where the data was to start with less steps.

