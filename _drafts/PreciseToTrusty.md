---
date: '2014-08-31 21:40 -0700'
layout: post
title: 'Upgrade notes Ubuntu 12.04 to 14.04'
---

Just a few things I encountered in my upgrade on my Zotac Zbox going to
from Ubuntu Precise (12.04) to Ubuntu Trusty (14.04)

-   Couldn't get it to use an iso as the upgrade material since there's
    no alternate cd anymore, so did an online upgrade which worked fine.

Fixes:

-   Atheros driver is way better, I went from 1 Mbps to 4 Mbps on
    Speedtest.net, nothing else changed in my network, the latter speed
    what I always got from other computers.
-   Streaming video full screen no longer requires gpu acceleration to
    be disabled.

Bugs (related):

-   nouveau driver hiccups on sound every few seconds when streaming
    videos
-   Nvidia Ion graphics/sounds always transmits sound on HDMI even if
    you switch to analog. In my case this provided a weird problem,
    where I couldn't use analog audio to bypass the previous bug above.
    See fix below...

Workarounds:

-   Installed the Nvidia drivers, which had major issues in 12.04
    (screen blank or not lined up with monitor/tv) - works great now
-   Forgot that Amazon Prime streaming require **hal** for flash drm get
    it from this
    <a href="https://launchpad.net/~mjblenner/+archive/ubuntu/ppa-hal" class="ext-link"> ppa</a>
-   Chromium and Chrome no longer work with Adobe flash from the repos,
    you need pepperflash

    ``` {.wiki}
    sudo apt-get install pepperflashplugin-nonfree
    sudo update-pepperflashplugin-nonfree --install
    ```

-   If you're using Apache pay attention to the 2.2 to 2.4 upgrade,
    syntax of allows and conf file names changed and are important.

<!-- -->

