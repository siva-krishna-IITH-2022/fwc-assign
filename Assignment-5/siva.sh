#!/bin/bash
#
#Download python and latex templates
#
#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math
#
#Test Latex Installation
#Uncomment only the following lines and comment the above line
#To run line assignment


cd /sdcard/DCIM/Assignment-5/codes
python3 circle.py

cd /sdcard/DCIM/Assignment-5/docs
#pdflatex circle.tex
termux-open circle.pdf

#cd /sdcard/download/matrix/circle
#python3 circlemeg.py
#pdflatex circle.tex
#termux-open circle.pdf
