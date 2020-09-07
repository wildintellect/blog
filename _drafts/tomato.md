# Router gone bad, Open Source It!

I'm not sure why but home routers seem to have a finite lifetime before they start misbehaving in strange ways. Last week mine started acting up, in a way I've never seen before, one in which power cycling seems to have no effect.

**What was it doing?** It decided I wasn't allowed to view websites or any other type of connection to one very specific subnet - which is where my servers happen to live. The rest of Internet worked as usual.

After, a couple of days of trying to figure out where the problem was I did narrow it down to my home router by plugging my laptop into the Internet service directly - which worked.

**Part 2:** Now that I knew it was the router and had some traceroutes handy, my best guess was that my computer was sending the request but the data was never coming back from the server, browser gave messages like server took too long to return request. Notice how it didn't say it couldn't find the server. Traceroutes no matter how many hops (should have been 16) keep going with \* \* \* which made me think and endless loop was somewhere.

Fingers started to point to the built in <a href="http://en.wikipedia.org/wiki/Stateful_firewall" class="ext-link"> SPI Firewall</a>.

So I tried turning off SPI, NAT filtering...upgrade the router firmware, reset the settings...nothing. (Maybe I need to try the mythical 30-30-30 method to flush the nvram).

**Plan B** Giving up on the router I went to my spare router. Hooked it all up, got connected, turned on the firewall and wham no Internet at all and reverting the settings didn't fix it.

Good news is I had intentionally bought 2 routers that shipped or were capable of running Linux based open source firmware. (Netgear WGR614Gv8, Asus WL520gu) So began the night of researching how to flash an open source firmware onto a router.

**Solution:** After reading many pages, and some 20-100 step processes I found a nifty 3 step that worked great the first time. <a href="http://en.wikibooks.org/wiki/Tomato_Firmware/Installation_and_Configuration#Installing_on_an_ASUS_WL-520gU" class="ext-link"> Flashing an Asus wl520gu in 3 steps with Tomato</a> (I actually used <a href="http://tomatousb.org/" class="ext-link"> Tomato-usb</a>)

Note: this method will probably work with <a href="http://www.dd-wrt.com/" class="ext-link"> DD-WRT</a> or <a href="http://openwrt.org/" class="ext-link"> OpenWrt</a> too but I didn't try it.

-   Posted: 2011-06-16 18:39
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [asus](category/asus.html) [router](category/router.html) [foss](category/foss.html) [linux](category/linux.html)

## Comments

No comments.
