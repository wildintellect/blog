---
date: '2009-05-16 15:11 -0700'
layout: post
title: 'Inkscape to Scribus to PDF document production: How to make a flyer'
---

It's comes up quite often that I need a flyer for this or that. Just a
few pages, sometime quarter, third or half sheets for putting up around
campus for people to see. Once you do a few though, it often happens
that you just need the same thing again later with a few minor
variations. Sure you could just do it all in one application, but when
not doing full pages then you have to keep messing with duplicating your
information 2-4 times on the same in a way that lines up well with being
cut.

This is where layout comes in handy, more specifically I use
<a href="http://www.scribus.net/" class="ext-link"> Scribus</a>. The
idea here is make one image and then replicate it multiple times across
a page all at once evenly. Well that and make a high resolution ready to
print PDF.

So start by making your image/item. In this case I don't have a ton of
text and it's kinda free float style (not paragraph) so I used
<a href="http://www.inkscape.org/" class="ext-link"> Inkscape</a>, well
that and it's the format the flyer was originally given to me in. Had
there been more text I would have started with
<a href="http://openoffice.org" class="ext-link"> OpenOffice</a>, done
the graphics in Inkscape or Gimp and done 100% of the layout in Scribus.

After writing the text, changing and scaling fonts, putting in the
image, adjusting transparencies and background colors it's now time to
export the image. From Inkscape particularly exporting to bitmap(png)
gives you the chance to specify you dpi and ensure it will show up
correctly when you insert it in to other documents. For printing I
usually use 300dpi, and in this case to cut out dealing with margins
only exported the drawing, not the page.

In Scribus:

1.  Now I set a guide to split the page in 1/2.
2.  Turn on guide snapping and grid snaping.
3.  Draw an image box, snapping it to the guides.
4.  Get picture, grab the png export
5.  Duplicate(copy) and snap a second one onto the bottom 1/2
6.  PDF export, no compression

And walla, the next Linux User's Group of Davis Installfest flyer is
done.

See Attached:

-   Inkscape svg
-   Export png
-   Scribus sla
-   <a href="http://blog.wildintellect.com/files/lugod/if-flyer-200905.pdf" class="ext-link"> Final
    Product pdf</a>

<!-- -->

