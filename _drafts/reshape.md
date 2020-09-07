# Reshape R - long to wide conversion

**--May be incorrect, working on a fix will post when done--** Keeping data in long format just makes sense, but for some reason statistics often requires your data in wide format. The good news is that it's much easier to go from long to wide than the other way around. Although the tool I'm about to describe can go both ways.

Using <a href="http://http://cran.r-project.org/" class="ext-link"> R</a> and pulling a dataframe in from an SQLite database the following command will take the dataframe and for every Species listed create a new column based on it. Then all the records are grouped by their Plot and the resulting Percent Cover for a given species in a plot is now a value in one of the columns instead of it being it's own row.

Plant (the data.frame)

|      |         |         |
|------|---------|---------|
| Plot | Species | PrCover |
| A    | Poppy   | 5       |
| A    | Redwood | 20      |
| B    | Oak     | 50      |
| B    | Poppy   | 10      |

     WidePlant <- reshape(Plant, v.names = "PrCover", idvar = "Plot", timevar = "Species", direction = "wide")

WidePlant (the results)

|      |               |                 |             |
|------|---------------|-----------------|-------------|
| Plot | PrCover.Poppy | PrCover.Redwood | PrCover.Oak |
| A    | 5             | 20              | NA          |
| B    | 10            | NA              | 50          |

The documentation is kinda hard to read, so here's my attempt at plain english

-   v.names = the values you want to show up under your new columns
-   idvar = the id that you want to group your data record by
-   timevar = the values that you want to make up the new columns, however many distinct values are in this column determines the number of new columns
-   direction = wide, the destination or resulting format we want

<!-- -->

-   Posted: 2009-02-18 23:43 (Updated: 2012-09-25 23:27)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [statistics](category/statistics.html) [r](category/r.html) [database](category/database.html)

## Comments

No comments.
