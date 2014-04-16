#!/usr/bin/env bash

# open rxvt-unicode with a random pixmap background
urxvt -pixmap "`find /home/jonasg/Pictures/tiles/ -name '*.png' | sort -R | head -n 1`;style=tiled"

