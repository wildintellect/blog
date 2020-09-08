---
date: '0000-00-00'
layout: post
title: 'Scan over wifi from multi-functions in Linux'
---

Ended up needing to configure a few multi-function machines to print and
scan via wifi with Linux. Here's the details of what you need to know.
Specifically I did a Brother HL-2280DW and an Epson WF-3540 on Ubuntu
12.04

In general set a static IP address, either on the printer or with your
home router using DHCP reservations based on MAC address.

Figuring out the device URI was the trickiest part as Ubuntu never seems
to guess that quite right. The drivers for printing tend to be found
automatically. If that fails both vendors have them available on their
website.

Brother
-------

### Printing

Add Printer, from network, give it the ip of the machine, then pick the
lpd option.

``` {.wiki}
Device URI: lpd://192.168.1.1xx/BINARY_P1
```

### Scanning

Go to the brother
<a href="http://support.brother.com" class="ext-link"> support site</a>
and get the following files for installation.

-   Scanner driver
    -   brscan4-0.4.2-1.amd64.deb
-   Scanner Setting File
    -   brother-udev-rule-type1-1.0.0-1.all.deb

Now also make sure you have *sane* installed.

Run the following to register your multi-function

``` {.wiki}
brsaneconfig4 -a name=Brother model=HL-2280DW ip=192.168.1.1xx
```

Should now work with sane based programs.

Epson
-----

### Printing

Add Printer, from network, give it the ip of the machine, then pick the
lpd option.

``` {.wiki}
Device URI lpd://192.168.1.1xx/printers/epson
```

### Scanning

Search the
<a href="http://download.ebz.epson.net/dsc/search/01/search/" class="ext-link"> epson
download site</a> for drivers. I needed:

-   WF-3540 Series Scanner Driver Linux core package&data package
    -   iscan-data\_1.28.0-2\_all.deb
    -   iscan\_2.29.3-1\~usb0.1.ltdl7\_amd64.deb
-   WF-3540 Series Scanner Driver Linux network plugin package
    -   iscan-network-nt\_1.1.1-1\_amd64.deb

Install them in that order. Now also make sure you have *sane*
installed. Then edit /etc/sane.d/epkowa.conf (This is the part no one on
web seems to describe.) Can't find the file you might needs to install
*libsane-extras*

In the net section add a line with your multi-function ip address.

``` {.wiki}
net 192.168.1.1xx
```

Save that and now when you open iscan or sane it should find your
scanner.

-   Posted: 2014-05-13 22:07
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [printer](category/printer.html)
    [scanner](category/scanner.html) [ubuntu](category/ubuntu.html)

Comments
--------

No comments.
