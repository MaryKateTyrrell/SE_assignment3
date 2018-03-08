#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for se_assignment3.

    This file was generated with PyScaffold 3.0.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup, find_packages

setup(name="Solve_led", 
      version="0.1",
      description="Basic System Info for COMP30670",
      url="",
      author="Mary-Kate Tyrrell",
      author_email="mary.tyrrell@ucdconnect.ie",
      license="GPL3",
      packages=['Assignment'],
      entry_points={'console_scripts':['Solve_led=Assignment.cli:main'],
                    }
      )


