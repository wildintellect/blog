---
date: '2011-09-26 12:08 -0700'
layout: post
title: GPT Booting with Ubuntu
---

So if you buy a 3 TB drive (or anything bigger than 2TB) and want to use
it as the primary drive for your machine you will need to use a GPT
paritioning system instead of the classic MBR.

Here's a couple of tricks/tips which should help:

-   You need to be using an OS that has GRUB2
-   When partitioning, the 1st partition should be a 1 MB section with
    the bios\_grub flag (recent versions of the Ubuntu installer, at
    least 11.04 has this option, 10.04 I had to set if with a Live disc
    and parted)
-   When you get to the install GRUB question, if you happen to be
    installing to something other than /dev/sda say no, and then it will
    ask you which drive or partition to install to.

<!-- -->

-   Posted: 2011-09-26 12:08
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [ubuntu](category/ubuntu.html)

Comments
--------

No comments.
