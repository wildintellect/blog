# How big was that database?

Database servers are great, but there's a lot of magic in there sometimes and it can be hard to figure just how much storage is being taken up by what database and which tables.

A nice little hint on how to check the size of the whole or parts of you database server (Postgres): <a href="http://feeding.cloud.geek.nz/2009/02/finding-size-of-postgres-database-on.html" class="ext-link"> http://feeding.cloud.geek.nz/2009/02/finding-size-of-postgres-database-on.html</a>

Or for the lazy

    SELECT pg_database.datname,
           pg_size_pretty(pg_database_size(pg_database.datname)) AS size
      FROM pg_database;

-   Posted: 2011-05-19 17:25 (Updated: 2012-09-25 23:24)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [osgeo](category/osgeo.html) [postgis](category/postgis.html) [database](category/database.html)

## Comments

No comments.
