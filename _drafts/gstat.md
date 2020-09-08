---
date: '2014-06-10 12:27 -0700'
layout: post
title: |
    R tip: G-Test G-Statistic G\^2 likelihood ratio, or whatever else you
    might want to call it.
---

When analyzing categorical data, sometimes Chi-Square just isn't the
right distribution for testing goodness-of-fit or testing Independence.
So many people recommend a G test instead.
<a href="http://www.biostathandbook.com/chiind.html" class="ext-link"> http://www.biostathandbook.com/chiind.html</a>

Being a user of
<a href="http://cran.r-project.org" class="ext-link"> R</a>, obviously
I'd like to also run this test along with my other tests. A little
searching the web, and answers are littered with, "R doesn't have g-test
built in, here's code to do it yourself..." Which is 1/2 true, unlike
the chisq.test the base R does not appear to have a g-test. I'd rather
leave coding of standard statistics to people who really know the ins
and outs of the formulas and have a good way to verify the answer.

So, a few hours later I find
<a href="http://cran.r-project.org/web/packages/Deducer/" class="ext-link"> Deducer</a>
has
<a href="http://www.rdocumentation.org/packages/Deducer/functions/likelihood.test" class="ext-link"> likelihood.test</a>
So we're all good, right?

Well then when I got significant results I started looking for Post-hoc
tests. In doing so it turns out that the following also do G-tests as
part of their Measures of Association tests (typically used as post-hoc
tests):

-   <a href="http://cran.r-project.org/web/packages/vcd/" class="ext-link"> vcd</a>
    \|
    <a href="http://www.rdocumentation.org/packages/vcd/functions/assocstats" class="ext-link"> assocstats</a>
-   <a href="http://cran.r-project.org/web/packages/polytomous/" class="ext-link"> polytomous</a>
    \|
    <a href="http://www.rdocumentation.org/packages/polytomous/functions/associations" class="ext-link"> associations</a>

So there, base R doesn't have it, but at least 3 packages do so people
don't need to keep re-writing it.

FYI
<a href="http://www.rdocumentation.org/" class="ext-link"> http://www.rdocumentation.org/</a>
is awesome if you haven't seen it yet.

