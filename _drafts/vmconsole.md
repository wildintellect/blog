---
date: '2010-06-08 01:22 -0700'
layout: post
title: 'More reliabe VMware Console?'
---

So VMWare server is an interesting product for virtualization. It does
some things really well (Like letting you open a desktop OS without
installing remote desktop tools) and seems to just fail at others (like
a web management tool that you can't get into 1/2 the time).

Tonight's frustration, lack of support for Firefox 3.6. But there's a
bit of a workaround. If you go into about:config and find
security.enable\_ssl2, and set it to true the Web Access site actual
seems to work reliably (so far).

However the console to any VM will always timeout. To work around this:

1.  make sure you've installed the console plugin
2.  go to your firefox settings directory
3.  find your way into your profile/extensions/VMWare.../plugins
4.  way down here you'll find a vmware-vmrc
    1.  to be safe enable execution permission on this and all the other
        vmware scripts in this folder, in the bin(vmware-vmrc) and in
        lib (wrapper-gtk24.sh) folders in this directory
5.  now you can directly call, setup a shortcut or start vmware-vmrc

        Linux:
        vmware-vmrc -h [<hostname>:<port>] [-u <username> -p <password>] [-M <moid> | <datastore path>]

        Windows:
        vmware-vmrc.exe -h <hostname>:<port> [-u <username> -p <password>] -M <moid> | <datastore path>

<!-- -->

1.  if you leave off command parameters it will just ask you in the GUI

The port number is really important, no idea what moid is yet. And walla
it seems to work. It also seems to be more reliable than the web
interface (note there is a tool in the web interface to create a
shortcut that does the above, and big surprise it doesn't work in
Firefox 3.6 hence the hack around).

<a href="http://communities.vmware.com/message/999988;jsessionid=A135EF8314A4068012697572DC180568" class="ext-link"> Where
I found the answer</a>

-   Posted: 2010-06-08 01:22 (Updated: 2011-01-16 20:04)
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [firefox](category/firefox.html)
    [virtualization](category/virtualization.html)
    [vmware](category/vmware.html)

Comments
--------

No comments.
