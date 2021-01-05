#! /bin/zsh
# Lazy way to update a github repository with 1 command instead of 3
# alias gitacp='[path]/gitacp.zsh'
# use by typeing gitacp followed by the commit comment in quotes
git add .
git commit -m $1
git push
