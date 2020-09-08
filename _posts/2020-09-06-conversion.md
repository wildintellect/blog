---
layout: post
title:  "Converting old site to a new static site generator"
date:   2020-09-06 22:01:09 -0700
categories: blog
---
This post is in incomplete walkthrough of converting my old blog that was built with TRAC to a static site generated blog, as of know with jekyll just to get up quickly with github pages.

## Dump the site

1. [Grab and archive](https://handyman.dulare.com/advanced-wget-website-mirroring/) the existing site,
using wget to mirror it so you have a working copy.

```
wget --mirror --convert-links --adjust-extension --page-requisites  http://www.mywebsite.com/
```

One could find a way to dump records from the existing site database and then convert the content, but that requires customizing the dump. It also doesn't make a usable archive of the old site that you can dig through.

## Convert the html to markdown

Using Pandoc, generally like so
`pandoc -f html -t markdown`


Find the content, and ignore everything else. The content can be located with the following html tag
`<div id="blog-main">` , and I followed these [tips](http://www.cantoni.org/2019/01/27/converting-html-markdown-using-pandoc)

```
#!/bin/bash
echo "converting $1"
cat $1 | sed '1,/<div class="blog-main">/d' | sed '/<div class="asset-footer">/,/<\/html>/d' | pandoc --wrap=none --from html --to markdown_strict > $1.md
```
Won't quite work, since we just want what's in the div tag, but not the tag.

Following additional [ideas](https://stackoverflow.com/questions/21015587/get-content-between-a-pair-of-html-tags-using-bash).


```
#!/bin/bash
echo "converting $1"
xmllint --html --xpath "//div[@id='blog-main']/node()" $1 | pandoc --wrap=none --atx-headers --from html-native_divs-native_spans --to markdown_github > $1.md
```
github markdown drops the extra attributes from the headers (header_attributes in pandoc, there's probably a more direct way), but we want those for out mardown headers.


Now we can run the script over all the files to create markdowns of every post.
```
find *.html -exec ./trac2md.sh '{}' \;
```

1. Next in a new repo setup for Jekyll on Github Pages, going to copy all the markdown files in as posts.
1. Need to also grab all the files from the raw-attachments folder and put them into assets. These are all the images used in posts and files attached (pdfs, etc...) `mv raw-attachments/*/* ../blog/assets`

We could have added command line args to set some of the meta tags but just added it to a filter that also sets the title based on the top level 1 header.

```
pandoc -s _drafts/airlinemap.md -o _drafts/airlinemap.2.md --filter assets/metadata.py
```


```
# links to attachments (can be images) need to be fixed
# before
../raw-attachment/blog/babyquail/babyquail.jpg

# The regex to find them
../raw-attachment/blog/.*?/

# after
attachments/babyquail.jpg

#Now apply with sed
find *.md -type f -exec sed 's|../raw-attachment/blog/.*?/|attachments|g' {} + | less
find *.md -type f -exec sed -i 's|../raw-attachment/blog/.*?/|attachments|g' {} +

# The more complicated ones, need to also drop the .html at the end
../attachment/blog/babyquail/babyquail.jpg.html

```
