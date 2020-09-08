---
date: '0000-00-00'
layout: post
title: 'Setting up Trac, getting past the errors.'
---

So I thought the install would go smooth but a few hiccups always creep
in.

Basically I followed these
<a href="http://trac.edgewall.org/wiki/TracInstallUbuntu" class="ext-link"> instructions</a>
and another page for
<a href="http://trac.edgewall.org/wiki/TracCgi" class="ext-link"> authentication</a>

With some diligent work I worked through: (make sure to look at your
apache logs, mines at /var/log/apache2/error.log)

1.  mod\_python is the way to go in terms of setup, speed etc.
2.  Get an IOError: zipimport: go check the permission on the mentioned
    file, make sure it's at least 644 example:

         sudo chmod 644 setuptools-0.6c9-py2.5.egg

<!-- -->

1.  Python Option and Set Env PYTHON\_EGG\_CACHE flat out didn't work
    for me though as
    <a href="http://stackoverflow.com/questions/215267/how-do-you-fix-a-trac-installation-that-begins-giving-errors-relating-to-python" class="ext-link"> reported
    and worked around</a>, although a fix to the code eludes.
2.  Import Error on compat, take a look at this
    <a href="http://trac.edgewall.org/ticket/7526" class="ext-link"> ticket</a>

-   Posted: 2008-12-19 03:20 (Updated: 2009-02-12 22:47)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [install](category/install.html)

Comments
--------

No comments.
