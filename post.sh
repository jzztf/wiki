#!/bin/bash

git add .
git commit -m "$*"
git push wiki@coding master
git push wiki@github master
