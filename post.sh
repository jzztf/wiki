#!/bin/bash

git add .
git commit -m $1
git push wiki@coding master
git push wiki@github master
