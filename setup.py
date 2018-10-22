# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

"""Pootle filesystem plugins
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='pootle_ws',
    version='0.0.1',
    description='Pootle WS',
    long_description="Pootle WebSocket hookup",
    url='https://github.com/translate/pootle_ws',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL3',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='pootle filesystem plugins',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pootle', "channels==2.1.5"],
)
