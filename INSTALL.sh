#!/bin/bash
# vim: ft=sh:tw=80:ts=4:sta:sw=4:si:ci
#************************************************************** SHELL SCRIPT ***
#   NAME
#       INSTALL.sh -- Install config files and extensions for IPython
#
#   FIRST RELEASE
#       2015-04-08  Sebastian Stigler		sebastian.stigler@htw-aalen.de
#
#   COPYRIGHT (C) 2015
#*******************************************************************************

mkdir -p $(ipython locate)/profile_default/static/custom/
mkdir -p $(ipython locate)/profile_sympy/static/custom/
mkdir -p $(ipython locate)/extensions
mkdir -p $(ipython locate)/nbextensions

ln -sf $(pwd)/custom.css $(ipython locate)/profile_default/static/custom
ln -sf $(pwd)/custom.css $(ipython locate)/profile_sympy/static/custom

ln -sf $(pwd)/extensions/* $(ipython locate)/extensions
ln -sf $(pwd)/_profile_default/*.py $(ipython locate)/profile_default
ln -sf $(pwd)/_profile_sympy/*.py $(ipython locate)/profile_sympy

python nbextensions/setup.py install --profile default
python nbextensions/setup.py install --profile sympy
#*********************************************************************** END ***
