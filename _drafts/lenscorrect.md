# Lens Correction for GoPro Hero2

Fisheye lenses are awesome, such a wide view captures great scenes. However if you want to stitch the photos together, that distortion on the edges causes some real trouble.

So you want to fix it, great, Digikam has a lens correction tool built in based on <a href="http://lensfun.sourceforge.net/" class="ext-link"> Lensfun</a>. Hmm, wait there's no record for GoPros. Ok take test shots with lots of straight lines(buildings work great) and upload them to the awesome maintainer of Lensfun via <a href="http://wilson.bronger.org/calibration" class="ext-link"> http://wilson.bronger.org/calibration</a>. Wait a couple days, get back a lens model, sweet.

In Digikam, try it on 1 photo, awesome it works, well at least on Digikam 3.5 (in Digikam 2.x it creates distortion art). But then you go to do it in batch on all your photos and wham, nothing, big fat nothing. Turns out it's a known bug: <a href="https://bugs.kde.org/show_bug.cgi?id=303848" class="ext-link"> https://bugs.kde.org/show_bug.cgi?id=303848</a>

Tried GIMP, with Gimp-Lenfun. Got it installed and working but it doesn't correct the distortion. Also batch processing in GIMP is somewhat a PITA, there are a couple of addons but they don't always work, or allow using addon filters.

[![gopro distortion before and after](../raw-attachment/blog/lenscorrect/overview.png "gopro distortion before and after")](../attachment/blog/lenscorrect/overview.png.html)

I was going to leave it at that and wait for a fix sometime down the road, but then had some down time. So a few hours later using Python, Lensfun (lensfunpy) and OpenCv (python-opencv) I got it to work at least on my laptop running Ubuntu 14.04. Trying it on my Ubuntu 12.04 desktop resulted in similar distortion art as digikam. So I tried updating opencv, no change. Turns out there's a bug in lensfun fixed between 2.5 and 2.8. So I had to Backport 2.8 to Ubuntu 12.04 (<a href="http://opensourcehacker.com/2013/03/20/how-to-backport-packages-on-ubuntu-linux/" class="ext-link"> instructions</a>). If you want my backport its in my <a href="https://launchpad.net/~wildintellect/+archive/ubuntu/wildintellect/+packages" class="ext-link"> PPA</a>

Want to see my code for doing it in batch, you're in luck head over to github: <a href="https://github.com/wildintellect/lenscorrection" class="ext-link"> https://github.com/wildintellect/lenscorrection</a>

-   Posted: 2014-10-29 13:44 (Updated: 2014-10-29 14:16)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [python](category/python.html) [photography](category/photography.html)

### Attachments

-   [overview.png](../attachment/blog/lenscorrect/overview.png.html "View attachment") <a href="../raw-attachment/blog/lenscorrect/overview.png" class="trac-rawlink" title="Download"><img src="../chrome/common/download.png" alt="Download" /></a> (565.7 KB) - added by *wildintellect* <a href="http://192.168.1.113/timeline?from=2014-10-29T13%3A45%3A25-07%3A00&amp;precision=second" class="timeline" title="2014-10-29T13:45:25-07:00 in Timeline">6 years</a> ago. “gopro distortion before and after”

## Comments

No comments.
