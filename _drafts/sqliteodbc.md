---
date: '2008-12-22 23:44 -0700'
layout: post
title: SQLite and ODBC for Data Entry
---

The one downside of all the good database systems is the lack of an easy
tool for entering data, especially coding in data off of hand written
field forms.

I recently revisited the idea of using Open Office Base or Access as a
front end to better databases. In this particular case due the number of
issues and my familiarity I got Access working, I plan to go back and
also get OOo working next chance I get and taking over my friends
windows box (The data entry is for her anyways).

Tools: sqlite-odbc driver (I tested it on Windows and Linux) An ODBC
client: Access, Excel, Open Office Base, Calc

Issues:

1.  All your tables must have a primary key declared.
    1.  If you don't have one it's real quick using the Firefox SQL
        Manager to fix that, however you have to make new tables),
        something like this.

            CREATE TABLE NewData (pk INTEGER PRIMARY KEY AUTOINCREMENT, Afield, someotherfield);
            INSERT INTO NewData (Afield,someotherfield) SELECT * FROM Data;
            DROP TABLE Data;
            ALTER TABLE NewDATA RENAME TO Data;

2.  Declaring field types as TEXT, Access will import them as blobs if
    you do and this makes linking the tables difficult. Just drop the
    type.
3.  The Relationship tool in Access and Open Office are useless with
    linked-tables in this case. OO tells you so, Access doens't.
    1.  To get around this I created nested forms each based on 1 table.
        When inserting a nested table into another I built in the
        relationship to the form so that for every record in the parent
        child records would be matched automatically.

More details to come soon...

List of useful links:

-   a
-   b

<!-- -->

-   Posted: 2008-12-22 23:44 (Updated: 2009-02-12 22:48)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [access](category/access.html)
    [sqlite](category/sqlite.html) [odbc](category/odbc.html)
    [openoffice](category/openoffice.html)
    [database](category/database.html)

Comments
--------

No comments.
