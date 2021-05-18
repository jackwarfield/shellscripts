#! /bin/zsh

mkdir /Volumes/brutus/astro-$(date +%s)
rsync -avzh /Users/jtw5zc/astro/* "/Volumes/brutus/astro-$(date +%s)/"
