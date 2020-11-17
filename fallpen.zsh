#! /bin/zsh
# finds files (recursive through directories), and then opens all of them
# alias fallpen='[path]/fallpen.zsh'
find $1 -exec open {} \;
