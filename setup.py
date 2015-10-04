# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

"""
This module allows installation of capablanca as a pip package:
    pip install .
"""

from distutils.core import setup

# Set pip requirements from the requirements file
requirements = []
with open('requirements.txt', 'rb') as req_file:
    for line in req_file.readlines():
        requirements.append(line.rstrip())

setup(
    name='capablanca',
    version='1.0',
    description='A small chess player',
    long_description=open('README.md').read(),
    author='Dario Blanco',
    author_email='dario@darioblanco.com',
    license='LICENSE',
    url='http://darioblanco.com',
    install_requires=requirements,
    packages=['capablanca'],
    entry_points={
        'console_scripts': [
            'capablanca = capablanca.play:play',
        ]
    },
)
