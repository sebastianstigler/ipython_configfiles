#!/usr/bin/env python3
############################################################## Python FILE ####
"""
    COPYRIGHT (C) 2015 by Sebastian Stigler

    NAME
        plantuml.py

    DESCRIPTION
        An Plantuml extension for generating UML figures from within ipython
        notebook.

    FIRST RELEASE
        2015-04-01  Sebastian Stigler		sebastian.stigler@htw-aalen.de

"""
###############################################################################

import os
from os.path import abspath, dirname, join
from IPython.core.magic import magics_class, cell_magic, Magics
from IPython.display import Image, SVG


@magics_class
class Plantuml(Magics):

    @cell_magic
    def plantuml(self, line, cell):
        """Generate and display a figure using Plantuml.
        Usage:
            %java -jar /opt/plantuml/plantuml.jar -tsvg filname
        """
        self.filename = line
        self.code = cell

        with open(self.filename + ".plt", "w") as file:
            file.write(self.code)

        self.jarfile = join(dirname(abspath(__file__)), 'plantuml.jar')
        os.system("java -jar %s -tsvg %s.plt" % (self.jarfile, self.filename))
        return SVG(filename=self.filename + ".svg")


def load_ipython_extension(ipython):
    ipython.register_magics(Plantuml)

###################################################################### END ####
# vim: ft=python ts=4 sta sw=4 et ai
