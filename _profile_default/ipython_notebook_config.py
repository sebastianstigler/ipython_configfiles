#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################################################## Python FILE ####
"""
    COPYRIGHT (C) 2015 by Sebastian Stigler

    NAME
        ipython_notebook_config.py

    FIRST RELEASE
        2015-03-16  Sebastian Stigler		sebastian.stigler@htw-aalen.de
"""
###############################################################################
c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
###################################################################### END ####
# vim: ft=python ts=4 sta sw=4 et ai
