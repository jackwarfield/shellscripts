#! /bin/zsh
# Open argument in vim, and then run it in python when vim is closed.
# alias vpy='[path]/vpy.zsh'
vim $1
python3 $1
