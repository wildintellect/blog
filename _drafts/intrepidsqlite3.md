---
date: '2009-02-10 17:46 -0700'
layout: post
title: 'Installing Sqlite 3.6.x on Ubuntu Intrepid'
---

I needed sqlite 3.6 or newer for an application I'm working on but
Ubuntu Intrepid has 3.5.9, specifically for Rtree spatial indexes. (In
order to build and use
<a href="http://www.gaia-gis.it/spatialite/" class="ext-link"> Spatialite</a>.

After weighing my options and doing a little research I noticed that the
Jaunty packages barely have any dependencies and they are already met by
Intrepid.

So I downloaded:

-   <a href="http://packages.ubuntu.com/jaunty/libsqlite3-0" class="ext-link"> libsqlite3-0</a>
-   <a href="http://packages.ubuntu.com/jaunty/libsqlite3-dev" class="ext-link"> libsqlite3-dev</a>
-   <a href="http://packages.ubuntu.com/jaunty/sqlite3" class="ext-link"> sqlite3</a>

Steps to follow:

1.  Uninstall libsqlite3-dev 3.5.9
2.  Install libsqlite3 3.6.10
3.  Install libsqlite3-dev 3.6.10
4.  Install sqlite3 3.6.10

To test with python(happens to be what I'm developing with)

    from pysqlite2 import dpapi2 as sqlite3
    print sqlite3.sqlite_version

-   Posted: 2009-02-10 17:46 (Updated: 2010-11-03 10:44)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [sqlite](category/sqlite.html)
    [intrepid](category/intrepid.html) [gis](category/gis.html)
    [spatialite](category/spatialite.html)
    [ubuntu](category/ubuntu.html)

Comments
--------

No comments.
