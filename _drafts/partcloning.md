# Un-doing the partition mess from a dual boot

More and more, when I make a dual boot system it turns out that 6 months to a year down the line the windows partition just isn't needed anymore. But now you've got 10GB+ of disk just sitting out at the front of the drive.

Over the holiday I tackled a shuffling of partitions and here's the important tips I picked up.

1.  Copy your important data to another drive (an external usb is great)
2.  Using the Ubuntu disk tools like gparted blank the space where you want to move stuff to.
3.  Using the <a href="http://clonezilla.org/" class="ext-link"> Clonezilla live disc</a> (and either partimage or <a href="http://partclone.org/" class="ext-link"> partclone</a> \[the new variant that handles ext4\]) clone your / partition over to the new space.
4.  Relabel the UUID of this new partition, otherwise it will be identical to the UUID of the original and the bootloader will quasi load both

          uuidgen
          tune2fs /dev/hdaX -U numbergeneratedbyuuidgen

5.Edit your grub config to boot the new drive. If you reboot into Ubuntu running the update-grub will find it.

1.  Once you're sure you can boot the relocated / you can add the empty space onto your /home (I always recommend separate / and /home partitions)

Things I also recommend:

1.  Converting ext3 to ext4
2.  Creating a Private directory for storing encrypted stuff.

-   Posted: 2011-01-16 20:03
-   Author: [wildintellect](author/wildintellect.html)
-   Categories: [ubuntu](category/ubuntu.html) [linux](category/linux.html)

## Comments

No comments.
