#!/bin/bash


./toc.py linux
./toc.py python
./toc.py front-end
./toc.py tools
./toc.py others
./toc.py notes

git add .
git commit -m "$*"
git push wiki@coding master
git push wiki@github master
