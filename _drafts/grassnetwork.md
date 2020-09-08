---
date: '2009-04-27 11:49 -0700'
layout: post
title: Network analysis using GRASS
---

I ended up wanting to analyze commute paths on several networks, but
instructions on how to properly prepare a network file with new points
snapped to it as nodes was a little less than clear. I'm not 100% sure
this is right but it is pieced together from the command history
<a href="http://" class="ext-link"> GRASS</a> stored with each layer in
my mapset.

    #bring the layer in
    v.in.ogr -o dsn="/scratch/congelton/davis_ped_net/ped_net_sep28.shp" output="pednets28" min_area=0.0001 snap=-1

    #find the nearest line to a point and create a line that connects them
    v.distance -p from="davissubset@PERMANENT" to="pednetsep28" from_type="point" to_type="point,line,area" from_layer=1 to_layer=1 output="ppl2pednet" dmax=-1 upload="dist" column="dist"

    #add categories to the distance lines(I think this is required otherwise v.net won't work later, if the cat column is already populated then you can skip this)
    v.category input="ppl2pednet" output="ppl2pednetcat" type="point,line,boundary,centroid,area" option="add" cat=1 layer=1 step=1

    #patch the distance lines to the to the original points, so you have the nodes for v.net
    v.patch input="ppl2pednetcat,pednets28" output="pplpednet"

    # patch the distance lines to the network
    v.patch input="pplpednet,davissubset" output="pplonpednet"

    #I ran a clean before I did the actual v.net command to make sure I dropped things that wouldn't work, outliers
    v.clean input="pplonpednet" output="pplonpednetclean3" type="line,point" tool="snap,break" thresh=3,3

    #run the network shortest path using the original points as starting points and end points in batch from a csv, the point id is it's cat
    v.net.path input="pplonpednetclean3" output="dcommute3" type="line,boundary" alayer=1 nlayer=1 file="pplonpednetclean.csv" dmax=1000


    #example of the csv
    #autonumber,Start node cat, end node cat
    1       1       3000
    2       5       3000
    3       6       3000
    4       7       3000
    5       8       3000
    6       9       3000
    7       10      3000
    8       14      3000
    9       15      3000
    10      25      3000
    11      26      3000
    12      27      3000
    #yes all my people traveled to the same end point

Things to watch out for:

-   A network file should have both lines and points with the same layer
    number(ie 1\_points 1\_lines)
-   A network file with no cat column in the points component

<!-- -->

